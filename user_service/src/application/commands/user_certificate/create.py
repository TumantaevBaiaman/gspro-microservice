from uuid import UUID
from datetime import datetime

from src.application.commands.user_certificate.dto import CreateUserCertificateDTO
from src.domain.entities.user_certificate_entity import UserCertificateEntity
from src.domain.repositories.user_certificate_repository import (
    IUserCertificateRepository,
)


class CreateUserCertificateCommand:

    def __init__(self, repo: IUserCertificateRepository):
        self.repo = repo

    async def execute(
        self,
        *,
        user_id: UUID,
        dto: CreateUserCertificateDTO,
    ) -> UserCertificateEntity:

        certificate = UserCertificateEntity(
            id=None,
            user_id=user_id,
            title=dto.title,
            issuer=dto.issuer,
            issued_at=dto.issued_at,
            link=dto.link,
            created_at=datetime.utcnow(),
        )

        return await self.repo.create(certificate)
