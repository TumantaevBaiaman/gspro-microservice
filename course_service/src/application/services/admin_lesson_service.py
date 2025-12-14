from src.application.commands.admin_lesson.create_lesson import CreateLessonCommand
from src.application.commands.admin_lesson.update_lesson import UpdateLessonCommand
from src.application.commands.admin_lesson.delete_lesson import DeleteLessonCommand
from src.application.queries.admin_lesson.get_lesson import GetLessonQuery
from src.application.queries.admin_lesson.list_lessons import ListLessonsQuery
from src.domain.repositories.admin_lesson_repository import IAdminLessonRepository


class AdminLessonService:
    def __init__(self, repo: IAdminLessonRepository):
        self.create = CreateLessonCommand(repo)
        self.update = UpdateLessonCommand(repo)     # problem update method
        self.delete = DeleteLessonCommand(repo)
        self.get = GetLessonQuery(repo)
        self.list = ListLessonsQuery(repo)
