

class ListLessonsByModuleQuery:
    def __init__(self, repo):
        self.repo = repo

    async def execute(self, module_id: str):
        return await self.repo.list_by_module_id(module_id)
