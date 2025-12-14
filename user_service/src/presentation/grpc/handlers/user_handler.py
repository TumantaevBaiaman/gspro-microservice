import grpc

import generated.user.user_pb2 as pb2
import generated.user.user_pb2_grpc as pb2_grpc

from src.application.services import UserService
from src.infrastructure.db.session import async_session_maker
from src.infrastructure.db.repositories.user_repository import UserRepository


class UserHandler(pb2_grpc.UserServiceServicer):

    async def RegisterEmail(self, request, context):
        async with async_session_maker() as session:
            repo = UserRepository(session)
            service = UserService(repo)

            try:
                res = await service.register_by_email(request)
            except ValueError as e:
                await context.abort(
                    grpc.StatusCode.ALREADY_EXISTS,
                    str(e)
                )

            return pb2.RegisterEmailResponse(
                user_id=str(res.user_id),
                access_token=str(res.access_token),
                refresh_token=str(res.refresh_token)
            )

    async def LoginEmail(self, request,  context):
        async with async_session_maker() as session:
            repo = UserRepository(session)
            service = UserService(repo)

            try:
                res = await service.login_by_email(request)
            except ValueError as e:
                await context.abort(
                    grpc.StatusCode.INVALID_ARGUMENT,
                    str(e)
                )

            return pb2.LoginEmailResponse(
                user_id=str(res.user_id),
                access_token=str(res.access_token),
                refresh_token=str(res.refresh_token)
            )

    async def RefreshToken(self, request, context):
        async with async_session_maker() as session:
            repo = UserRepository(session)
            service = UserService(repo)

            try:
                res = await service.refresh_tokens(request)
            except ValueError as e:
                await context.abort(
                    grpc.StatusCode.INVALID_ARGUMENT,
                    str(e)
                )

            return pb2.RefreshTokenResponse(
                access_token=str(res.access_token),
                refresh_token=str(res.refresh_token)
            )
