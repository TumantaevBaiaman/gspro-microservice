from src.domain.repositories.course_repository import ICourseRepository


class ListCoursesQuery:
    def __init__(self, repo: ICourseRepository):
        self.repo = repo

    async def execute(self, limit: int, offset: int):
        items, total = await self.repo.list_courses(
            limit=limit,
            offset=offset
        )
        return items, total