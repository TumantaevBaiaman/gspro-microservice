from src.application.commands.purchase_request.dto import (
    CreatePurchaseRequestDTO,
)
from src.domain.repositories.purchase_request_repository import (
    IPurchaseRequestRepository,
)


class CreatePurchaseRequestCommand:
    def __init__(self, repo: IPurchaseRequestRepository):
        self.repo = repo

    async def execute(self, dto: CreatePurchaseRequestDTO):
        return await self.repo.create(
            user_id=dto.user_id,
            email=dto.email,
            phone_number=dto.phone_number,
            target_type=dto.target_type,
            target_id=dto.target_id,
        )
