// Copyright 2016-2020, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

//nolint:goconst
package pcl

import (
	"github.com/hashicorp/hcl/v2"
	"github.com/pulumi/pulumi/pkg/v3/codegen/hcl2/model"
	hclsyntax "github.com/pulumi/pulumi/pkg/v3/codegen/hcl2/syntax"
	"io/fs"
	"os"
	"path/filepath"
)

// componentVariableType returns the type of the variable of which the value is a component.
// The type is derived from the outputs of the sub-program of the component into an ObjectType
func componentVariableType(program *Program) model.Type {
	properties := map[string]model.Type{}
	for _, node := range program.Nodes {
		switch node := node.(type) {
		case *OutputVariable:
			properties[node.LogicalName()] = node.Type()
		}
	}

	return &model.ObjectType{Properties: properties}
}

type componentInput struct {
	key      string
	required bool
}

func componentInputs(program *Program) map[string]componentInput {
	inputs := map[string]componentInput{}
	for _, node := range program.Nodes {
		switch node := node.(type) {
		case *ConfigVariable:
			inputs[node.LogicalName()] = componentInput{
				required: node.DefaultValue == nil,
				key:      node.LogicalName(),
			}
		}
	}

	return inputs
}

func contains(slice []string, item string) bool {
	set := make(map[string]struct{}, len(slice))
	for _, s := range slice {
		set[s] = struct{}{}
	}

	_, ok := set[item]
	return ok
}

func (b *binder) bindComponent(node *Component) hcl.Diagnostics {
	block, diagnostics := model.BindBlock(node.syntax, model.StaticScope(b.root), b.tokens, b.options.modelOptions()...)
	node.Definition = block

	// check we can use components and load the program
	if b.options.dirPath == "" {
		diagnostics = diagnostics.Append(errorf(node.SyntaxNode().Range(),
			"components require the binder to have set a directory path"))
		return diagnostics
	}

	// bind the component here as if it was a new program
	componentSourceDir := filepath.Join(b.options.dirPath, node.source)

	parser := hclsyntax.NewParser()
	// Load all .pp files in the components' subdirectory
	err := filepath.WalkDir(componentSourceDir, func(path string, d fs.DirEntry, err error) error {
		if d.IsDir() {
			return nil
		}

		if filepath.Ext(path) == ".pp" {
			file, err := os.Open(path)
			if err != nil {
				return err
			}

			err = parser.ParseFile(file, filepath.Base(path))
			if err != nil {
				return err
			}
			diags := parser.Diagnostics
			if diags.HasErrors() {
				return diags
			}
		}
		return nil
	})

	if err != nil {
		diagnostics = diagnostics.Append(errorf(node.SyntaxNode().Range(), err.Error()))
		return diagnostics
	}

	allowMissingProperties := func(options *bindOptions) {
		options.allowMissingProperties = b.options.allowMissingProperties
	}

	allowMissingVariables := func(options *bindOptions) {
		options.allowMissingVariables = b.options.allowMissingVariables
	}

	componentProgram, programDiags, err := BindProgram(parser.Files,
		Loader(b.options.loader),
		DirPath(componentSourceDir),
		allowMissingProperties,
		allowMissingVariables)

	if err != nil {
		diagnostics = diagnostics.Append(errorf(node.SyntaxNode().Range(), err.Error()))
		return diagnostics
	}

	if programDiags.HasErrors() || componentProgram == nil {
		diagnostics = diagnostics.Append(errorf(node.SyntaxNode().Range(), programDiags.Error()))
		return diagnostics
	}

	node.program = componentProgram
	node.VariableType = componentVariableType(componentProgram)
	node.fullPath = componentSourceDir

	componentInputs := componentInputs(componentProgram)
	providedInputs := []string{}

	var options *model.Block
	for _, item := range block.Body.Items {
		switch item := item.(type) {
		case *model.Attribute:
			// logical name is a special attribute
			if item.Name == LogicalNamePropertyKey {
				logicalName, lDiags := getStringAttrValue(item)
				if lDiags != nil {
					diagnostics = diagnostics.Append(lDiags)
				} else {
					node.logicalName = logicalName
				}
				continue
			}
			// all other attributes are part of the inputs
			_, knownInput := componentInputs[item.Name]

			if !knownInput {
				diagnostics = append(diagnostics, unsupportedAttribute(item.Name, item.Syntax.NameRange))
				return diagnostics
			}

			node.Inputs = append(node.Inputs, item)
			providedInputs = append(providedInputs, item.Name)
		case *model.Block:
			switch item.Type {
			case "options":
				if options != nil {
					diagnostics = append(diagnostics, duplicateBlock(item.Type, item.Syntax.TypeRange))
				} else {
					options = item
				}
			default:
				diagnostics = append(diagnostics, unsupportedBlock(item.Type, item.Syntax.TypeRange))
			}
		}
	}

	// check that all required inputs are actually set
	for inputKey, componentInput := range componentInputs {
		if componentInput.required && !contains(providedInputs, inputKey) {
			diagnostics = append(diagnostics, missingRequiredAttribute(inputKey, node.SyntaxNode().Range()))
		}
	}

	if options != nil {
		resourceOptions, optionsDiags := bindResourceOptions(options)
		diagnostics = append(diagnostics, optionsDiags...)
		node.Options = resourceOptions
	}

	return diagnostics
}
