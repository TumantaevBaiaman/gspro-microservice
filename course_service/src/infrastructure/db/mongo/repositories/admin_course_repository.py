from beanie import PydanticObjectId
from beanie.operators import Set
from pymongo.errors import DuplicateKeyError

from src.domain.dto.admin_course_dto import (
    AdminCourseCreateDTO,
    AdminCourseUpdateDTO,
)
from src.domain.entities import CourseEntity
from src.domain.repositories.admin_course_repository import IAdminCourseRepository
from src.domain.exceptions.admin_course import CourseNotFoundError, CourseAlreadyExistsError


class AdminCourseRepository(IAdminCourseRepository):

    async def create(self, dto: AdminCourseCreateDTO) -> CourseEntity:
        try:
            course = CourseEntity(**dto.model_dump())
            return await course.insert()
        except DuplicateKeyError:
            raise CourseAlreadyExistsError(
                "Course with this title already exists"
            )

    async def get(self, course_id: str) -> CourseEntity | None:
        return await CourseEntity.get(course_id)

    async def list(self) -> list[CourseEntity]:
        return await CourseEntity.find_all().to_list()

    async def update(self, course_id: str, data: dict) -> CourseEntity:
        query = CourseEntity.find_one(
            CourseEntity.id == PydanticObjectId(course_id)
        )

        result = await query.update(Set(data))

        if result.matched_count == 0:
            raise CourseNotFoundError(course_id)

        return await self.get(course_id)

    async def delete(self, course_id: str):
        course = await self.get(course_id)
        if not course:
            raise CourseNotFoundError(course_id)

        await course.delete()
