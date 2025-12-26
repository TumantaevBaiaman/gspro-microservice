from uuid import UUID
from datetime import datetime

from src.application.commands.user_experience.dto import CreateUserExperienceDTO
from src.domain.entities.user_experience_entity import UserExperienceEntity
from src.domain.repositories.user_experience_repository import (
    IUserExperienceRepository,
)


class CreateUserExperienceCommand:

    def __init__(self, repo: IUserExperienceRepository):
        self.repo = repo

    async def execute(
        self,
        *,
        user_id: UUID,
        dto: CreateUserExperienceDTO,
    ) -> UserExperienceEntity:

        experience = UserExperienceEntity(
            id=None,
            user_id=user_id,
            company=dto.company,
            position=dto.position,
            start_date=dto.start_date,
            end_date=dto.end_date,
            description=dto.description,
            created_at=datetime.utcnow(),
        )

        return await self.repo.create(experience)
