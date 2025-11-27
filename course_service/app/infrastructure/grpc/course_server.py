import grpc
from grpc import aio

from app.core.config import settings
from app.infrastructure.db.mongo.models import init_mongo

from app.presentation.grpc.handlers.course_handler import CourseHandler
from generated.course.course_pb2_grpc import add_CourseServiceServicer_to_server


async def start_grpc_server():
    server = aio.server()

    add_CourseServiceServicer_to_server(
        CourseHandler(),
        server
    )

    server.add_insecure_port(f"{settings.GRPC_HOST}:{settings.GRPC_PORT}")
    print(f"🚀 Course gRPC server starting on {settings.GRPC_HOST}:{settings.GRPC_PORT}")

    await init_mongo()

    await server.start()
    await server.wait_for_termination()
