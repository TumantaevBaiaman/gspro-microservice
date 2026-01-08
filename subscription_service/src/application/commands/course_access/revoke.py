from src.application.commands.course_access.dto import (
    RevokeCourseAccessDTO,
)
from src.domain.repositories.course_access_repository import (
    ICourseAccessRepository,
)


class RevokeCourseAccessCommand:
    def __init__(self, repo: ICourseAccessRepository):
        self.repo = repo

    async def execute(self, dto: RevokeCourseAccessDTO) -> bool:
        return await self.repo.revoke(
            user_id=dto.user_id,
            course_id=dto.course_id,
        )
