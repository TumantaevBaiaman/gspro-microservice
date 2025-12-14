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
        course = await self.repo.get(course_id)
        if not course:
            raise CourseNotFoundError("Course not found")

        for key, value in dto.model_dump(exclude_unset=True).items():
            setattr(course, key, value)

        try:
            return await self.repo.save(course)
        except DuplicateKeyError:
            raise CourseAlreadyExistsError(
                "Course already exists with given unique values"
            )
