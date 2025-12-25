from dataclasses import dataclass
from typing import Type, Callable

from src.application.services import *

from src.presentation.grpc.handlers import *

from generated.favorites.course_favorites_pb2_grpc import add_FavoriteCourseServiceServicer_to_server


@dataclass(frozen=True)
class GrpcServiceConfig:
    add_to_server: Callable
    service_cls: Type
    handler_cls: Type


GRPC_SERVICES: list[GrpcServiceConfig] = [
    GrpcServiceConfig(
        add_to_server=add_FavoriteCourseServiceServicer_to_server,
        service_cls=FavoriteCourseService,
        handler_cls=FavoriteCourseHandler,
    ),
]
