from generated.user.user_pb2_grpc import add_UserServiceServicer_to_server
from generated.user.profile_pb2_grpc import add_UserProfileServiceServicer_to_server

from src.presentation.grpc.handlers import (
    UserHandler,
    ProfileHandler
)


GRPC_SERVICES = [
    (add_UserServiceServicer_to_server, "user", UserHandler),
    (add_UserProfileServiceServicer_to_server, "profile", ProfileHandler)
]