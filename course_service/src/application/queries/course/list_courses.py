from src.domain.repositories.course_repository import ICourseRepository


class ListCoursesQuery:
    def __init__(self, repo: ICourseRepository):
        self.repo = repo

    async def execute(self, limit: int, offset: int, mode: str):
        items, total = await self.repo.list(
            limit=limit,
            offset=offset,
            mode=mode
        )
        return items, total