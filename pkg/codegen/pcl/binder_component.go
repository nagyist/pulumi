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
		DirPath(b.options.dirPath),
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
	return diagnostics
}
