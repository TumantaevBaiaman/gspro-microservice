from src.domain.dto.profile_dto import GetProfileResponseDTO
from src.domain.exceptions.profile import ProfileNotFoundError


class UpdateProfileCommand:
    def __init__(self, profile_repo):
        self.profile_repo = profile_repo

    async def execute(
        self,
        user_id: str,
        update_data: dict
    ) -> GetProfileResponseDTO:

        profile = await self.profile_repo.get_profile_by_user_id(user_id)
        if profile is None:
            raise ProfileNotFoundError("Profile not found")

        updated_profile = await self.profile_repo.update_profile(
            profile.id,
            update_data
        )

        return GetProfileResponseDTO(
            full_name=updated_profile.full_name,
            bio=updated_profile.bio,
            industry=updated_profile.industry,
            city=updated_profile.city,
            experience_level=updated_profile.experience_level,
        )