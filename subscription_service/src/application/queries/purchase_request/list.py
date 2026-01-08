from src.application.queries.purchase_request.dto import (
    ListPurchaseRequestsDTO,
)
from src.domain.repositories.purchase_request_repository import (
    IPurchaseRequestRepository,
)


class ListPurchaseRequestsQuery:
    def __init__(self, repo: IPurchaseRequestRepository):
        self.repo = repo

    async def execute(self, dto: ListPurchaseRequestsDTO):
        return await self.repo.list(
            limit=dto.limit,
            offset=dto.offset,
        )
