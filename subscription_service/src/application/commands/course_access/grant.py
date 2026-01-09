from src.application.commands.course_access.dto import (
    GrantCourseAccessDTO,
)
from src.domain.repositories.course_access_repository import (
    ICourseAccessRepository,
)


class GrantCourseAccessCommand:
    def __init__(self, repo: ICourseAccessRepository):
        self.repo = repo

    async def execute(self, dto: GrantCourseAccessDTO):
        exists = await self.repo.has_access(
            user_id=dto.user_id,
            course_id=dto.course_id,
        )

        if exists:
            return None

        return await self.repo.grant(
            user_id=dto.user_id,
            course_id=dto.course_id,
        )
