from uuid import UUID
from datetime import datetime

from src.application.commands.user_education.dto import CreateUserEducationDTO
from src.domain.entities.user_education_entity import UserEducationEntity
from src.domain.repositories.user_education_repository import (
    IUserEducationRepository,
)


class CreateUserEducationCommand:

    def __init__(self, repo: IUserEducationRepository):
        self.repo = repo

    async def execute(
        self,
        *,
        user_id: UUID,
        dto: CreateUserEducationDTO,
    ) -> UserEducationEntity:

        education = UserEducationEntity(
            id=None,
            user_id=user_id,
            institution=dto.institution,
            degree=dto.degree,
            start_year=dto.start_year,
            end_year=dto.end_year,
            created_at=datetime.utcnow(),
        )

        return await self.repo.create(education)
