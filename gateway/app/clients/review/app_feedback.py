import grpc
from fastapi import HTTPException
from google.protobuf.json_format import MessageToDict

from generated.reviews import app_feedback_pb2 as pb2
from generated.reviews import app_feedback_pb2_grpc as pb2_grpc


class AppFeedbackClient:
    def __init__(self):
        self.channel = grpc.insecure_channel("reviews_service:50053")
        self.stub = pb2_grpc.AppFeedbackServiceStub(self.channel)

    def create_feedback(
        self,
        *,
        user_id: str,
        message: str,
        type: str = "feedback",
        is_public: bool = False,
    ) -> dict:
        try:
            res = self.stub.CreateFeedback(
                pb2.CreateFeedbackRequest(
                    user_id=user_id,
                    message=message,
                    type=type,
                    is_public=is_public,
                ),
                timeout=3.0,
            )

            return MessageToDict(
                res.feedback,
                preserving_proto_field_name=True,
            )

        except grpc.RpcError as e:
            self._err(e)

    def list_feedback(
        self,
        *,
        limit: int,
        offset: int,
    ) -> dict:
        try:
            res = self.stub.ListFeedback(
                pb2.ListFeedbackRequest(
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

    @staticmethod
    def _err(e: grpc.RpcError):
        code = e.code()
        msg = e.details()

        if code == grpc.StatusCode.NOT_FOUND:
            raise HTTPException(404, msg)

        raise HTTPException(400, msg)


app_feedback_client = AppFeedbackClient()
