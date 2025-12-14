from abc import ABC, abstractmethod

from src.domain.dto.admin_course_dto import AdminCourseCreateDTO
from src.domain.entities import CourseEntity


class IAdminCourseRepository(ABC):

    @abstractmethod
    async def create(self, dto: AdminCourseCreateDTO) -> CourseEntity:
        pass

    @abstractmethod
    async def get(self, course_id: str) -> CourseEntity | None:
        pass

    @abstractmethod
    async def list(self) -> list[CourseEntity]:
        pass

    @abstractmethod
    async def update(self, course_id: str, data: dict) -> CourseEntity:
        pass

    @abstractmethod
    async def delete(self, course: CourseEntity):
        pass
