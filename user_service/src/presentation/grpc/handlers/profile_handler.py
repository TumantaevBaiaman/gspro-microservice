from datetime import date
from uuid import UUID

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
                email=profile.email,
                full_name=profile.full_name or "",
                phone_number=profile.phone_number or "",
                bio=profile.bio or "",
                date_of_birth=profile.date_of_birth or "",
                city=profile.city or "",
                industry=profile.industry or "",
                experience_level=profile.experience_level or "",
                avatar=pb2.UserAvatar(
                    original_url=profile.avatar.original_url,
                    thumb_small_url=profile.avatar.thumb_small_url or "",
                    thumb_medium_url=profile.avatar.thumb_medium_url or "",
                ) if profile.avatar else None,
            )

    async def UpdateUserProfile(self, request, context):
        async with async_session_maker() as session:
            container = Container(session)
            try:
                await container.profile_service.update_profile.execute(
                    user_id=request.user_id,
                    update_data={
                        "full_name": request.full_name,
                        "bio": request.bio,
                        "date_of_birth": date.fromisoformat(request.date_of_birth) if request.date_of_birth else None,
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
                success=True
            )

    async def ListUserProfiles(self, request, context):
        async with async_session_maker() as session:
            container = Container(session)

            response_dto = await container.profile_service.list_profiles.execute(request)

            items = [
                pb2.UserProfileItem(
                    user_id=item.user_id,
                    full_name=item.full_name or "",
                    phone_number=item.phone_number or "",
                    city=item.city or "",
                    industry=item.industry or "",
                    experience_level=item.experience_level or "",
                )
                for item in response_dto.items
            ]

            return pb2.ListUserProfilesResponse(
                items=items,
                total=response_dto.total
            )

    async def SetUserAvatar(self, request, context):
        async with async_session_maker() as session:
            container = Container(session)

            try:
                image_id = await container.profile_service.set_avatar.execute(
                    user_id=UUID(request.user_id),
                    original_url=request.original_url,
                    thumb_small_url=request.thumb_small_url or None,
                    thumb_medium_url=request.thumb_medium_url or None,
                )

                await container.uow.commit()

            except ProfileNotFoundError as e:
                await container.uow.rollback()
                await context.abort(
                    grpc.StatusCode.NOT_FOUND,
                    str(e),
                )

            except Exception as e:
                await container.uow.rollback()
                await context.abort(
                    grpc.StatusCode.INTERNAL,
                    "Failed to set user avatar",
                )

            return pb2.SetUserAvatarResponse(
                image_id=str(image_id),
            )

    async def ListProfilesByIds(self, request, context):
        async with async_session_maker() as session:
            container = Container(session)

            response_dto = await container.profile_service.get_profiles_by_ids.execute(
                list(request.user_ids)
            )

            items = [
                pb2.GetProfilesByIdsItem(
                    user_id=item.user_id,
                    full_name=item.full_name or "",
                    bio=item.bio or "",
                    industry=item.industry or "",
                    experience_level=item.experience_level or "",
                    avatar=pb2.UserAvatar(
                        original_url=item.avatar.original_url,
                        thumb_small_url=item.avatar.thumb_small_url or "",
                        thumb_medium_url=item.avatar.thumb_medium_url or "",
                    ) if item.avatar else None,
                )
                for item in response_dto.items
            ]

            return pb2.ListProfilesByIdsResponse(
                users=items
            )
