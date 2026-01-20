from abc import ABC, abstractmethod
from typing import List

from bson import ObjectId

from src.domain.entities.course_entity import CourseEntity


class ICourseRepository(ABC):

    @abstractmethod
    async def get_course_by_id(self, course_id: str) -> CourseEntity:
        pass

    @abstractmethod
    async def list(
            self,
            limit: int,
            offset: int,
            mode: str,
            author_id: str = None,
    ) -> tuple[list[CourseEntity], int]:
        pass

    @abstractmethod
    async def list_by_ids(
            self,
            course_ids,
    ) -> List[CourseEntity]:
        pass
