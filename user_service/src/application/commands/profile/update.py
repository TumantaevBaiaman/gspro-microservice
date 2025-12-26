from src.domain.exceptions.profile import ProfileNotFoundError


class UpdateProfileCommand:
    def __init__(self, profile_repo):
        self.profile_repo = profile_repo

    async def execute(
        self,
        user_id: str,
        update_data: dict
    ) -> None:

        profile = await self.profile_repo.get_profile_by_user_id(user_id)
        if profile is None:
            raise ProfileNotFoundError("Profile not found")

        await self.profile_repo.update_profile(
            profile.id,
            update_data
        )