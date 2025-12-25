from grpc import aio

from src.presentation.grpc.registry import GRPC_SERVICES
from src.presentation.grpc.container import build_services
from src.presentation.grpc.interceptors.logging_interceptor import LoggingInterceptor
from src.infrastructure.db.mongo.init import init_mongo
from src.core.config import settings
from src.core.logging.logger import logger


async def start_grpc_server():
    await init_mongo()

    server = aio.server(
        interceptors=[LoggingInterceptor()]
    )

    services = build_services()

    for cfg in GRPC_SERVICES:
        service = services[cfg.service_cls]
        handler = cfg.handler_cls(service)
        cfg.add_to_server(handler, server)

    server.add_insecure_port(
        f"{settings.GRPC_HOST}:{settings.GRPC_PORT}"
    )

    logger.info("🚀 Course gRPC server started")

    await server.start()
    await server.wait_for_termination()