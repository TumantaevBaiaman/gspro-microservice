from src.domain.dto.profile_dto import (
    ListProfilesByIdsResponseDTO,
    ListProfilesByIdsItemDTO
)


class ListProfilesByIdsQuery:
    def __init__(self, repo, image_repo):
        self.repo = repo
        self.image_repo = image_repo

    async def execute(
            self,
            user_ids: list[str]
    ) -> ListProfilesByIdsResponseDTO:
        profiles = await self.repo.list_profiles_by_ids(user_ids=user_ids)
        items = []
        for profile in profiles:
            avatar = None
            if profile.avatar_image_id:
                avatar_image = await self.image_repo.get_by_id(profile.avatar_image_id)
                if avatar_image:
                    avatar = {
                        "original_url": avatar_image.original_url,
                        "thumb_small_url": avatar_image.thumb_small_url,
                        "thumb_medium_url": avatar_image.thumb_medium_url,
                    }

            items.append(
                ListProfilesByIdsItemDTO(
                    user_id=str(profile.user_id),
                    full_name=profile.full_name,
                    phone_number=profile.phone_number,
                    city=profile.city,
                    industry=profile.industry,
                    experience_level=profile.experience_level,
                    avatar=avatar,
                )
            )
        return ListProfilesByIdsResponseDTO(items=items)