from uuid import UUID

from src.domain.repositories.user_education_repository import (
    IUserEducationRepository,
)


class DeleteUserEducationCommand:

    def __init__(self, repo: IUserEducationRepository):
        self.repo = repo

    async def execute(self, education_id: UUID) -> None:
        await self.repo.delete(education_id)
