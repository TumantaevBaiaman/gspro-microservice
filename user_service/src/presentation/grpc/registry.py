from generated.user.user_pb2_grpc import add_UserServiceServicer_to_server
from generated.user.profile_pb2_grpc import add_UserProfileServiceServicer_to_server
from generated.user.user_category_pb2_grpc import add_UserCategoryServiceServicer_to_server
from generated.user.user_experience_pb2_grpc import add_UserExperienceServiceServicer_to_server
from generated.user.user_education_pb2_grpc import add_UserEducationServiceServicer_to_server
from generated.user.user_certificate_pb2_grpc import add_UserCertificateServiceServicer_to_server

from src.presentation.grpc.handlers import (
    UserHandler,
    ProfileHandler,
    UserCategoryHandler,
    UserExperienceHandler,
    UserEducationHandler,
    UserCertificateHandler,
)


GRPC_SERVICES = [
    (add_UserServiceServicer_to_server, "user", UserHandler),
    (add_UserProfileServiceServicer_to_server, "profile", ProfileHandler),
    (add_UserCategoryServiceServicer_to_server, "user_category", UserCategoryHandler),
    (add_UserExperienceServiceServicer_to_server, "user_experience", UserExperienceHandler),
    (add_UserEducationServiceServicer_to_server, "user_education", UserEducationHandler),
    (add_UserCertificateServiceServicer_to_server, "user_certificate", UserCertificateHandler),
]