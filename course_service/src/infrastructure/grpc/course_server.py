import grpc
from grpc import aio

from src.core.config import settings
from src.infrastructure.db.mongo.models import init_mongo

from src.core.logging.logger import logger
from src.presentation.grpc.handlers import (
    CourseHandler,
    AdminCategoryHandler,
    AdminCourseHandler,
    AdminModuleHandler,
    AdminLessonHandler,
)
from generated.course.course_pb2_grpc import add_CourseServiceServicer_to_server
from generated.course.admin_category_pb2_grpc import add_AdminCategoryServiceServicer_to_server
from generated.course.admin_course_pb2_grpc import add_AdminCourseServiceServicer_to_server
from generated.course.admin_lesson_pb2_grpc import add_AdminLessonServiceServicer_to_server
from generated.course.admin_module_pb2_grpc import add_AdminModuleServiceServicer_to_server


async def start_grpc_server():
    server = aio.server()

    add_CourseServiceServicer_to_server(
        CourseHandler(),
        server
    )
    add_AdminCategoryServiceServicer_to_server(
        AdminCategoryHandler(),
        server
    )
    add_AdminCourseServiceServicer_to_server(
        AdminCourseHandler(),
        server
    )
    add_AdminModuleServiceServicer_to_server(
        AdminModuleHandler(),
        server
    )
    add_AdminLessonServiceServicer_to_server(
        AdminLessonHandler(),
        server
    )

    server.add_insecure_port(f"{settings.GRPC_HOST}:{settings.GRPC_PORT}")
    logger.info(f"🚀 Course gRPC server starting on {settings.GRPC_HOST}:{settings.GRPC_PORT}")

    await init_mongo()

    await server.start()
    await server.wait_for_termination()
