from uuid import UUID

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.repositories.user_certificate_repository import (
    IUserCertificateRepository,
)
from src.infrastructure.db.models.user_certificate_model import (
    UserCertificateModel,
)
from src.domain.entities.user_certificate_entity import (
    UserCertificateEntity,
)


class UserCertificateRepository(IUserCertificateRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(
        self,
        certificate: UserCertificateEntity,
    ) -> UserCertificateEntity:

        model = UserCertificateModel(
            user_id=certificate.user_id,
            title=certificate.title,
            issuer=certificate.issuer,
            issued_at=certificate.issued_at,
            link=certificate.link,
        )

        self.session.add(model)
        await self.session.commit()
        await self.session.refresh(model)

        return UserCertificateEntity(
            id=model.id,
            user_id=model.user_id,
            title=model.title,
            issuer=model.issuer,
            issued_at=model.issued_at,
            link=model.link,
            created_at=model.created_at,
        )

    async def list_by_user_id(
        self,
        user_id: UUID,
        limit: int,
        offset: int,
    ) -> tuple[list[UserCertificateModel], int]:

        stmt = (
            select(UserCertificateModel)
            .where(UserCertificateModel.user_id == user_id)
            .limit(limit)
            .offset(offset)
        )

        count_stmt = (
            select(func.count())
            .select_from(UserCertificateModel)
            .where(UserCertificateModel.user_id == user_id)
        )

        result = await self.session.execute(stmt)
        items = result.scalars().all()

        count_result = await self.session.execute(count_stmt)
        total = count_result.scalar_one()

        return items, total

    async def delete(self, certificate_id: UUID) -> None:
        certificate = await self.session.get(UserCertificateModel, certificate_id)
        if not certificate:
            raise Exception("Certificate not found")

        await self.session.delete(certificate)
        await self.session.commit()
