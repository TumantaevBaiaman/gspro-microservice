import grpc

import generated.user.profile_pb2 as pb2
import generated.user.profile_pb2_grpc as pb2_grpc

from src.infrastructure.db.session import async_session_maker
from src.presentation.grpc.container import Container
from src.domain.exceptions.profile import ProfileNotFoundError


class ProfileHandler(pb2_grpc.UserProfileServiceServicer):

    async def GetUserProfile(self, request, context):
        async with async_session_maker() as session:
            container = Container(session)

            try:
                profile = await container.profile_service.get_profile_by_user_id.execute(
                    request
                )
            except ProfileNotFoundError as e:
                await context.abort(
                    grpc.StatusCode.NOT_FOUND,
                )

            return pb2.GetUserProfileResponse(
                full_name=profile.full_name or "",
                phone_number=profile.phone_number or "",
                bio=profile.bio or "",
                city=profile.city or "",
                industry=profile.industry or "",
                experience_level=profile.experience_level or "",
            )

    async def UpdateUserProfile(self, request, context):
        async with async_session_maker() as session:
            container = Container(session)

            try:
                profile = await container.profile_service.update_profile.execute(
                    user_id=request.user_id,
                    data={
                        "full_name": request.full_name,
                        "bio": request.bio,
                        "city": request.city,
                        "industry": request.industry,
                        "experience_level": request.experience_level,
                    },
                )
                await container.uow.commit()
            except ProfileNotFoundError as e:
                await container.uow.rollback()
                await context.abort(
                    grpc.StatusCode.NOT_FOUND,
                    str(e)
                )

            return pb2.UpdateUserProfileResponse(
                full_name=profile.full_name or "",
                bio=profile.bio or "",
                city=profile.city or "",
                industry=profile.industry or "",
                experience_level=profile.experience_level or "",
            )
