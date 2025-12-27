from abc import ABC, abstractmethod
from uuid import UUID

from src.domain.entities.user_experience_entity import UserExperienceEntity


class IUserExperienceRepository(ABC):

    @abstractmethod
    async def create(
        self,
        experience: UserExperienceEntity,
    ) -> UserExperienceEntity:
        pass

    @abstractmethod
    async def list_by_user_id(
        self,
        user_id: UUID,
        limit: int,
        offset: int,
    ) -> tuple[list[UserExperienceEntity], int]:
        pass

    @abstractmethod
    async def delete(self, experience_id: UUID) -> None:
        pass
