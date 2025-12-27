from abc import ABC, abstractmethod
from uuid import UUID

from src.domain.entities.user_education_entity import UserEducationEntity


class IUserEducationRepository(ABC):

    @abstractmethod
    async def create(
        self,
        education: UserEducationEntity,
    ) -> UserEducationEntity:
        pass

    @abstractmethod
    async def list_by_user_id(
        self,
        user_id: UUID,
        limit: int,
        offset: int,
    ) -> tuple[list[UserEducationEntity], int]:
        pass

    @abstractmethod
    async def delete(self, education_id: UUID) -> None:
        pass
