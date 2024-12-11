# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import language_pb2 as pulumi_dot_language__pb2
from . import plugin_pb2 as pulumi_dot_plugin__pb2


class LanguageRuntimeStub(object):
    """LanguageRuntime is the interface that the planning monitor uses to drive execution of an interpreter responsible
    for confguring and creating resource objects.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Handshake = channel.unary_unary(
                '/pulumirpc.LanguageRuntime/Handshake',
                request_serializer=pulumi_dot_language__pb2.LanguageHandshakeRequest.SerializeToString,
                response_deserializer=pulumi_dot_language__pb2.LanguageHandshakeResponse.FromString,
                )
        self.GetRequiredPlugins = channel.unary_unary(
                '/pulumirpc.LanguageRuntime/GetRequiredPlugins',
                request_serializer=pulumi_dot_language__pb2.GetRequiredPluginsRequest.SerializeToString,
                response_deserializer=pulumi_dot_language__pb2.GetRequiredPluginsResponse.FromString,
                )
        self.GetRequiredPackages = channel.unary_unary(
                '/pulumirpc.LanguageRuntime/GetRequiredPackages',
                request_serializer=pulumi_dot_language__pb2.GetRequiredPackagesRequest.SerializeToString,
                response_deserializer=pulumi_dot_language__pb2.GetRequiredPackagesResponse.FromString,
                )
        self.Run = channel.unary_unary(
                '/pulumirpc.LanguageRuntime/Run',
                request_serializer=pulumi_dot_language__pb2.RunRequest.SerializeToString,
                response_deserializer=pulumi_dot_language__pb2.RunResponse.FromString,
                )
        self.GetPluginInfo = channel.unary_unary(
                '/pulumirpc.LanguageRuntime/GetPluginInfo',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=pulumi_dot_plugin__pb2.PluginInfo.FromString,
                )
        self.InstallDependencies = channel.unary_stream(
                '/pulumirpc.LanguageRuntime/InstallDependencies',
                request_serializer=pulumi_dot_language__pb2.InstallDependenciesRequest.SerializeToString,
                response_deserializer=pulumi_dot_language__pb2.InstallDependenciesResponse.FromString,
                )
        self.RuntimeOptionsPrompts = channel.unary_unary(
                '/pulumirpc.LanguageRuntime/RuntimeOptionsPrompts',
                request_serializer=pulumi_dot_language__pb2.RuntimeOptionsRequest.SerializeToString,
                response_deserializer=pulumi_dot_language__pb2.RuntimeOptionsResponse.FromString,
                )
        self.About = channel.unary_unary(
                '/pulumirpc.LanguageRuntime/About',
                request_serializer=pulumi_dot_language__pb2.AboutRequest.SerializeToString,
                response_deserializer=pulumi_dot_language__pb2.AboutResponse.FromString,
                )
        self.GetProgramDependencies = channel.unary_unary(
                '/pulumirpc.LanguageRuntime/GetProgramDependencies',
                request_serializer=pulumi_dot_language__pb2.GetProgramDependenciesRequest.SerializeToString,
                response_deserializer=pulumi_dot_language__pb2.GetProgramDependenciesResponse.FromString,
                )
        self.RunPlugin = channel.unary_stream(
                '/pulumirpc.LanguageRuntime/RunPlugin',
                request_serializer=pulumi_dot_language__pb2.RunPluginRequest.SerializeToString,
                response_deserializer=pulumi_dot_language__pb2.RunPluginResponse.FromString,
                )
        self.GenerateProgram = channel.unary_unary(
                '/pulumirpc.LanguageRuntime/GenerateProgram',
                request_serializer=pulumi_dot_language__pb2.GenerateProgramRequest.SerializeToString,
                response_deserializer=pulumi_dot_language__pb2.GenerateProgramResponse.FromString,
                )
        self.GenerateProject = channel.unary_unary(
                '/pulumirpc.LanguageRuntime/GenerateProject',
                request_serializer=pulumi_dot_language__pb2.GenerateProjectRequest.SerializeToString,
                response_deserializer=pulumi_dot_language__pb2.GenerateProjectResponse.FromString,
                )
        self.GeneratePackage = channel.unary_unary(
                '/pulumirpc.LanguageRuntime/GeneratePackage',
                request_serializer=pulumi_dot_language__pb2.GeneratePackageRequest.SerializeToString,
                response_deserializer=pulumi_dot_language__pb2.GeneratePackageResponse.FromString,
                )
        self.Pack = channel.unary_unary(
                '/pulumirpc.LanguageRuntime/Pack',
                request_serializer=pulumi_dot_language__pb2.PackRequest.SerializeToString,
                response_deserializer=pulumi_dot_language__pb2.PackResponse.FromString,
                )


class LanguageRuntimeServicer(object):
    """LanguageRuntime is the interface that the planning monitor uses to drive execution of an interpreter responsible
    for confguring and creating resource objects.
    """

    def Handshake(self, request, context):
        """`Handshake` is the first call made by the engine to a language host. It is used to pass the 
        engine's address to the language host so that it may establish its own connections back,
        and to establish protocol configuration that will be used to communicate between the two parties. 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRequiredPlugins(self, request, context):
        """GetRequiredPlugins computes the complete set of anticipated plugins required by a program.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRequiredPackages(self, request, context):
        """GetRequiredPackages computes the complete set of anticipated packages required by a program.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Run(self, request, context):
        """Run executes a program and returns its result.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPluginInfo(self, request, context):
        """GetPluginInfo returns generic information about this plugin, like its version.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InstallDependencies(self, request, context):
        """InstallDependencies will install dependencies for the project, e.g. by running `npm install` for nodejs projects.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RuntimeOptionsPrompts(self, request, context):
        """RuntimeOptionsPrompts returns a list of additional prompts to ask during `pulumi new`.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def About(self, request, context):
        """About returns information about the runtime for this language.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProgramDependencies(self, request, context):
        """GetProgramDependencies returns the set of dependencies required by the program.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RunPlugin(self, request, context):
        """RunPlugin executes a plugin program and returns its result asynchronously.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GenerateProgram(self, request, context):
        """GenerateProgram generates a given PCL program into a program for this language.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GenerateProject(self, request, context):
        """GenerateProject generates a given PCL program into a project for this language.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GeneratePackage(self, request, context):
        """GeneratePackage generates a given pulumi package into a package for this language.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Pack(self, request, context):
        """Pack packs a package into a language specific artifact.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LanguageRuntimeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Handshake': grpc.unary_unary_rpc_method_handler(
                    servicer.Handshake,
                    request_deserializer=pulumi_dot_language__pb2.LanguageHandshakeRequest.FromString,
                    response_serializer=pulumi_dot_language__pb2.LanguageHandshakeResponse.SerializeToString,
            ),
            'GetRequiredPlugins': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRequiredPlugins,
                    request_deserializer=pulumi_dot_language__pb2.GetRequiredPluginsRequest.FromString,
                    response_serializer=pulumi_dot_language__pb2.GetRequiredPluginsResponse.SerializeToString,
            ),
            'GetRequiredPackages': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRequiredPackages,
                    request_deserializer=pulumi_dot_language__pb2.GetRequiredPackagesRequest.FromString,
                    response_serializer=pulumi_dot_language__pb2.GetRequiredPackagesResponse.SerializeToString,
            ),
            'Run': grpc.unary_unary_rpc_method_handler(
                    servicer.Run,
                    request_deserializer=pulumi_dot_language__pb2.RunRequest.FromString,
                    response_serializer=pulumi_dot_language__pb2.RunResponse.SerializeToString,
            ),
            'GetPluginInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPluginInfo,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=pulumi_dot_plugin__pb2.PluginInfo.SerializeToString,
            ),
            'InstallDependencies': grpc.unary_stream_rpc_method_handler(
                    servicer.InstallDependencies,
                    request_deserializer=pulumi_dot_language__pb2.InstallDependenciesRequest.FromString,
                    response_serializer=pulumi_dot_language__pb2.InstallDependenciesResponse.SerializeToString,
            ),
            'RuntimeOptionsPrompts': grpc.unary_unary_rpc_method_handler(
                    servicer.RuntimeOptionsPrompts,
                    request_deserializer=pulumi_dot_language__pb2.RuntimeOptionsRequest.FromString,
                    response_serializer=pulumi_dot_language__pb2.RuntimeOptionsResponse.SerializeToString,
            ),
            'About': grpc.unary_unary_rpc_method_handler(
                    servicer.About,
                    request_deserializer=pulumi_dot_language__pb2.AboutRequest.FromString,
                    response_serializer=pulumi_dot_language__pb2.AboutResponse.SerializeToString,
            ),
            'GetProgramDependencies': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProgramDependencies,
                    request_deserializer=pulumi_dot_language__pb2.GetProgramDependenciesRequest.FromString,
                    response_serializer=pulumi_dot_language__pb2.GetProgramDependenciesResponse.SerializeToString,
            ),
            'RunPlugin': grpc.unary_stream_rpc_method_handler(
                    servicer.RunPlugin,
                    request_deserializer=pulumi_dot_language__pb2.RunPluginRequest.FromString,
                    response_serializer=pulumi_dot_language__pb2.RunPluginResponse.SerializeToString,
            ),
            'GenerateProgram': grpc.unary_unary_rpc_method_handler(
                    servicer.GenerateProgram,
                    request_deserializer=pulumi_dot_language__pb2.GenerateProgramRequest.FromString,
                    response_serializer=pulumi_dot_language__pb2.GenerateProgramResponse.SerializeToString,
            ),
            'GenerateProject': grpc.unary_unary_rpc_method_handler(
                    servicer.GenerateProject,
                    request_deserializer=pulumi_dot_language__pb2.GenerateProjectRequest.FromString,
                    response_serializer=pulumi_dot_language__pb2.GenerateProjectResponse.SerializeToString,
            ),
            'GeneratePackage': grpc.unary_unary_rpc_method_handler(
                    servicer.GeneratePackage,
                    request_deserializer=pulumi_dot_language__pb2.GeneratePackageRequest.FromString,
                    response_serializer=pulumi_dot_language__pb2.GeneratePackageResponse.SerializeToString,
            ),
            'Pack': grpc.unary_unary_rpc_method_handler(
                    servicer.Pack,
                    request_deserializer=pulumi_dot_language__pb2.PackRequest.FromString,
                    response_serializer=pulumi_dot_language__pb2.PackResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pulumirpc.LanguageRuntime', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class LanguageRuntime(object):
    """LanguageRuntime is the interface that the planning monitor uses to drive execution of an interpreter responsible
    for confguring and creating resource objects.
    """

    @staticmethod
    def Handshake(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pulumirpc.LanguageRuntime/Handshake',
            pulumi_dot_language__pb2.LanguageHandshakeRequest.SerializeToString,
            pulumi_dot_language__pb2.LanguageHandshakeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRequiredPlugins(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pulumirpc.LanguageRuntime/GetRequiredPlugins',
            pulumi_dot_language__pb2.GetRequiredPluginsRequest.SerializeToString,
            pulumi_dot_language__pb2.GetRequiredPluginsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRequiredPackages(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pulumirpc.LanguageRuntime/GetRequiredPackages',
            pulumi_dot_language__pb2.GetRequiredPackagesRequest.SerializeToString,
            pulumi_dot_language__pb2.GetRequiredPackagesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Run(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pulumirpc.LanguageRuntime/Run',
            pulumi_dot_language__pb2.RunRequest.SerializeToString,
            pulumi_dot_language__pb2.RunResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPluginInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pulumirpc.LanguageRuntime/GetPluginInfo',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            pulumi_dot_plugin__pb2.PluginInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InstallDependencies(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/pulumirpc.LanguageRuntime/InstallDependencies',
            pulumi_dot_language__pb2.InstallDependenciesRequest.SerializeToString,
            pulumi_dot_language__pb2.InstallDependenciesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RuntimeOptionsPrompts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pulumirpc.LanguageRuntime/RuntimeOptionsPrompts',
            pulumi_dot_language__pb2.RuntimeOptionsRequest.SerializeToString,
            pulumi_dot_language__pb2.RuntimeOptionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def About(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pulumirpc.LanguageRuntime/About',
            pulumi_dot_language__pb2.AboutRequest.SerializeToString,
            pulumi_dot_language__pb2.AboutResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProgramDependencies(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pulumirpc.LanguageRuntime/GetProgramDependencies',
            pulumi_dot_language__pb2.GetProgramDependenciesRequest.SerializeToString,
            pulumi_dot_language__pb2.GetProgramDependenciesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RunPlugin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/pulumirpc.LanguageRuntime/RunPlugin',
            pulumi_dot_language__pb2.RunPluginRequest.SerializeToString,
            pulumi_dot_language__pb2.RunPluginResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GenerateProgram(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pulumirpc.LanguageRuntime/GenerateProgram',
            pulumi_dot_language__pb2.GenerateProgramRequest.SerializeToString,
            pulumi_dot_language__pb2.GenerateProgramResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GenerateProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pulumirpc.LanguageRuntime/GenerateProject',
            pulumi_dot_language__pb2.GenerateProjectRequest.SerializeToString,
            pulumi_dot_language__pb2.GenerateProjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GeneratePackage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pulumirpc.LanguageRuntime/GeneratePackage',
            pulumi_dot_language__pb2.GeneratePackageRequest.SerializeToString,
            pulumi_dot_language__pb2.GeneratePackageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Pack(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pulumirpc.LanguageRuntime/Pack',
            pulumi_dot_language__pb2.PackRequest.SerializeToString,
            pulumi_dot_language__pb2.PackResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
