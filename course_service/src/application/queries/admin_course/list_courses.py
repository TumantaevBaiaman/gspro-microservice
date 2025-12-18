from src.domain.repositories import IAdminCourseRepository


class ListCoursesQuery:
    def __init__(self, repo: IAdminCourseRepository):
        self.repo = repo

    async def execute(self, limit: int, offset: int):
        # return await self.repo.list_courses(
        #     limit=limit,
        #     offset=offset
        # )
        pass
