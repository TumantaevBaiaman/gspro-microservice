from beanie.operators import Set

from src.domain.dto.admin_course_dto import AdminCourseCreateDTO, AdminCourseUpdateDTO
from src.domain.entities import CourseEntity
from src.domain.repositories.admin_course_repository import IAdminCourseRepository


class AdminCourseRepository(IAdminCourseRepository):

    async def create(self, dto: AdminCourseCreateDTO) -> CourseEntity:
        course = CourseEntity(**dto.dict())
        return await course.insert()

    async def get(self, course_id: str) -> CourseEntity | None:
        return await CourseEntity.get(course_id)

    async def list(self) -> list[CourseEntity]:
        return await CourseEntity.find_all().to_list()

    async def update(self, course_id: str, data: dict) -> CourseEntity:
        await CourseEntity.find_one(
            CourseEntity.id == course_id
        ).update(
            Set(data)
        )

        return await self.get(course_id)

    async def delete(self, course: CourseEntity):
        return await course.delete()
