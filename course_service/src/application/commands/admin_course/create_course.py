from pymongo.errors import DuplicateKeyError

from src.domain.dto.admin_course_dto import AdminCourseCreateDTO
from src.domain.repositories import IAdminCourseRepository
from src.domain.exceptions.admin_course import CourseAlreadyExistsError


class CreateCourseCommand:
    def __init__(self, repo: IAdminCourseRepository):
        self.repo = repo

    async def execute(self, dto: AdminCourseCreateDTO):
        try:
            return await self.repo.create(dto)
        except DuplicateKeyError:
            raise CourseAlreadyExistsError(
                "Course with this title or codename already exists"
            )
