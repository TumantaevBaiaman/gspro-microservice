from src.domain.dto.profile_dto import (
    GetProfileResponseDTO,
    GetProfileRequestDTO,
)


class ProfileService:

    def __init__(self, profile_repo):
        self.profile_repo = profile_repo

    async def get_profile_by_user_id(
        self,
        dto: GetProfileRequestDTO
    ) -> GetProfileResponseDTO | None:

        profile = await self.profile_repo.get_profile_by_user_id(dto.user_id)
        if profile is None:
            return None

        return GetProfileResponseDTO(
            full_name=profile.full_name,
            bio=profile.bio,
            industry=profile.industry,
            city=profile.city,
            experience_level=profile.experience_level,
        )

    async def update_profile(
        self,
        user_id: str,
        update_data: dict
    ) -> GetProfileResponseDTO | None:

        profile = await self.profile_repo.get_profile_by_user_id(user_id)
        if profile is None:
            return None

        updated_profile = await self.profile_repo.update_profile(profile.id, update_data)

        return GetProfileResponseDTO(
            full_name=updated_profile.full_name,
            bio=updated_profile.bio,
            industry=updated_profile.industry,
            city=updated_profile.city,
            experience_level=updated_profile.experience_level,
        )