from src.domain.exceptions.lesson import LessonNotFoundError


class GetLessonQuery:
    def __init__(self, repo):
        self.repo = repo

    async def execute(self, lesson_id: str):
        lesson = await self.repo.get_by_id(lesson_id)
        if not lesson:
            raise LessonNotFoundError()
        return lesson
