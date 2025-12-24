from pymongo.errors import DuplicateKeyError

from src.domain.dto.admin_course_dto import AdminCourseUpdateDTO
from src.domain.repositories import IAdminCourseRepository
from src.domain.exceptions.admin_course import (
    CourseNotFoundError,
    CourseAlreadyExistsError,
)


class UpdateCourseCommand:
    def __init__(self, repo: IAdminCourseRepository):
        self.repo = repo

    async def execute(self, course_id: str, dto: AdminCourseUpdateDTO):
        data = dto.model_dump(exclude_unset=True)

        if not data:
            course = await self.repo.get(course_id)
            if not course:
                raise CourseNotFoundError(course_id)
            return course

        return await self.repo.update(course_id, data)
