# coding=utf-8
# Copyright 2019 The Tensor2Tensor Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# pylint: skip-file
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from tensor2tensor.envs import env_service_pb2 as tensor2tensor_dot_envs_dot_env__service__pb2


class EnvServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Reset = channel.unary_unary(
        '/tensor2tensor.trax.rlax.envs.EnvService/Reset',
        request_serializer=tensor2tensor_dot_envs_dot_env__service__pb2.ResetRequest.SerializeToString,
        response_deserializer=tensor2tensor_dot_envs_dot_env__service__pb2.ResetResponse.FromString,
        )
    self.Step = channel.unary_unary(
        '/tensor2tensor.trax.rlax.envs.EnvService/Step',
        request_serializer=tensor2tensor_dot_envs_dot_env__service__pb2.StepRequest.SerializeToString,
        response_deserializer=tensor2tensor_dot_envs_dot_env__service__pb2.StepResponse.FromString,
        )
    self.Close = channel.unary_unary(
        '/tensor2tensor.trax.rlax.envs.EnvService/Close',
        request_serializer=tensor2tensor_dot_envs_dot_env__service__pb2.CloseRequest.SerializeToString,
        response_deserializer=tensor2tensor_dot_envs_dot_env__service__pb2.CloseResponse.FromString,
        )
    self.Render = channel.unary_unary(
        '/tensor2tensor.trax.rlax.envs.EnvService/Render',
        request_serializer=tensor2tensor_dot_envs_dot_env__service__pb2.RenderRequest.SerializeToString,
        response_deserializer=tensor2tensor_dot_envs_dot_env__service__pb2.RenderResponse.FromString,
        )
    self.GetEnvInfo = channel.unary_unary(
        '/tensor2tensor.trax.rlax.envs.EnvService/GetEnvInfo',
        request_serializer=tensor2tensor_dot_envs_dot_env__service__pb2.EnvInfoRequest.SerializeToString,
        response_deserializer=tensor2tensor_dot_envs_dot_env__service__pb2.EnvInfoResponse.FromString,
        )


class EnvServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Reset(self, request, context):
    """Reset
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Step(self, request, context):
    """Step
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Close(self, request, context):
    """Close
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Render(self, request, context):
    """Render
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetEnvInfo(self, request, context):
    """Observation and Action Space.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_EnvServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Reset': grpc.unary_unary_rpc_method_handler(
          servicer.Reset,
          request_deserializer=tensor2tensor_dot_envs_dot_env__service__pb2.ResetRequest.FromString,
          response_serializer=tensor2tensor_dot_envs_dot_env__service__pb2.ResetResponse.SerializeToString,
      ),
      'Step': grpc.unary_unary_rpc_method_handler(
          servicer.Step,
          request_deserializer=tensor2tensor_dot_envs_dot_env__service__pb2.StepRequest.FromString,
          response_serializer=tensor2tensor_dot_envs_dot_env__service__pb2.StepResponse.SerializeToString,
      ),
      'Close': grpc.unary_unary_rpc_method_handler(
          servicer.Close,
          request_deserializer=tensor2tensor_dot_envs_dot_env__service__pb2.CloseRequest.FromString,
          response_serializer=tensor2tensor_dot_envs_dot_env__service__pb2.CloseResponse.SerializeToString,
      ),
      'Render': grpc.unary_unary_rpc_method_handler(
          servicer.Render,
          request_deserializer=tensor2tensor_dot_envs_dot_env__service__pb2.RenderRequest.FromString,
          response_serializer=tensor2tensor_dot_envs_dot_env__service__pb2.RenderResponse.SerializeToString,
      ),
      'GetEnvInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetEnvInfo,
          request_deserializer=tensor2tensor_dot_envs_dot_env__service__pb2.EnvInfoRequest.FromString,
          response_serializer=tensor2tensor_dot_envs_dot_env__service__pb2.EnvInfoResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'tensor2tensor.trax.rlax.envs.EnvService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))