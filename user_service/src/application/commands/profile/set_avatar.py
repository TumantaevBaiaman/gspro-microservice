from uuid import UUID

from src.domain.entities import UserImageEntity
from src.domain.repositories.user_image_repository import IUserImageRepository
from src.domain.repositories.profile_repository import IProfileRepository


class SetUserAvatarCommand:

    def __init__(
        self,
        image_repo: IUserImageRepository,
        profile_repo: IProfileRepository,
    ):
        self.image_repo = image_repo
        self.profile_repo = profile_repo

    async def execute(
        self,
        user_id: UUID,
        original_url: str,
        thumb_small_url: str | None,
        thumb_medium_url: str | None,
    ) -> UUID:
        image = UserImageEntity.create_avatar(
            user_id=user_id,
            original_url=original_url,
            thumb_small_url=thumb_small_url,
            thumb_medium_url=thumb_medium_url,
        )

        await self.image_repo.add(image)

        await self.profile_repo.set_avatar_image(
            user_id=user_id,
            image_id=image.id,
        )

        return image.id
