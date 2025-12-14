from src.domain.repositories import IAdminCourseRepository


class ListCoursesQuery:
    def __init__(self, repo: IAdminCourseRepository):
        self.repo = repo

    async def execute(self):
        return await self.repo.list()
