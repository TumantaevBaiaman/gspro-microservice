from abc import ABC, abstractmethod

from src.domain.entities import UserImageEntity
from src.infrastructure.db.models import UserImageModel


class IUserImageRepository(ABC):

    @abstractmethod
    async def add(self, image: UserImageEntity) -> None:
        pass

    @abstractmethod
    async def get_by_id(self, image_id: str) -> UserImageModel | None:
        pass
