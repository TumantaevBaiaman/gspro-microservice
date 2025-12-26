from uuid import UUID

from src.domain.repositories.user_certificate_repository import (
    IUserCertificateRepository,
)


class DeleteUserCertificateCommand:

    def __init__(self, repo: IUserCertificateRepository):
        self.repo = repo

    async def execute(self, certificate_id: UUID) -> None:
        await self.repo.delete(certificate_id)
