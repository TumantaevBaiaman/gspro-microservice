from src.domain.entities import CourseEntity
from src.domain.repositories import ICourseRepository


class ListCoursesByIdsQuery:

    def __init__(self, repo: ICourseRepository):
        self.repo = repo

    async def execute(
        self,
        course_ids: list[str] | str,
    ) -> list[CourseEntity]:
        return await self.repo.list_by_ids(course_ids)
