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
import abc
import collections.abc
import google.protobuf.empty_pb2
import grpc
import grpc.aio
import typing
import pulumi.language_pb2
import pulumi.plugin_pb2

class LanguageRuntimeStub:
    """The LanguageRuntime service defines a standard interface for [language hosts/runtimes](languages). At a high level, a
    language runtime provides the ability to execute programs, install and query dependencies, and generate code for a
    specific language.
    """

    def __init__(self, channel: grpc.Channel) -> None: ...
    Handshake: grpc.UnaryUnaryMultiCallable[
        pulumi.language_pb2.LanguageHandshakeRequest,
        pulumi.language_pb2.LanguageHandshakeResponse,
    ]
    """`Handshake` is the first call made by the engine to a language host. It is used to pass the engine's address to
    the language host so that it may establish its own connections back, and to establish protocol configuration that
    will be used to communicate between the two parties.
    """
    GetRequiredPlugins: grpc.UnaryUnaryMultiCallable[
        pulumi.language_pb2.GetRequiredPluginsRequest,
        pulumi.language_pb2.GetRequiredPluginsResponse,
    ]
    """`GetRequiredPlugins` computes the complete set of anticipated [plugins](plugins) required by a Pulumi program.
    Among other things, it is intended to be used to pre-install plugins before running a program with
    [](pulumirpc.LanguageRuntime.Run), to avoid the need to install them on-demand in response to [resource
    registrations](resource-registration) sent back from the running program to the engine.

    :::{important}
    The use of `GetRequiredPlugins` is deprecated in favour of [](pulumirpc.LanguageRuntime.GetRequiredPackages),
    which returns more granular information about which plugins are required by which packages.
    :::
    """
    GetRequiredPackages: grpc.UnaryUnaryMultiCallable[
        pulumi.language_pb2.GetRequiredPackagesRequest,
        pulumi.language_pb2.GetRequiredPackagesResponse,
    ]
    """`GetRequiredPackages` computes the complete set of anticipated [packages](pulumirpc.PackageDependency) required
    by a program. It is used to pre-install packages before running a program with [](pulumirpc.LanguageRuntime.Run),
    to avoid the need to install them on-demand in response to [resource registrations](resource-registration) sent
    back from the running program to the engine. Moreover, when importing resources into a stack, it is used to
    determine which plugins are required to service the import of a given resource, since given the presence of
    [parameterized providers](parameterized-providers), it is not in general true that a package name corresponds 1:1
    with a plugin name. It replaces [](pulumirpc.LanguageRuntime.GetRequiredPlugins) in the face of [parameterized
    providers](parameterized-providers), which as mentioned above can enable multiple instances of the same plugin to
    provide multiple packages.
    """
    Run: grpc.UnaryUnaryMultiCallable[
        pulumi.language_pb2.RunRequest,
        pulumi.language_pb2.RunResponse,
    ]
    """`Run` executes a Pulumi program, returning information about whether or not the program produced an error."""
    GetPluginInfo: grpc.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        pulumi.plugin_pb2.PluginInfo,
    ]
    """`GetPluginInfo` returns information about the [plugin](plugins) implementing this language runtime."""
    InstallDependencies: grpc.UnaryStreamMultiCallable[
        pulumi.language_pb2.InstallDependenciesRequest,
        pulumi.language_pb2.InstallDependenciesResponse,
    ]
    """`InstallDependencies` accepts a request specifying a Pulumi project and program that can be executed with
    [](pulumirpc.LanguageRuntime.Run) and installs the dependencies for that program (e.g. by running `npm install`
    for NodeJS, or `pip install` for Python). Since dependency installation could take a while, and callers may wish
    to report on its progress, this method returns a stream of [](pulumirpc.InstallDependenciesResponse) messages
    containing information about standard error and output.
    """
    RuntimeOptionsPrompts: grpc.UnaryUnaryMultiCallable[
        pulumi.language_pb2.RuntimeOptionsRequest,
        pulumi.language_pb2.RuntimeOptionsResponse,
    ]
    """`RuntimeOptionsPrompts` accepts a request specifying a Pulumi project and returns a list of additional prompts to
    ask during `pulumi new`.
    """
    About: grpc.UnaryUnaryMultiCallable[
        pulumi.language_pb2.AboutRequest,
        pulumi.language_pb2.AboutResponse,
    ]
    """`About` returns information about the language runtime being used."""
    GetProgramDependencies: grpc.UnaryUnaryMultiCallable[
        pulumi.language_pb2.GetProgramDependenciesRequest,
        pulumi.language_pb2.GetProgramDependenciesResponse,
    ]
    """`GetProgramDependencies` computes the set of language-level dependencies (e.g. NPM packages for NodeJS, or Maven
    libraries for Java) required by a program.
    """
    RunPlugin: grpc.UnaryStreamMultiCallable[
        pulumi.language_pb2.RunPluginRequest,
        pulumi.language_pb2.RunPluginResponse,
    ]
    """`RunPlugin` is used to execute a program written in this host's language that implements a Pulumi
    [plugin](plugins). It it is plugins what [](pulumirpc.LanguageRuntime.Run) is to programs. Since a plugin is not
    expected to terminate until instructed/for a long time, this method returns a stream of
    [](pulumirpc.RunPluginResponse) messages containing information about standard error and output, as well as the
    exit code of the plugin when it does terminate.
    """
    GenerateProgram: grpc.UnaryUnaryMultiCallable[
        pulumi.language_pb2.GenerateProgramRequest,
        pulumi.language_pb2.GenerateProgramResponse,
    ]
    """`GenerateProgram` generates code in this host's language that implements the given [PCL](pcl) program. Unlike
    [](pulumirpc.LanguageRuntime.GenerateProject), this method *only* generates program code, and does not e.g.
    generate a `package.json` for a NodeJS project that details how to run that code.
    [](pulumirpc.LanguageRuntime.GenerateProject), this method underpins ["programgen"](programgen) and the main
    functionality powering `pulumi convert`.
    """
    GenerateProject: grpc.UnaryUnaryMultiCallable[
        pulumi.language_pb2.GenerateProjectRequest,
        pulumi.language_pb2.GenerateProjectResponse,
    ]
    """`GenerateProject` generates code in this host's language that implements the given [PCL](pcl) program and wraps
    it in some language-specific notion of a "project", where a project is a buildable or runnable artifact. In this
    sense, `GenerateProject`'s output is a superset of that of [](pulumirpc.LanguageRuntime.GenerateProgram). For
    instance, when generating a NodeJS project, this method might generate a corresponding `package.json` file, as
    well as the relevant NodeJS program code. Along with [](pulumirpc.LanguageRuntime.GenerateProgram), this method
    underpins ["programgen"](programgen) and the main functionality powering `pulumi convert`.
    """
    GeneratePackage: grpc.UnaryUnaryMultiCallable[
        pulumi.language_pb2.GeneratePackageRequest,
        pulumi.language_pb2.GeneratePackageResponse,
    ]
    """`GeneratePackage` generates code in this host's language that implements an [SDK](sdkgen) ("sdkgen") for the
    given Pulumi package, as specified by a [schema](schema).
    """
    Pack: grpc.UnaryUnaryMultiCallable[
        pulumi.language_pb2.PackRequest,
        pulumi.language_pb2.PackResponse,
    ]
    """`Pack` accepts a request specifying a generated SDK package and packs it into a language-specific artifact. For
    instance, in the case of Java, it might produce a JAR file from a list of `.java` sources; in the case of NodeJS,
    a `.tgz` file might be produced from a list of `.js` sources; and so on. Presently, `Pack` is primarily used in
    [language conformance tests](language-conformance-tests), though it is intended to be used more widely in future
    to standardise e.g. provider publishing workflows.
    """

class LanguageRuntimeServicer(metaclass=abc.ABCMeta):
    """The LanguageRuntime service defines a standard interface for [language hosts/runtimes](languages). At a high level, a
    language runtime provides the ability to execute programs, install and query dependencies, and generate code for a
    specific language.
    """

    
    def Handshake(
        self,
        request: pulumi.language_pb2.LanguageHandshakeRequest,
        context: grpc.ServicerContext,
    ) -> pulumi.language_pb2.LanguageHandshakeResponse:
        """`Handshake` is the first call made by the engine to a language host. It is used to pass the engine's address to
        the language host so that it may establish its own connections back, and to establish protocol configuration that
        will be used to communicate between the two parties.
        """
    
    def GetRequiredPlugins(
        self,
        request: pulumi.language_pb2.GetRequiredPluginsRequest,
        context: grpc.ServicerContext,
    ) -> pulumi.language_pb2.GetRequiredPluginsResponse:
        """`GetRequiredPlugins` computes the complete set of anticipated [plugins](plugins) required by a Pulumi program.
        Among other things, it is intended to be used to pre-install plugins before running a program with
        [](pulumirpc.LanguageRuntime.Run), to avoid the need to install them on-demand in response to [resource
        registrations](resource-registration) sent back from the running program to the engine.

        :::{important}
        The use of `GetRequiredPlugins` is deprecated in favour of [](pulumirpc.LanguageRuntime.GetRequiredPackages),
        which returns more granular information about which plugins are required by which packages.
        :::
        """
    
    def GetRequiredPackages(
        self,
        request: pulumi.language_pb2.GetRequiredPackagesRequest,
        context: grpc.ServicerContext,
    ) -> pulumi.language_pb2.GetRequiredPackagesResponse:
        """`GetRequiredPackages` computes the complete set of anticipated [packages](pulumirpc.PackageDependency) required
        by a program. It is used to pre-install packages before running a program with [](pulumirpc.LanguageRuntime.Run),
        to avoid the need to install them on-demand in response to [resource registrations](resource-registration) sent
        back from the running program to the engine. Moreover, when importing resources into a stack, it is used to
        determine which plugins are required to service the import of a given resource, since given the presence of
        [parameterized providers](parameterized-providers), it is not in general true that a package name corresponds 1:1
        with a plugin name. It replaces [](pulumirpc.LanguageRuntime.GetRequiredPlugins) in the face of [parameterized
        providers](parameterized-providers), which as mentioned above can enable multiple instances of the same plugin to
        provide multiple packages.
        """
    
    def Run(
        self,
        request: pulumi.language_pb2.RunRequest,
        context: grpc.ServicerContext,
    ) -> pulumi.language_pb2.RunResponse:
        """`Run` executes a Pulumi program, returning information about whether or not the program produced an error."""
    
    def GetPluginInfo(
        self,
        request: google.protobuf.empty_pb2.Empty,
        context: grpc.ServicerContext,
    ) -> pulumi.plugin_pb2.PluginInfo:
        """`GetPluginInfo` returns information about the [plugin](plugins) implementing this language runtime."""
    
    def InstallDependencies(
        self,
        request: pulumi.language_pb2.InstallDependenciesRequest,
        context: grpc.ServicerContext,
    ) -> collections.abc.Iterator[pulumi.language_pb2.InstallDependenciesResponse]:
        """`InstallDependencies` accepts a request specifying a Pulumi project and program that can be executed with
        [](pulumirpc.LanguageRuntime.Run) and installs the dependencies for that program (e.g. by running `npm install`
        for NodeJS, or `pip install` for Python). Since dependency installation could take a while, and callers may wish
        to report on its progress, this method returns a stream of [](pulumirpc.InstallDependenciesResponse) messages
        containing information about standard error and output.
        """
    
    def RuntimeOptionsPrompts(
        self,
        request: pulumi.language_pb2.RuntimeOptionsRequest,
        context: grpc.ServicerContext,
    ) -> pulumi.language_pb2.RuntimeOptionsResponse:
        """`RuntimeOptionsPrompts` accepts a request specifying a Pulumi project and returns a list of additional prompts to
        ask during `pulumi new`.
        """
    
    def About(
        self,
        request: pulumi.language_pb2.AboutRequest,
        context: grpc.ServicerContext,
    ) -> pulumi.language_pb2.AboutResponse:
        """`About` returns information about the language runtime being used."""
    
    def GetProgramDependencies(
        self,
        request: pulumi.language_pb2.GetProgramDependenciesRequest,
        context: grpc.ServicerContext,
    ) -> pulumi.language_pb2.GetProgramDependenciesResponse:
        """`GetProgramDependencies` computes the set of language-level dependencies (e.g. NPM packages for NodeJS, or Maven
        libraries for Java) required by a program.
        """
    
    def RunPlugin(
        self,
        request: pulumi.language_pb2.RunPluginRequest,
        context: grpc.ServicerContext,
    ) -> collections.abc.Iterator[pulumi.language_pb2.RunPluginResponse]:
        """`RunPlugin` is used to execute a program written in this host's language that implements a Pulumi
        [plugin](plugins). It it is plugins what [](pulumirpc.LanguageRuntime.Run) is to programs. Since a plugin is not
        expected to terminate until instructed/for a long time, this method returns a stream of
        [](pulumirpc.RunPluginResponse) messages containing information about standard error and output, as well as the
        exit code of the plugin when it does terminate.
        """
    
    def GenerateProgram(
        self,
        request: pulumi.language_pb2.GenerateProgramRequest,
        context: grpc.ServicerContext,
    ) -> pulumi.language_pb2.GenerateProgramResponse:
        """`GenerateProgram` generates code in this host's language that implements the given [PCL](pcl) program. Unlike
        [](pulumirpc.LanguageRuntime.GenerateProject), this method *only* generates program code, and does not e.g.
        generate a `package.json` for a NodeJS project that details how to run that code.
        [](pulumirpc.LanguageRuntime.GenerateProject), this method underpins ["programgen"](programgen) and the main
        functionality powering `pulumi convert`.
        """
    
    def GenerateProject(
        self,
        request: pulumi.language_pb2.GenerateProjectRequest,
        context: grpc.ServicerContext,
    ) -> pulumi.language_pb2.GenerateProjectResponse:
        """`GenerateProject` generates code in this host's language that implements the given [PCL](pcl) program and wraps
        it in some language-specific notion of a "project", where a project is a buildable or runnable artifact. In this
        sense, `GenerateProject`'s output is a superset of that of [](pulumirpc.LanguageRuntime.GenerateProgram). For
        instance, when generating a NodeJS project, this method might generate a corresponding `package.json` file, as
        well as the relevant NodeJS program code. Along with [](pulumirpc.LanguageRuntime.GenerateProgram), this method
        underpins ["programgen"](programgen) and the main functionality powering `pulumi convert`.
        """
    
    def GeneratePackage(
        self,
        request: pulumi.language_pb2.GeneratePackageRequest,
        context: grpc.ServicerContext,
    ) -> pulumi.language_pb2.GeneratePackageResponse:
        """`GeneratePackage` generates code in this host's language that implements an [SDK](sdkgen) ("sdkgen") for the
        given Pulumi package, as specified by a [schema](schema).
        """
    
    def Pack(
        self,
        request: pulumi.language_pb2.PackRequest,
        context: grpc.ServicerContext,
    ) -> pulumi.language_pb2.PackResponse:
        """`Pack` accepts a request specifying a generated SDK package and packs it into a language-specific artifact. For
        instance, in the case of Java, it might produce a JAR file from a list of `.java` sources; in the case of NodeJS,
        a `.tgz` file might be produced from a list of `.js` sources; and so on. Presently, `Pack` is primarily used in
        [language conformance tests](language-conformance-tests), though it is intended to be used more widely in future
        to standardise e.g. provider publishing workflows.
        """

def add_LanguageRuntimeServicer_to_server(servicer: LanguageRuntimeServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
