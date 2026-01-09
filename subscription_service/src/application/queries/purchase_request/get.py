from src.application.queries.purchase_request.dto import (
    GetPurchaseRequestDTO,
)
from src.domain.repositories.purchase_request_repository import (
    IPurchaseRequestRepository,
)


class GetPurchaseRequestQuery:
    def __init__(self, repo: IPurchaseRequestRepository):
        self.repo = repo

    async def execute(self, dto: GetPurchaseRequestDTO):
        return await self.repo.get_by_id(
            request_id=dto.request_id
        )
