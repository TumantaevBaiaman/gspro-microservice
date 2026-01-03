from src.application.queries.admin_course import ListCoursesQuery
from src.application.queries.course.get_course import GetCourseQuery
from src.application.queries.course.get_lessons_count import GetCourseLessonsCountQuery
from src.domain.repositories.course_repository import ICourseRepository


class CourseService:
    def __init__(self,
                 repo: ICourseRepository,
                 lesson_service,
    ):
        self.get = GetCourseQuery(repo)
        self.list = ListCoursesQuery(repo)
        self.get_lessons_count = GetCourseLessonsCountQuery(lesson_service)
