from src.domain.dto.profile_dto import (
    GetProfileRequestDTO,
    GetProfileResponseDTO,
)
from src.domain.exceptions.profile import ProfileNotFoundError


class GetProfileQuery:
    def __init__(self, repo):
        self.repo = repo

    async def execute(
        self,
        dto: GetProfileRequestDTO
    ) -> GetProfileResponseDTO:

        profile = await self.repo.get_profile_by_user_id(dto.user_id)
        if profile is None:
            raise ProfileNotFoundError("Profile not found")

        return GetProfileResponseDTO(
            full_name=profile.full_name,
            phone_number=profile.phone_number,
            bio=profile.bio,
            industry=profile.industry,
            city=profile.city,
            experience_level=profile.experience_level,
        )