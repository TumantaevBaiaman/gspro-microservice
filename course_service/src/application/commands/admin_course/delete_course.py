from src.domain.repositories import IAdminCourseRepository
from src.domain.exceptions.admin_course import CourseNotFoundError


class DeleteCourseCommand:
    def __init__(self, repo: IAdminCourseRepository):
        self.repo = repo

    async def execute(self, course_id: str):
        course = await self.repo.get(course_id)
        if not course:
            raise CourseNotFoundError("Course not found")

        await self.repo.delete(course_id)
