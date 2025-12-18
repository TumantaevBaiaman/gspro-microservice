from abc import ABC, abstractmethod

from src.domain.entities.course_entity import CourseEntity


class ICourseRepository(ABC):

    @abstractmethod
    async def get_course_by_id(self, course_id: str) -> CourseEntity:
        pass

    @abstractmethod
    async def list_courses(self, limit: int,  offset: int) -> list[CourseEntity]:
        pass
