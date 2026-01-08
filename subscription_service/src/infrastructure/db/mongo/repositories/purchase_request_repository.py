from pydantic import EmailStr

from src.domain.repositories.purchase_request_repository import (
    IPurchaseRequestRepository,
)
from src.infrastructure.db.mongo.models.purchase_request_document import (
    PurchaseRequestDocument,
)
from src.domain.enums.purchase_request import (
    PurchaseRequestStatus,
    PurchaseTargetType,
)


class PurchaseRequestRepository(IPurchaseRequestRepository):

    async def create(
        self,
        *,
        user_id: str | None,
        email: EmailStr,
        phone_number: str,
        target_type: PurchaseTargetType,
        target_id: str,
    ) -> PurchaseRequestDocument:
        doc = PurchaseRequestDocument(
            user_id=user_id,
            email=email,
            phone_number=phone_number,
            target_type=target_type,
            target_id=target_id,
        )
        await doc.insert()
        return doc

    async def update_status(
        self,
        *,
        request_id: str,
        status: PurchaseRequestStatus,
    ) -> bool:
        doc = await PurchaseRequestDocument.get(request_id)

        if not doc:
            return False

        doc.status = status
        await doc.save()
        return True

    async def list(
        self,
        *,
        limit: int,
        offset: int,
    ):
        query = PurchaseRequestDocument.find()

        total = await query.count()
        items = await (
            query
            .skip(offset)
            .limit(limit)
            .to_list()
        )
        return items, total
