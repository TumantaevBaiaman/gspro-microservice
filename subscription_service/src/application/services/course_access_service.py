from src.application.queries.course_access.list_user_courses import (
    ListUserCoursesQuery,
)
from src.application.commands.course_access.grant import (
    GrantCourseAccessCommand,
)
from src.application.commands.course_access.revoke import (
    RevokeCourseAccessCommand,
)
from src.application.queries.course_access.has_access import (
    HasCourseAccessQuery,
)
from src.domain.repositories.course_access_repository import (
    ICourseAccessRepository,
)


class CourseAccessService:
    def __init__(self, repo: ICourseAccessRepository):
        self.grant = GrantCourseAccessCommand(repo)
        self.revoke = RevokeCourseAccessCommand(repo)
        self.has_access = HasCourseAccessQuery(repo)
        self.list_user_courses = ListUserCoursesQuery(repo)
