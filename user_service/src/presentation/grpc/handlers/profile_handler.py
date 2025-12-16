import grpc

import generated.user.profile_pb2 as pb2
import generated.user.profile_pb2_grpc as pb2_grpc

from src.application.services import ProfileService
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
                phone_number=profile_dto.phone_number or "",
                bio=profile_dto.bio or "",
                city=profile_dto.city or "",
                industry=profile_dto.industry or "",
                experience_level=profile_dto.experience_level or ""
            )

    async def UpdateUserProfile(self, request, context):
        async with async_session_maker() as session:
            repo = ProfileRepository(session)
            service = ProfileService(repo)

            update_data = {
                "full_name": request.full_name,
                "bio": request.bio,
                "city": request.city,
                "industry": request.industry,
                "experience_level": request.experience_level
            }

            profile_dto = await service.update_profile(request.user_id, update_data)
            if profile_dto is None:
                await context.abort(
                    grpc.StatusCode.NOT_FOUND,
                    "Profile not found"
                )

            return pb2.UpdateUserProfileResponse(
                full_name=profile_dto.full_name or "",
                bio=profile_dto.bio or "",
                city=profile_dto.city or "",
                industry=profile_dto.industry or "",
                experience_level=profile_dto.experience_level or ""
            )
