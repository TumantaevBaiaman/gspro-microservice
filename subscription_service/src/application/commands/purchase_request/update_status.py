from src.domain.repositories.purchase_request_repository import (
    IPurchaseRequestRepository,
)
from src.domain.enums.purchase_request import (
    PurchaseRequestStatus,
)


class UpdatePurchaseRequestStatusCommand:
    def __init__(self, repo: IPurchaseRequestRepository):
        self.repo = repo

    async def execute(
        self,
        *,
        request_id: str,
        status: PurchaseRequestStatus,
    ) -> bool:
        return await self.repo.update_status(
            request_id=request_id,
            status=status,
        )
