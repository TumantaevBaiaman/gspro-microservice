import asyncio

from src.infrastructure.grpc.course_server import start_grpc_server

if __name__ == "__main__":
    asyncio.run(start_grpc_server())