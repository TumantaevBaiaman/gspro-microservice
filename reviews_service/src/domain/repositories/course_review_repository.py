from abc import ABC, abstractmethod

from src.infrastructure.db.mongo.models.course_review import CourseReviewDocument


class ICourseReviewRepository(ABC):

    @abstractmethod
    async def create(
        self,
        *,
        course_id: str,
        user_id: str,
        rating: int,
        comment: str,
        tags: list[str],
    ) -> CourseReviewDocument:
        ...

    @abstractmethod
    async def list_by_course(
        self,
        *,
        course_id: str,
        limit: int,
        offset: int,
    ) -> tuple[list[CourseReviewDocument], int]:
        ...

    @abstractmethod
    async def exists_by_user_and_course(
        self,
        *,
        course_id: str,
        user_id: str,
    ) -> bool:
        ...

    @abstractmethod
    async def get_course_rating(
        self,
        *,
        course_id: str,
    ) -> tuple[float, int]:
        ...
