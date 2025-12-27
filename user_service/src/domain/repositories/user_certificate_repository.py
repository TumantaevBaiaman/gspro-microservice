from abc import ABC, abstractmethod
from uuid import UUID

from src.domain.entities.user_certificate_entity import UserCertificateEntity


class IUserCertificateRepository(ABC):

    @abstractmethod
    async def create(
        self,
        certificate: UserCertificateEntity,
    ) -> UserCertificateEntity:
        pass

    @abstractmethod
    async def list_by_user_id(
        self,
        user_id: UUID,
        limit: int,
        offset: int,
    ) -> tuple[list[UserCertificateEntity], int]:
        pass

    @abstractmethod
    async def delete(self, certificate_id: UUID) -> None:
        pass
