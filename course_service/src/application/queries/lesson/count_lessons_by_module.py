from src.domain.repositories.lesson_repository import ILessonRepository


class CountLessonsByModuleQuery:
    def __init__(self, repo: ILessonRepository):
        self.repo = repo

    async def execute(self, module_id: str) -> int:
        return await self.repo.count_by_module_id(module_id)
