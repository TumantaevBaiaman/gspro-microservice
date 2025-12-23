from src.application.queries.lesson.get_lesson import GetLessonQuery
from src.application.queries.lesson.list_lessons_by_module import (
    ListLessonsByModuleQuery
)
from src.domain.repositories.lesson_repository import ILessonRepository


class LessonService:
    def __init__(self, repo: ILessonRepository):
        self.get = GetLessonQuery(repo)
        self.list_by_module = ListLessonsByModuleQuery(repo)
