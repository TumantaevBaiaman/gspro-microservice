import grpc
from fastapi import HTTPException
from google.protobuf.json_format import MessageToDict

from generated.subscription import purchase_request_pb2 as pb2
from generated.subscription import purchase_request_pb2_grpc as pb2_grpc


class PurchaseRequestClient:
    def __init__(self):
        self.channel = grpc.insecure_channel(
            "subscription_service:50057"
        )
        self.stub = pb2_grpc.PurchaseRequestServiceStub(
            self.channel
        )

    def create(
        self,
        *,
        user_id: str | None,
        email: str,
        phone_number: str,
        target_type: str,
        target_id: str,
    ) -> dict:
        try:
            res = self.stub.Create(
                pb2.CreatePurchaseRequestRequest(
                    user_id=user_id or "",
                    email=email,
                    phone_number=phone_number,
                    target_type=target_type,
                    target_id=target_id,
                ),
                timeout=3.0,
            )

            return {"request_id": res.request_id}

        except grpc.RpcError as e:
            self._err(e)

    def list(
        self,
        *,
        limit: int,
        offset: int,
    ) -> dict:
        try:
            res = self.stub.List(
                pb2.ListPurchaseRequestsRequest(
                    limit=limit,
                    offset=offset,
                ),
                timeout=3.0,
            )

            return {
                "items": [
                    MessageToDict(
                        item,
                        preserving_proto_field_name=True,
                    )
                    for item in res.items
                ],
                "total": res.total,
            }

        except grpc.RpcError as e:
            self._err(e)

    def update_status(
        self,
        *,
        request_id: str,
        status: str,
    ) -> bool:
        try:
            res = self.stub.UpdateStatus(
                pb2.UpdatePurchaseRequestStatusRequest(
                    request_id=request_id,
                    status=status,
                ),
                timeout=3.0,
            )

            return res.success

        except grpc.RpcError as e:
            self._err(e)

    @staticmethod
    def _err(e: grpc.RpcError):
        code = e.code()
        msg = e.details()

        if code == grpc.StatusCode.NOT_FOUND:
            raise HTTPException(404, msg)

        if code == grpc.StatusCode.ALREADY_EXISTS:
            raise HTTPException(409, msg)

        raise HTTPException(400, msg)


purchase_request_client = PurchaseRequestClient()
