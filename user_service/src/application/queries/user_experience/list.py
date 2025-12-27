from uuid import UUID

from src.domain.repositories.user_experience_repository import (
    IUserExperienceRepository,
)


class ListUserExperiencesQuery:

    def __init__(self, repo: IUserExperienceRepository):
        self.repo = repo

    async def execute(
        self,
        *,
        user_id: UUID,
        limit: int,
        offset: int,
    ):
        return await self.repo.list_by_user_id(
            user_id=user_id,
            limit=limit,
            offset=offset,
        )
