from grpc import aio
from generated.user import user_pb2_grpc, profile_pb2_grpc

from src.core.config import settings
from src.core.logging import logger
from src.presentation.grpc.handlers.user_handler import UserHandler
from src.presentation.grpc.handlers.profile_handler import ProfileHandler


async def start_grpc_server():
    server = aio.server()
    user_pb2_grpc.add_UserServiceServicer_to_server(
        UserHandler(),
        server
    )
    profile_pb2_grpc.add_UserProfileServiceServicer_to_server(
        ProfileHandler(),
        server
    )

    server.add_insecure_port(f"{settings.GRPC_HOST}:{settings.GRPC_PORT}")
    logger.info(f"🚀 User gRPC server starting on {settings.GRPC_HOST}:{settings.GRPC_PORT}")

    await server.start()
    await server.wait_for_termination()
