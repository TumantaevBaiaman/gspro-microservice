import grpc

import generated.user.profile_pb2 as pb2
import generated.user.profile_pb2_grpc as pb2_grpc

from src.application.services.profile_service import ProfileService
from src.infrastructure.db.session import async_session_maker
from src.infrastructure.db.repositories.profile_repository import ProfileRepository


class ProfileHandler(pb2_grpc.UserProfileServiceServicer):

    async def GetUserProfile(self, request, context):
        async with async_session_maker() as session:
            repo = ProfileRepository(session)
            service = ProfileService(repo)

            profile_dto = await service.get_profile_by_user_id(request)
            if profile_dto is None:
                await context.abort(
                    grpc.StatusCode.NOT_FOUND,
                    "Profile not found"
                )

            return pb2.GetUserProfileResponse(
                full_name=profile_dto.full_name or "",
                bio=profile_dto.bio or "",
                city=profile_dto.city or "",
                industry=profile_dto.industry or "",
                experience_level=profile_dto.experience_level or ""
            )
