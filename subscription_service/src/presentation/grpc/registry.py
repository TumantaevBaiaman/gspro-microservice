from dataclasses import dataclass
from typing import Type, Callable

from src.application.services import *

from src.presentation.grpc.handlers import *

from generated.subscription.course_access_pb2_grpc import add_CourseAccessServiceServicer_to_server
from generated.subscription.purchase_request_pb2_grpc import add_PurchaseRequestServiceServicer_to_server


@dataclass(frozen=True)
class GrpcServiceConfig:
    add_to_server: Callable
    service_cls: Type
    handler_cls: Type


GRPC_SERVICES: list[GrpcServiceConfig] = [
    GrpcServiceConfig(
        add_to_server=add_PurchaseRequestServiceServicer_to_server,
        service_cls=PurchaseRequestService,
        handler_cls=PurchaseRequestHandler
    ),
    GrpcServiceConfig(
        add_to_server=add_CourseAccessServiceServicer_to_server,
        service_cls=CourseAccessService,
        handler_cls=CourseAccessHandler
    )
]
