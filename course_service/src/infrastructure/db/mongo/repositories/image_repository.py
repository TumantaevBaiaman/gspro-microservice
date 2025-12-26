from uuid import UUID
from typing import Optional

from src.domain.entities.image_entity import ImageEntity
from src.domain.enums.image_type import ImageType
from src.domain.repositories.image_repository import IImageRepository


class ImageRepository(IImageRepository):

    async def get_by_id(self, image_id: UUID) -> Optional[ImageEntity]:
        return await ImageEntity.get(image_id)

    async def get_by_owner_and_type(
        self,
        *,
        owner_type: str,
        owner_id: str,
        image_type: ImageType,
    ) -> Optional[ImageEntity]:
        return await ImageEntity.find_one(
            ImageEntity.owner_type == owner_type,
            ImageEntity.owner_id == owner_id,
            ImageEntity.type == image_type,
        )

    async def save(self, image: ImageEntity) -> ImageEntity:
        await image.save()
        return image
