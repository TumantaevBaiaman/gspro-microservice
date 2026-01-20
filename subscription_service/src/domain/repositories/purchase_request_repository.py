from abc import ABC, abstractmethod

from pydantic import EmailStr

from src.domain.enums.purchase_request import (
    PurchaseTargetType,
    PurchaseRequestStatus,
)
from src.infrastructure.db.mongo.models.purchase_request_document import (
    PurchaseRequestDocument,
)


class IPurchaseRequestRepository(ABC):

    @abstractmethod
    async def create(
        self,
        *,
        user_id: str | None,
        email: EmailStr,
        phone_number: str,
        telegram: str | None,
        target_type: PurchaseTargetType,
        target_id: str,
    ) -> PurchaseRequestDocument:
        ...

    @abstractmethod
    async def update_status(
        self,
        *,
        request_id: str,
        status: PurchaseRequestStatus,
    ) -> bool:
        ...

    @abstractmethod
    async def list(
        self,
        *,
        limit: int,
        offset: int,
    ):
        ...

    @abstractmethod
    async def get_by_id(
            self,
            request_id: str,
    ) -> PurchaseRequestDocument:
        ...
