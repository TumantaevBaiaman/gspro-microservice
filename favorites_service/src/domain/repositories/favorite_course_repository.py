from abc import ABC, abstractmethod
from src.infrastructure.db.mongo.models.favorite_course import FavoriteCourseDocument


class IFavoriteCourseRepository(ABC):

    @abstractmethod
    async def add(
        self,
        *,
        user_id: str,
        course_id: str,
    ) -> FavoriteCourseDocument:
        ...

    @abstractmethod
    async def remove(
        self,
        *,
        user_id: str,
        course_id: str,
    ) -> bool:
        ...

    @abstractmethod
    async def list_by_user(
        self,
        *,
        user_id: str,
        limit: int,
        offset: int,
    ) -> tuple[list[FavoriteCourseDocument], int]:
        ...

    @abstractmethod
    async def is_favorite(
        self,
        *,
        user_id: str,
        course_id: str,
    ) -> bool:
        ...