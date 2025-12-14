from src.domain.repositories.admin_lesson_repository import IAdminLessonRepository


class ListLessonsQuery:
    def __init__(self, repo: IAdminLessonRepository):
        self.repo = repo

    async def execute(self, module_id: str | None = None):
        return await self.repo.list(module_id)
