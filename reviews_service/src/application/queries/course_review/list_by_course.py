class ListReviewsByCourseQuery:
    def __init__(self, repo):
        self.repo = repo

    async def execute(self, *, course_id: str, limit: int, offset: int):
        return await self.repo.list_by_course(
            course_id=course_id,
            limit=limit,
            offset=offset,
        )