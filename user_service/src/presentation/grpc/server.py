from grpc import aio
from generated.user import (
    user_pb2_grpc,
    profile_pb2_grpc,
    user_category_pb2_grpc,
    user_experience_pb2_grpc,
    user_education_pb2_grpc,
    user_certificate_pb2_grpc,
)

from src.core.config import settings
from src.core.logging import logger
from src.presentation.grpc.handlers.user_handler import UserHandler
from src.presentation.grpc.handlers.profile_handler import ProfileHandler
from src.presentation.grpc.handlers.user_category_handler import UserCategoryHandler
from src.presentation.grpc.handlers.user_experience_handler import UserExperienceHandler
from src.presentation.grpc.handlers.user_education_handler import UserEducationHandler
from src.presentation.grpc.handlers.user_certificate_handler import UserCertificateHandler


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
    user_category_pb2_grpc.add_UserCategoryServiceServicer_to_server(
        UserCategoryHandler(),
        server
    )
    user_experience_pb2_grpc.add_UserExperienceServiceServicer_to_server(
        UserExperienceHandler(),
        server
    )
    user_education_pb2_grpc.add_UserEducationServiceServicer_to_server(
        UserEducationHandler(),
        server
    )
    user_certificate_pb2_grpc.add_UserCertificateServiceServicer_to_server(
        UserCertificateHandler(),
        server
    )

    server.add_insecure_port(f"{settings.GRPC_HOST}:{settings.GRPC_PORT}")
    logger.info(f"🚀 User gRPC server starting on {settings.GRPC_HOST}:{settings.GRPC_PORT}")

    await server.start()
    await server.wait_for_termination()
