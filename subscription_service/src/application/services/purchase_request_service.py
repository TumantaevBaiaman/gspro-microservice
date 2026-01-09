from src.application.commands.purchase_request.create import (
    CreatePurchaseRequestCommand
)
from src.application.commands.purchase_request.update_status import (
    UpdatePurchaseRequestStatusCommand
)
from src.application.queries.purchase_request.list import (
    ListPurchaseRequestsQuery,
)
from src.application.queries.purchase_request.get import (
    GetPurchaseRequestQuery,
)
from src.domain.repositories.purchase_request_repository import (
    IPurchaseRequestRepository,
)


class PurchaseRequestService:
    def __init__(self, repo: IPurchaseRequestRepository):
        self.create = CreatePurchaseRequestCommand(repo)
        self.list = ListPurchaseRequestsQuery(repo)
        self.get_by_id = GetPurchaseRequestQuery(repo)
        self.update_status = UpdatePurchaseRequestStatusCommand(repo)
