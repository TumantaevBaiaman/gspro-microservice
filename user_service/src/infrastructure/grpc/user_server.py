import grpc
from grpc import aio
from concurrent import futures
from generated.user import user_pb2, user_pb2_grpc
from src.core.config import settings
from src.presentation.grpc.handlers.user_handler import UserHandler


async def start_grpc_server():
    server = aio.server()
    user_pb2_grpc.add_UserServiceServicer_to_server(
        UserHandler(),
        server
    )

    server.add_insecure_port(f"{settings.GRPC_HOST}:{settings.GRPC_PORT}")
    print(f"🚀 Async gRPC server running on {settings.GRPC_HOST}:{settings.GRPC_PORT}")

    await server.start()
    await server.wait_for_termination()
