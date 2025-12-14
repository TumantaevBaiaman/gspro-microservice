from src.application.commands.admin_course.create_course import CreateCourseCommand
from src.application.commands.admin_course.update_course import UpdateCourseCommand
from src.application.commands.admin_course.delete_course import DeleteCourseCommand
from src.application.queries.admin_course.get_course import GetCourseQuery
from src.application.queries.admin_course.list_courses import ListCoursesQuery
from src.domain.repositories import IAdminCourseRepository


class AdminCourseService:
    def __init__(self, repo: IAdminCourseRepository):
        self.create = CreateCourseCommand(repo)
        self.update = UpdateCourseCommand(repo)
        self.delete = DeleteCourseCommand(repo)
        self.get = GetCourseQuery(repo)
        self.list = ListCoursesQuery(repo)
