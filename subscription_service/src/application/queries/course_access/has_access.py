from src.application.queries.course_access.dto import (
    CheckCourseAccessDTO,
)
from src.domain.repositories.course_access_repository import (
    ICourseAccessRepository,
)


class HasCourseAccessQuery:
    def __init__(self, repo: ICourseAccessRepository):
        self.repo = repo

    async def execute(self, dto: CheckCourseAccessDTO) -> bool:
        return await self.repo.has_access(
            user_id=dto.user_id,
            course_id=dto.course_id,
        )
