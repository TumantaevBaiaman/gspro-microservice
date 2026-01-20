import grpc

from generated.subscription import purchase_request_pb2 as pb2
from generated.subscription import purchase_request_pb2_grpc as pb2_grpc

from src.application.services import (
    PurchaseRequestService,
)
from src.application.commands.purchase_request.dto import (
    CreatePurchaseRequestDTO,
)
from src.application.queries.purchase_request.dto import (
    ListPurchaseRequestsDTO,
)
from src.domain.enums.purchase_request import (
    PurchaseRequestStatus,
    PurchaseTargetType,
)


class PurchaseRequestHandler(
    pb2_grpc.PurchaseRequestServiceServicer
):
    def __init__(self, service: PurchaseRequestService):
        self.service = service

    async def Create(self, request, context):
        dto = CreatePurchaseRequestDTO(
            user_id=request.user_id or None,
            email=request.email,
            phone_number=request.phone_number,
            telegram=request.telegram,
            target_type=PurchaseTargetType(request.target_type),
            target_id=request.target_id,
        )

        try:
            doc = await self.service.create.execute(dto)
        except Exception as e:
            await context.abort(
                grpc.StatusCode.INTERNAL,
                str(e),
            )

        return pb2.CreatePurchaseRequestResponse(
            request_id=str(doc.id)
        )

    async def List(self, request, context):
        dto = ListPurchaseRequestsDTO(
            limit=request.limit,
            offset=request.offset,
        )

        try:
            items, total = await self.service.list.execute(dto)
        except Exception as e:
            await context.abort(
                grpc.StatusCode.INTERNAL,
                str(e),
            )

        return pb2.ListPurchaseRequestsResponse(
            items=[self._map_request(item) for item in items],
            total=total,
        )

    async def UpdateStatus(self, request, context):
        try:
            success = await self.service.update_status.execute(
                request_id=request.request_id,
                status=PurchaseRequestStatus(request.status),
            )
        except Exception as e:
            await context.abort(
                grpc.StatusCode.INTERNAL,
                str(e),
            )

        return pb2.UpdatePurchaseRequestStatusResponse(
            success=success
        )

    @staticmethod
    def _map_request(doc):
        return pb2.PurchaseRequest(
            id=str(doc.id),
            user_id=doc.user_id or "",
            email=doc.email,
            phone_number=doc.phone_number,
            telegram=doc.telegram,
            target_type=doc.target_type.value,
            target_id=doc.target_id,
            status=doc.status.value,
        )
