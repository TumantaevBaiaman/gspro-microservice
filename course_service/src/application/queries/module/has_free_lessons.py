class HasFreeLessonsQuery:
    def __init__(self, lesson_repo):
        self.lesson_repo = lesson_repo

    async def execute(self, module_id: str) -> bool:
        return await self.lesson_repo.has_free_lessons(module_id)
