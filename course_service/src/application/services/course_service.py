from src.application.queries.admin_course import ListCoursesQuery
from src.application.queries.course.get_course import GetCourseQuery
from src.domain.repositories.course_repository import ICourseRepository


class CourseService:
    def __init__(self, repo: ICourseRepository):
        self.get = GetCourseQuery(repo)
        self.list = ListCoursesQuery(repo)