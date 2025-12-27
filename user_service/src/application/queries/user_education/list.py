from uuid import UUID

from src.domain.repositories.user_education_repository import (
    IUserEducationRepository,
)


class ListUserEducationsQuery:

    def __init__(self, repo: IUserEducationRepository):
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
