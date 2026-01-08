from abc import ABC, abstractmethod
from src.infrastructure.db.mongo.models.course_access_document import (
    CourseAccessDocument,
)


class ICourseAccessRepository(ABC):

    @abstractmethod
    async def grant(
        self,
        *,
        user_id: str,
        course_id: str,
    ) -> CourseAccessDocument:
        ...

    @abstractmethod
    async def revoke(
        self,
        *,
        user_id: str,
        course_id: str,
    ) -> bool:
        ...

    @abstractmethod
    async def has_access(
        self,
        *,
        user_id: str,
        course_id: str,
    ) -> bool:
        ...
