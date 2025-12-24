from sqlalchemy import select

from src.domain.entities import UserImageEntity
from src.domain.repositories.user_image_repository import IUserImageRepository
from src.infrastructure.db.models import UserImageModel


class UserImageRepository(IUserImageRepository):

    def __init__(self, session):
        self.session = session

    async def add(self, image: UserImageEntity) -> None:
        model = UserImageModel(
            user_id=image.user_id,
            type=image.type,
            original_url=image.original_url,
            thumb_small_url=image.thumb_small_url,
            thumb_medium_url=image.thumb_medium_url,
        )

        self.session.add(model)
        await self.session.flush()
        image.id = model.id

    async def get_by_id(self, image_id: str) -> UserImageModel | None:
        stmt = select(UserImageModel).where(UserImageModel.id == image_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
