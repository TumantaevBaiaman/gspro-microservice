from uuid import UUID

from src.domain.repositories.user_experience_repository import (
    IUserExperienceRepository,
)


class DeleteUserExperienceCommand:

    def __init__(self, repo: IUserExperienceRepository):
        self.repo = repo

    async def execute(self, experience_id: UUID) -> None:
        await self.repo.delete(experience_id)
