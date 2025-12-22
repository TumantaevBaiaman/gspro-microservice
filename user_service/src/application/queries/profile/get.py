from src.domain.dto.profile_dto import (
    GetProfileRequestDTO,
    GetProfileResponseDTO,
    AvatarDTO
)
from src.domain.exceptions.profile import ProfileNotFoundError


class GetProfileQuery:
    def __init__(self, repo, image_repo):
        self.repo = repo
        self.image_repo = image_repo

    async def execute(
        self,
        dto: GetProfileRequestDTO
    ) -> GetProfileResponseDTO:

        profile = await self.repo.get_profile_by_user_id(dto.user_id)
        if profile is None:
            raise ProfileNotFoundError("Profile not found")

        avatar = await self.image_repo.get_by_id(profile.avatar_image_id) if profile.avatar_image_id else None
        if avatar:
            avatar = AvatarDTO(
                original_url=avatar.original_url,
                thumb_small_url=avatar.thumb_small_url,
                thumb_medium_url=avatar.thumb_medium_url,
            )

        return GetProfileResponseDTO(
            full_name=profile.full_name,
            phone_number=profile.phone_number,
            bio=profile.bio,
            industry=profile.industry,
            city=profile.city,
            experience_level=profile.experience_level,
            avatar=avatar,
        )