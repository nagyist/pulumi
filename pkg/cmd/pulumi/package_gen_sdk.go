// Copyright 2016-2022, Pulumi Corporation.
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

package main

import (
	"fmt"
	"os"
	"path/filepath"

	"github.com/spf13/cobra"

	javagen "github.com/pulumi/pulumi-java/pkg/codegen/java"

	"github.com/pulumi/pulumi/pkg/v3/codegen/dotnet"
	"github.com/pulumi/pulumi/pkg/v3/codegen/nodejs"
	"github.com/pulumi/pulumi/pkg/v3/codegen/python"
	"github.com/pulumi/pulumi/pkg/v3/codegen/schema"
	"github.com/pulumi/pulumi/sdk/v3/go/common/util/cmdutil"
	"github.com/pulumi/pulumi/sdk/v3/go/common/util/contract"
)

func newGenSdkCommand() *cobra.Command {
	var language string
	var out string
	cmd := &cobra.Command{
		Use:   "gen-sdk <schema_source>",
		Args:  cobra.ExactArgs(1),
		Short: "Generate SDK(s) from a package or schema",
		Long: `Generate SDK(s) from a package or schema.

<schema_source> can be a package name, the path to a plugin binary, or the path to a schema file.`,
		Run: cmdutil.RunFunc(func(cmd *cobra.Command, args []string) error {
			source := args[0]

			pkg, err := schemaFromSchemaSource(source)
			if err != nil {
				return err
			}
			if language == "all" {
				for _, lang := range []string{"dotnet", "go", "java", "nodejs", "python"} {
					// If we're codegen'ing all languages, we'll generate a subdirectory for each one.
					root := filepath.Join(out, language)
					err := genSDK(lang, root, pkg)
					if err != nil {
						return err
					}
				}
				return nil
			}
			return genSDK(language, out, pkg)
		}),
	}
	cmd.Flags().StringVarP(&language, "language", "", "all",
		"The SDK language to generate: [nodejs|python|go|dotnet|java|all]")
	cmd.Flags().StringVarP(&out, "out", "o", "./sdk",
		"The directory to write the SDK to")
	return cmd
}

func genSDK(language, out string, pkg *schema.Package) error {
	cwd, err := os.Getwd()
	if err != nil {
		return fmt.Errorf("could not resolve current working directory: %w", err)
	}

	// Translate well known languages to runtimes
	switch language {
	case "csharp", "c#":
		language = "dotnet" //nolint:goconst
	case "typescript":
		language = "nodejs" //nolint:goconst
	}

	var f func(string, *schema.Package, map[string][]byte) error

	writeWrapper := func(
		f func(string, *schema.Package, map[string][]byte) (map[string][]byte, error),
	) func(string, *schema.Package, map[string][]byte) error {
		return func(directory string, p *schema.Package, extraFiles map[string][]byte) error {
			m, err := f("pulumi", p, extraFiles)
			if err != nil {
				return err
			}

			err = os.RemoveAll(directory)
			if err != nil && !os.IsNotExist(err) {
				return err
			}
			for k, v := range m {
				path := filepath.Join(directory, k)
				err := os.MkdirAll(filepath.Dir(path), 0700)
				if err != nil {
					return err
				}
				err = os.WriteFile(path, v, 0600)
				if err != nil {
					return err
				}
			}
			return nil
		}
	}

	switch language {
	case "dotnet":
		f = writeWrapper(dotnet.GeneratePackage)
	case "nodejs":
		f = writeWrapper(nodejs.GeneratePackage)
	case "python": //nolint:goconst
		f = writeWrapper(python.GeneratePackage)
	case "java":
		f = writeWrapper(javagen.GeneratePackage)
	default:
		f = func(directory string, pkg *schema.Package, extraFiles map[string][]byte) error {
			// Ensure the target directory is clean, but created.
			err = os.RemoveAll(directory)
			if err != nil && !os.IsNotExist(err) {
				return err
			}
			err := os.MkdirAll(directory, 0700)
			if err != nil {
				return err
			}

			jsonBytes, err := pkg.MarshalJSON()
			if err != nil {
				return err
			}

			host, err := newPluginHost()
			if err != nil {
				return fmt.Errorf("could not create plugin host: %w", err)
			}
			defer contract.IgnoreClose(host)

			languagePlugin, err := host.LanguageRuntime(cwd, cwd, language, nil)
			if err != nil {
				return err
			}

			err = languagePlugin.GeneratePackage(directory, string(jsonBytes), extraFiles)
			if err != nil {
				return err
			}

			return nil
		}
	}

	err = f(out, pkg, nil)
	if err != nil {
		return err
	}
	return nil
}
