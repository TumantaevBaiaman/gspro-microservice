from src.domain.repositories import ICourseRepository


class ListCoursesQuery:
    def __init__(self, repo: ICourseRepository):
        self.repo = repo

    async def execute(self, limit: int, offset: int) -> tuple[list, int]:
        limit = max(1, min(limit, 100))
        offset = max(0, offset)

        courses, total = await self.repo.list(
            limit=limit,
            offset=offset,
        )

        return courses, total
