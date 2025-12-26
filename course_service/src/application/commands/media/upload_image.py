
from src.domain.entities.image_entity import ImageEntity
from src.domain.dto.image_dto import UploadImageDTO
from src.domain.repositories.image_repository import IImageRepository


class UploadImageCommand:
    def __init__(self, repo: IImageRepository):
        self.repo = repo

    async def execute(self, dto: UploadImageDTO) -> ImageEntity:
        image = ImageEntity(
            type=dto.type,
            original_url=dto.original_url,
            thumb_small_url=dto.thumb_small_url,
            thumb_medium_url=dto.thumb_medium_url,
        )

        return await self.repo.save(image)
