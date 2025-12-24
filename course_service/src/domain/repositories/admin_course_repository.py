from abc import ABC, abstractmethod
from typing import Optional, List

from src.domain.entities import CourseEntity


class IAdminCourseRepository(ABC):

    @abstractmethod
    async def create(self, dto) -> CourseEntity:
        pass

    @abstractmethod
    async def get(self, course_id: str) -> Optional[CourseEntity]:
        pass

    @abstractmethod
    async def list(self) -> List[CourseEntity]:
        pass

    @abstractmethod
    async def update(self, course_id: str, data: dict) -> CourseEntity:
        pass

    @abstractmethod
    async def delete(self, course_id: str) -> None:
        pass
