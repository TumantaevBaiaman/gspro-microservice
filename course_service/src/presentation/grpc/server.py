from grpc import aio

from src.container import build_services
from src.core.config import settings
from src.infrastructure.db.mongo.models import init_mongo
from src.core.logging.logger import logger
from src.presentation.grpc.registry import GRPC_SERVICES


async def start_grpc_server():
    await init_mongo()

    server = aio.server()
    services = build_services()

    for add_func, key, handler_cls in GRPC_SERVICES:
        add_func(handler_cls(services[key]), server)

    server.add_insecure_port(
        f"{settings.GRPC_HOST}:{settings.GRPC_PORT}"
    )

    logger.info("🚀 Course gRPC server started")

    await server.start()
    await server.wait_for_termination()
