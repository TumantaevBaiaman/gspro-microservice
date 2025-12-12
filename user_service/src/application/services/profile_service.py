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
