from dataclasses import dataclass
from typing import Type, Callable

from src.application.services import *

from src.presentation.grpc.handlers import *

from generated.chat.chat_message_pb2_grpc import add_ChatMessageServiceServicer_to_server
from generated.chat.chat_pb2_grpc import add_ChatServiceServicer_to_server


@dataclass(frozen=True)
class GrpcServiceConfig:
    add_to_server: Callable
    handler_cls: type


GRPC_SERVICES = [
    GrpcServiceConfig(
        add_to_server=add_ChatMessageServiceServicer_to_server,
        handler_cls=ChatMessageHandler,
    ),
    GrpcServiceConfig(
        add_to_server=add_ChatServiceServicer_to_server,
        handler_cls=ChatHandler,
    )
]
