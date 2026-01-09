from fastapi import APIRouter

from app.schemas.subscription.purchase_request import (
    CreatePurchaseRequestSchema,
    UpdatePurchaseRequestStatusSchema,
)
from app.clients.subscription import (
    purchase_request_client,
)

purchase_request_router = APIRouter(
    prefix="/purchase-requests",
    tags=["Purchase Requests"]
)


@purchase_request_router.post("/")
def create_purchase_request(
    body: CreatePurchaseRequestSchema,
):
    return purchase_request_client.create(
        user_id=None,
        email=body.email,
        phone_number=body.phone_number,
        target_type=body.target_type,
        target_id=body.target_id,
    )


@purchase_request_router.patch("/{request_id}/status")
def update_status(
    request_id: str,
    body: UpdatePurchaseRequestStatusSchema,
):
    return {
        "success": purchase_request_client.update_status(
            request_id=request_id,
            status=body.status,
        )
    }


@purchase_request_router.get("/")
def list_purchase_requests(
    limit: int = 20,
    offset: int = 0,
):
    return purchase_request_client.list(
        limit=limit,
        offset=offset,
    )
