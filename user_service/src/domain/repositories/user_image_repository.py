from abc import ABC, abstractmethod

from src.domain.entities import UserImageEntity


class IUserImageRepository(ABC):

    @abstractmethod
    async def add(self, image: UserImageEntity) -> None:
        pass
