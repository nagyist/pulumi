"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2016-2023, Pulumi Corporation.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.struct_pb2
import pulumi.codegen.hcl_pb2
import pulumi.plugin_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class ProgramInfo(google.protobuf.message.Message):
    """ProgramInfo are the common set of options that a language runtime needs to execute or query a program. This
    is filled in by the engine based on where the `Pulumi.yaml` file was, the `runtime.options` property, and
    the `main` property.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ROOT_DIRECTORY_FIELD_NUMBER: builtins.int
    PROGRAM_DIRECTORY_FIELD_NUMBER: builtins.int
    ENTRY_POINT_FIELD_NUMBER: builtins.int
    OPTIONS_FIELD_NUMBER: builtins.int
    root_directory: builtins.str
    """the root of the project, where the `Pulumi.yaml` file is located."""
    program_directory: builtins.str
    """the absolute path to the directory of the program to execute. Generally, but not required to be,
    underneath the root directory.
    """
    entry_point: builtins.str
    """the entry point of the program, normally '.' meaning to just use the program directory, but can also be
    a filename inside the program directory. How that filename is interpreted, if at all, is language
    specific.
    """
    @property
    def options(self) -> google.protobuf.struct_pb2.Struct:
        """JSON style options from the `Pulumi.yaml` runtime options section."""
    def __init__(
        self,
        *,
        root_directory: builtins.str = ...,
        program_directory: builtins.str = ...,
        entry_point: builtins.str = ...,
        options: google.protobuf.struct_pb2.Struct | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["options", b"options"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["entry_point", b"entry_point", "options", b"options", "program_directory", b"program_directory", "root_directory", b"root_directory"]) -> None: ...

global___ProgramInfo = ProgramInfo

@typing_extensions.final
class AboutRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INFO_FIELD_NUMBER: builtins.int
    @property
    def info(self) -> global___ProgramInfo:
        """the program info to use."""
    def __init__(
        self,
        *,
        info: global___ProgramInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["info", b"info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["info", b"info"]) -> None: ...

global___AboutRequest = AboutRequest

@typing_extensions.final
class AboutResponse(google.protobuf.message.Message):
    """AboutResponse returns runtime information about the language."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class MetadataEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    EXECUTABLE_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    executable: builtins.str
    """the primary executable for the runtime of this language."""
    version: builtins.str
    """the version of the runtime for this language."""
    @property
    def metadata(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """other information about this language."""
    def __init__(
        self,
        *,
        executable: builtins.str = ...,
        version: builtins.str = ...,
        metadata: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["executable", b"executable", "metadata", b"metadata", "version", b"version"]) -> None: ...

global___AboutResponse = AboutResponse

@typing_extensions.final
class GetProgramDependenciesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_FIELD_NUMBER: builtins.int
    PWD_FIELD_NUMBER: builtins.int
    PROGRAM_FIELD_NUMBER: builtins.int
    TRANSITIVEDEPENDENCIES_FIELD_NUMBER: builtins.int
    INFO_FIELD_NUMBER: builtins.int
    project: builtins.str
    """the project name, the engine always sets this to "deprecated" now."""
    pwd: builtins.str
    """the program's working directory. Deprecated, use info.program_directory instead."""
    program: builtins.str
    """the path to the program. Deprecated, use info.entry_point instead."""
    transitiveDependencies: builtins.bool
    """if transitive dependencies should be included in the result."""
    @property
    def info(self) -> global___ProgramInfo:
        """the program info to use to calculate dependencies."""
    def __init__(
        self,
        *,
        project: builtins.str = ...,
        pwd: builtins.str = ...,
        program: builtins.str = ...,
        transitiveDependencies: builtins.bool = ...,
        info: global___ProgramInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["info", b"info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["info", b"info", "program", b"program", "project", b"project", "pwd", b"pwd", "transitiveDependencies", b"transitiveDependencies"]) -> None: ...

global___GetProgramDependenciesRequest = GetProgramDependenciesRequest

@typing_extensions.final
class DependencyInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    name: builtins.str
    """The name of the dependency."""
    version: builtins.str
    """The version of the dependency."""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        version: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name", "version", b"version"]) -> None: ...

global___DependencyInfo = DependencyInfo

@typing_extensions.final
class GetProgramDependenciesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEPENDENCIES_FIELD_NUMBER: builtins.int
    @property
    def dependencies(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DependencyInfo]:
        """the dependencies of this program"""
    def __init__(
        self,
        *,
        dependencies: collections.abc.Iterable[global___DependencyInfo] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["dependencies", b"dependencies"]) -> None: ...

global___GetProgramDependenciesResponse = GetProgramDependenciesResponse

@typing_extensions.final
class GetRequiredPluginsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_FIELD_NUMBER: builtins.int
    PWD_FIELD_NUMBER: builtins.int
    PROGRAM_FIELD_NUMBER: builtins.int
    INFO_FIELD_NUMBER: builtins.int
    project: builtins.str
    """the project name, the engine always sets this to "deprecated" now."""
    pwd: builtins.str
    """the program's working directory. Deprecated, use info.program_directory instead."""
    program: builtins.str
    """the path to the program. Deprecated, use info.entry_point instead."""
    @property
    def info(self) -> global___ProgramInfo:
        """the program info to use to calculate plugins."""
    def __init__(
        self,
        *,
        project: builtins.str = ...,
        pwd: builtins.str = ...,
        program: builtins.str = ...,
        info: global___ProgramInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["info", b"info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["info", b"info", "program", b"program", "project", b"project", "pwd", b"pwd"]) -> None: ...

global___GetRequiredPluginsRequest = GetRequiredPluginsRequest

@typing_extensions.final
class GetRequiredPluginsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PLUGINS_FIELD_NUMBER: builtins.int
    @property
    def plugins(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[pulumi.plugin_pb2.PluginDependency]:
        """a list of plugins required by this program."""
    def __init__(
        self,
        *,
        plugins: collections.abc.Iterable[pulumi.plugin_pb2.PluginDependency] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["plugins", b"plugins"]) -> None: ...

global___GetRequiredPluginsResponse = GetRequiredPluginsResponse

@typing_extensions.final
class GetRequiredPackagesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INFO_FIELD_NUMBER: builtins.int
    @property
    def info(self) -> global___ProgramInfo:
        """the program info to use to calculate packages."""
    def __init__(
        self,
        *,
        info: global___ProgramInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["info", b"info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["info", b"info"]) -> None: ...

global___GetRequiredPackagesRequest = GetRequiredPackagesRequest

@typing_extensions.final
class GetRequiredPackagesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PACKAGES_FIELD_NUMBER: builtins.int
    @property
    def packages(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[pulumi.plugin_pb2.PackageDependency]:
        """a list of packages required by this program."""
    def __init__(
        self,
        *,
        packages: collections.abc.Iterable[pulumi.plugin_pb2.PackageDependency] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["packages", b"packages"]) -> None: ...

global___GetRequiredPackagesResponse = GetRequiredPackagesResponse

@typing_extensions.final
class RunRequest(google.protobuf.message.Message):
    """RunRequest asks the interpreter to execute a program."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class ConfigEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    PROJECT_FIELD_NUMBER: builtins.int
    STACK_FIELD_NUMBER: builtins.int
    PWD_FIELD_NUMBER: builtins.int
    PROGRAM_FIELD_NUMBER: builtins.int
    ARGS_FIELD_NUMBER: builtins.int
    CONFIG_FIELD_NUMBER: builtins.int
    DRYRUN_FIELD_NUMBER: builtins.int
    PARALLEL_FIELD_NUMBER: builtins.int
    MONITOR_ADDRESS_FIELD_NUMBER: builtins.int
    QUERYMODE_FIELD_NUMBER: builtins.int
    CONFIGSECRETKEYS_FIELD_NUMBER: builtins.int
    ORGANIZATION_FIELD_NUMBER: builtins.int
    CONFIGPROPERTYMAP_FIELD_NUMBER: builtins.int
    INFO_FIELD_NUMBER: builtins.int
    LOADER_TARGET_FIELD_NUMBER: builtins.int
    ATTACH_DEBUGGER_FIELD_NUMBER: builtins.int
    project: builtins.str
    """the project name."""
    stack: builtins.str
    """the name of the stack being deployed into."""
    pwd: builtins.str
    """the program's working directory."""
    program: builtins.str
    """the path to the program to execute. Deprecated, use info.entry_point instead."""
    @property
    def args(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """any arguments to pass to the program."""
    @property
    def config(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """the configuration variables to apply before running."""
    dryRun: builtins.bool
    """true if we're only doing a dryrun (preview)."""
    parallel: builtins.int
    """the degree of parallelism for resource operations (<=1 for serial)."""
    monitor_address: builtins.str
    """the address for communicating back to the resource monitor."""
    queryMode: builtins.bool
    """true if we're only doing a query."""
    @property
    def configSecretKeys(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """the configuration keys that have secret values."""
    organization: builtins.str
    """the organization of the stack being deployed into."""
    @property
    def configPropertyMap(self) -> google.protobuf.struct_pb2.Struct:
        """the configuration variables to apply before running."""
    @property
    def info(self) -> global___ProgramInfo:
        """the program info to use to execute the program."""
    loader_target: builtins.str
    """The target of a codegen.LoaderServer to use for loading schemas."""
    attach_debugger: builtins.bool
    """true if the language host is supposed to start the program under a debugger."""
    def __init__(
        self,
        *,
        project: builtins.str = ...,
        stack: builtins.str = ...,
        pwd: builtins.str = ...,
        program: builtins.str = ...,
        args: collections.abc.Iterable[builtins.str] | None = ...,
        config: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        dryRun: builtins.bool = ...,
        parallel: builtins.int = ...,
        monitor_address: builtins.str = ...,
        queryMode: builtins.bool = ...,
        configSecretKeys: collections.abc.Iterable[builtins.str] | None = ...,
        organization: builtins.str = ...,
        configPropertyMap: google.protobuf.struct_pb2.Struct | None = ...,
        info: global___ProgramInfo | None = ...,
        loader_target: builtins.str = ...,
        attach_debugger: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["configPropertyMap", b"configPropertyMap", "info", b"info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["args", b"args", "attach_debugger", b"attach_debugger", "config", b"config", "configPropertyMap", b"configPropertyMap", "configSecretKeys", b"configSecretKeys", "dryRun", b"dryRun", "info", b"info", "loader_target", b"loader_target", "monitor_address", b"monitor_address", "organization", b"organization", "parallel", b"parallel", "program", b"program", "project", b"project", "pwd", b"pwd", "queryMode", b"queryMode", "stack", b"stack"]) -> None: ...

global___RunRequest = RunRequest

@typing_extensions.final
class RunResponse(google.protobuf.message.Message):
    """RunResponse is the response back from the interpreter/source back to the monitor."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ERROR_FIELD_NUMBER: builtins.int
    BAIL_FIELD_NUMBER: builtins.int
    error: builtins.str
    """An unhandled error if any occurred."""
    bail: builtins.bool
    """An error happened.  And it was reported to the user.  Work should stop immediately
    with nothing further to print to the user.  This corresponds to a "result.Bail()"
    value in the 'go' layer.
    """
    def __init__(
        self,
        *,
        error: builtins.str = ...,
        bail: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["bail", b"bail", "error", b"error"]) -> None: ...

global___RunResponse = RunResponse

@typing_extensions.final
class InstallDependenciesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DIRECTORY_FIELD_NUMBER: builtins.int
    IS_TERMINAL_FIELD_NUMBER: builtins.int
    INFO_FIELD_NUMBER: builtins.int
    USE_LANGUAGE_VERSION_TOOLS_FIELD_NUMBER: builtins.int
    directory: builtins.str
    """the program's working directory. Deprecated, use info.program_directory instead."""
    is_terminal: builtins.bool
    """if we are running in a terminal and should use ANSI codes"""
    @property
    def info(self) -> global___ProgramInfo:
        """the program info to use to execute the plugin."""
    use_language_version_tools: builtins.bool
    """if we should use language version tools like pyenv or"""
    def __init__(
        self,
        *,
        directory: builtins.str = ...,
        is_terminal: builtins.bool = ...,
        info: global___ProgramInfo | None = ...,
        use_language_version_tools: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["info", b"info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["directory", b"directory", "info", b"info", "is_terminal", b"is_terminal", "use_language_version_tools", b"use_language_version_tools"]) -> None: ...

global___InstallDependenciesRequest = InstallDependenciesRequest

@typing_extensions.final
class InstallDependenciesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STDOUT_FIELD_NUMBER: builtins.int
    STDERR_FIELD_NUMBER: builtins.int
    stdout: builtins.bytes
    """a line of stdout text."""
    stderr: builtins.bytes
    """a line of stderr text."""
    def __init__(
        self,
        *,
        stdout: builtins.bytes = ...,
        stderr: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["stderr", b"stderr", "stdout", b"stdout"]) -> None: ...

global___InstallDependenciesResponse = InstallDependenciesResponse

@typing_extensions.final
class RuntimeOptionsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INFO_FIELD_NUMBER: builtins.int
    @property
    def info(self) -> global___ProgramInfo:
        """The current program info used to evaluate which prompts should be asked."""
    def __init__(
        self,
        *,
        info: global___ProgramInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["info", b"info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["info", b"info"]) -> None: ...

global___RuntimeOptionsRequest = RuntimeOptionsRequest

@typing_extensions.final
class RuntimeOptionPrompt(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _RuntimeOptionType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _RuntimeOptionTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[RuntimeOptionPrompt._RuntimeOptionType.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STRING: RuntimeOptionPrompt._RuntimeOptionType.ValueType  # 0
        INT32: RuntimeOptionPrompt._RuntimeOptionType.ValueType  # 1

    class RuntimeOptionType(_RuntimeOptionType, metaclass=_RuntimeOptionTypeEnumTypeWrapper): ...
    STRING: RuntimeOptionPrompt.RuntimeOptionType.ValueType  # 0
    INT32: RuntimeOptionPrompt.RuntimeOptionType.ValueType  # 1

    @typing_extensions.final
    class RuntimeOptionValue(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        PROMPTTYPE_FIELD_NUMBER: builtins.int
        STRINGVALUE_FIELD_NUMBER: builtins.int
        INT32VALUE_FIELD_NUMBER: builtins.int
        DISPLAYNAME_FIELD_NUMBER: builtins.int
        promptType: global___RuntimeOptionPrompt.RuntimeOptionType.ValueType
        stringValue: builtins.str
        int32Value: builtins.int
        displayName: builtins.str
        def __init__(
            self,
            *,
            promptType: global___RuntimeOptionPrompt.RuntimeOptionType.ValueType = ...,
            stringValue: builtins.str = ...,
            int32Value: builtins.int = ...,
            displayName: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["displayName", b"displayName", "int32Value", b"int32Value", "promptType", b"promptType", "stringValue", b"stringValue"]) -> None: ...

    KEY_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    PROMPTTYPE_FIELD_NUMBER: builtins.int
    CHOICES_FIELD_NUMBER: builtins.int
    DEFAULT_FIELD_NUMBER: builtins.int
    key: builtins.str
    description: builtins.str
    promptType: global___RuntimeOptionPrompt.RuntimeOptionType.ValueType
    @property
    def choices(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___RuntimeOptionPrompt.RuntimeOptionValue]: ...
    @property
    def default(self) -> global___RuntimeOptionPrompt.RuntimeOptionValue: ...
    def __init__(
        self,
        *,
        key: builtins.str = ...,
        description: builtins.str = ...,
        promptType: global___RuntimeOptionPrompt.RuntimeOptionType.ValueType = ...,
        choices: collections.abc.Iterable[global___RuntimeOptionPrompt.RuntimeOptionValue] | None = ...,
        default: global___RuntimeOptionPrompt.RuntimeOptionValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["default", b"default"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["choices", b"choices", "default", b"default", "description", b"description", "key", b"key", "promptType", b"promptType"]) -> None: ...

global___RuntimeOptionPrompt = RuntimeOptionPrompt

@typing_extensions.final
class RuntimeOptionsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROMPTS_FIELD_NUMBER: builtins.int
    @property
    def prompts(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___RuntimeOptionPrompt]:
        """additional prompts to ask the user"""
    def __init__(
        self,
        *,
        prompts: collections.abc.Iterable[global___RuntimeOptionPrompt] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["prompts", b"prompts"]) -> None: ...

global___RuntimeOptionsResponse = RuntimeOptionsResponse

@typing_extensions.final
class RunPluginRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PWD_FIELD_NUMBER: builtins.int
    PROGRAM_FIELD_NUMBER: builtins.int
    ARGS_FIELD_NUMBER: builtins.int
    ENV_FIELD_NUMBER: builtins.int
    INFO_FIELD_NUMBER: builtins.int
    pwd: builtins.str
    """the program's working directory."""
    program: builtins.str
    """the path to the program to execute. Deprecated, use info.entry_point instead."""
    @property
    def args(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """any arguments to pass to the program."""
    @property
    def env(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """any environment variables to set as part of the program."""
    @property
    def info(self) -> global___ProgramInfo:
        """the program info to use to execute the plugin."""
    def __init__(
        self,
        *,
        pwd: builtins.str = ...,
        program: builtins.str = ...,
        args: collections.abc.Iterable[builtins.str] | None = ...,
        env: collections.abc.Iterable[builtins.str] | None = ...,
        info: global___ProgramInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["info", b"info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["args", b"args", "env", b"env", "info", b"info", "program", b"program", "pwd", b"pwd"]) -> None: ...

global___RunPluginRequest = RunPluginRequest

@typing_extensions.final
class RunPluginResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STDOUT_FIELD_NUMBER: builtins.int
    STDERR_FIELD_NUMBER: builtins.int
    EXITCODE_FIELD_NUMBER: builtins.int
    stdout: builtins.bytes
    """a line of stdout text."""
    stderr: builtins.bytes
    """a line of stderr text."""
    exitcode: builtins.int
    """the exit code of the provider."""
    def __init__(
        self,
        *,
        stdout: builtins.bytes = ...,
        stderr: builtins.bytes = ...,
        exitcode: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["exitcode", b"exitcode", "output", b"output", "stderr", b"stderr", "stdout", b"stdout"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["exitcode", b"exitcode", "output", b"output", "stderr", b"stderr", "stdout", b"stdout"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["output", b"output"]) -> typing_extensions.Literal["stdout", "stderr", "exitcode"] | None: ...

global___RunPluginResponse = RunPluginResponse

@typing_extensions.final
class GenerateProgramRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class SourceEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    SOURCE_FIELD_NUMBER: builtins.int
    LOADER_TARGET_FIELD_NUMBER: builtins.int
    STRICT_FIELD_NUMBER: builtins.int
    @property
    def source(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """the PCL source of the project."""
    loader_target: builtins.str
    """The target of a codegen.LoaderServer to use for loading schemas."""
    strict: builtins.bool
    """if PCL binding should be strict or not."""
    def __init__(
        self,
        *,
        source: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        loader_target: builtins.str = ...,
        strict: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["loader_target", b"loader_target", "source", b"source", "strict", b"strict"]) -> None: ...

global___GenerateProgramRequest = GenerateProgramRequest

@typing_extensions.final
class GenerateProgramResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class SourceEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.bytes
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.bytes = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    DIAGNOSTICS_FIELD_NUMBER: builtins.int
    SOURCE_FIELD_NUMBER: builtins.int
    @property
    def diagnostics(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[pulumi.codegen.hcl_pb2.Diagnostic]:
        """any diagnostics from code generation."""
    @property
    def source(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.bytes]:
        """the generated program source code."""
    def __init__(
        self,
        *,
        diagnostics: collections.abc.Iterable[pulumi.codegen.hcl_pb2.Diagnostic] | None = ...,
        source: collections.abc.Mapping[builtins.str, builtins.bytes] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["diagnostics", b"diagnostics", "source", b"source"]) -> None: ...

global___GenerateProgramResponse = GenerateProgramResponse

@typing_extensions.final
class GenerateProjectRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class LocalDependenciesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    SOURCE_DIRECTORY_FIELD_NUMBER: builtins.int
    TARGET_DIRECTORY_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    STRICT_FIELD_NUMBER: builtins.int
    LOADER_TARGET_FIELD_NUMBER: builtins.int
    LOCAL_DEPENDENCIES_FIELD_NUMBER: builtins.int
    source_directory: builtins.str
    """the directory to generate the project from."""
    target_directory: builtins.str
    """the directory to generate the project in."""
    project: builtins.str
    """the JSON-encoded pulumi project file."""
    strict: builtins.bool
    """if PCL binding should be strict or not."""
    loader_target: builtins.str
    """The target of a codegen.LoaderServer to use for loading schemas."""
    @property
    def local_dependencies(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """local dependencies to use instead of using the package system. This is a map of package name to a local
        path of a language specific artifact to use for the SDK for that package.
        """
    def __init__(
        self,
        *,
        source_directory: builtins.str = ...,
        target_directory: builtins.str = ...,
        project: builtins.str = ...,
        strict: builtins.bool = ...,
        loader_target: builtins.str = ...,
        local_dependencies: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["loader_target", b"loader_target", "local_dependencies", b"local_dependencies", "project", b"project", "source_directory", b"source_directory", "strict", b"strict", "target_directory", b"target_directory"]) -> None: ...

global___GenerateProjectRequest = GenerateProjectRequest

@typing_extensions.final
class GenerateProjectResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DIAGNOSTICS_FIELD_NUMBER: builtins.int
    @property
    def diagnostics(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[pulumi.codegen.hcl_pb2.Diagnostic]:
        """any diagnostics from code generation."""
    def __init__(
        self,
        *,
        diagnostics: collections.abc.Iterable[pulumi.codegen.hcl_pb2.Diagnostic] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["diagnostics", b"diagnostics"]) -> None: ...

global___GenerateProjectResponse = GenerateProjectResponse

@typing_extensions.final
class GeneratePackageRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class ExtraFilesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.bytes
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.bytes = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    @typing_extensions.final
    class LocalDependenciesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    DIRECTORY_FIELD_NUMBER: builtins.int
    SCHEMA_FIELD_NUMBER: builtins.int
    EXTRA_FILES_FIELD_NUMBER: builtins.int
    LOADER_TARGET_FIELD_NUMBER: builtins.int
    LOCAL_DEPENDENCIES_FIELD_NUMBER: builtins.int
    LOCAL_FIELD_NUMBER: builtins.int
    directory: builtins.str
    """the directory to generate the package in."""
    schema: builtins.str
    """the JSON-encoded schema."""
    @property
    def extra_files(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.bytes]:
        """extra files to copy to the package output."""
    loader_target: builtins.str
    """The target of a codegen.LoaderServer to use for loading schemas."""
    @property
    def local_dependencies(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """local dependencies to use instead of using the package system. This is a map of package name to a local
        path of a language specific artifact to use for the SDK for that package.
        """
    local: builtins.bool
    """if true generates an SDK appropriate for local usage, this may differ from a standard publishable SDK depending
    on the language.
    """
    def __init__(
        self,
        *,
        directory: builtins.str = ...,
        schema: builtins.str = ...,
        extra_files: collections.abc.Mapping[builtins.str, builtins.bytes] | None = ...,
        loader_target: builtins.str = ...,
        local_dependencies: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        local: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["directory", b"directory", "extra_files", b"extra_files", "loader_target", b"loader_target", "local", b"local", "local_dependencies", b"local_dependencies", "schema", b"schema"]) -> None: ...

global___GeneratePackageRequest = GeneratePackageRequest

@typing_extensions.final
class GeneratePackageResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DIAGNOSTICS_FIELD_NUMBER: builtins.int
    @property
    def diagnostics(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[pulumi.codegen.hcl_pb2.Diagnostic]:
        """any diagnostics from code generation."""
    def __init__(
        self,
        *,
        diagnostics: collections.abc.Iterable[pulumi.codegen.hcl_pb2.Diagnostic] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["diagnostics", b"diagnostics"]) -> None: ...

global___GeneratePackageResponse = GeneratePackageResponse

@typing_extensions.final
class PackRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PACKAGE_DIRECTORY_FIELD_NUMBER: builtins.int
    DESTINATION_DIRECTORY_FIELD_NUMBER: builtins.int
    package_directory: builtins.str
    """the directory of a package to pack."""
    destination_directory: builtins.str
    """the directory to write the packed artifact to."""
    def __init__(
        self,
        *,
        package_directory: builtins.str = ...,
        destination_directory: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["destination_directory", b"destination_directory", "package_directory", b"package_directory"]) -> None: ...

global___PackRequest = PackRequest

@typing_extensions.final
class PackResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ARTIFACT_PATH_FIELD_NUMBER: builtins.int
    artifact_path: builtins.str
    """the full path of the packed artifact."""
    def __init__(
        self,
        *,
        artifact_path: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["artifact_path", b"artifact_path"]) -> None: ...

global___PackResponse = PackResponse
