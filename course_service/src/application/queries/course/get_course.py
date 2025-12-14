from src.domain.repositories.course_repository import ICourseRepository
from src.domain.exceptions.course import CourseNotFoundError


class GetCourseQuery:
    def __init__(self, repo: ICourseRepository):
        self.repo = repo

    async def execute(self, course_id: str):
        course = await self.repo.get_course_by_id(course_id)
        if not course:
            raise CourseNotFoundError("Course not found")

        return course