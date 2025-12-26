from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID

from src.domain.entities.image_entity import ImageEntity


class IImageRepository(ABC):

    @abstractmethod
    async def get_by_id(self, image_id: UUID) -> Optional[ImageEntity]:
        pass

    @abstractmethod
    async def save(self, image: ImageEntity) -> ImageEntity:
        pass
