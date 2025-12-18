import grpc

import generated.user.user_pb2 as pb2
import generated.user.user_pb2_grpc as pb2_grpc

from src.infrastructure.db.session import async_session_maker
from src.presentation.grpc.container import Container
from src.domain.exceptions.user import (
    UserAlreadyExistsError,
    InvalidCredentialsError,
)


class UserHandler(pb2_grpc.UserServiceServicer):

    async def RegisterEmail(self, request, context):
        async with async_session_maker() as session:
            container = Container(session)

            try:
                res = await container.user_service.register_by_email.execute(request)
                await container.uow.commit()
            except UserAlreadyExistsError as e:
                await container.uow.rollback()
                await context.abort(
                    grpc.StatusCode.ALREADY_EXISTS,
                    str(e)
                )

            return pb2.RegisterEmailResponse(
                user_id=str(res.user_id),
                access_token=res.access_token,
                refresh_token=res.refresh_token,
            )

    async def LoginEmail(self, request, context):
        async with async_session_maker() as session:
            container = Container(session)

            try:
                res = await container.user_service.login_by_email.execute(request)
                await container.uow.commit()
            except InvalidCredentialsError as e:
                await container.uow.rollback()
                await context.abort(
                    grpc.StatusCode.INVALID_ARGUMENT,
                    str(e)
                )

            return pb2.LoginEmailResponse(
                user_id=str(res.user_id),
                access_token=res.access_token,
                refresh_token=res.refresh_token,
            )

    async def RefreshToken(self, request, context):
        async with async_session_maker() as session:
            container = Container(session)

            try:
                res = await container.user_service.refresh_tokens.execute(request)
                await container.uow.commit()
            except Exception as e:
                await container.uow.rollback()
                await context.abort(
                    grpc.StatusCode.INVALID_ARGUMENT,
                    str(e)
                )

            return pb2.RefreshTokenResponse(
                access_token=res.access_token,
                refresh_token=res.refresh_token,
            )
