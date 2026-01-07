import grpc
from fastapi import HTTPException
from google.protobuf.json_format import MessageToDict

from generated.chat import chat_message_pb2 as pb2
from generated.chat import chat_message_pb2_grpc as pb2_grpc


class ChatMessageClient:
    def __init__(self):
        self.channel = grpc.insecure_channel("chat_service:50055")
        self.stub = pb2_grpc.ChatMessageServiceStub(self.channel)

    def send_message(
        self,
        *,
        chat_id: str | None,
        chat_type: str,
        course_id: str | None,
        student_id: str | None,
        peer_id: str | None,
        sender_id: str,
        text: str,
    ) -> dict:
        try:
            res = self.stub.SendMessage(
                pb2.SendMessageRequest(
                    chat_id=chat_id or "",
                    chat_type=chat_type,
                    course_id=course_id or "",
                    student_id=student_id or "",
                    peer_id=peer_id or "",
                    sender_id=sender_id,
                    text=text,
                ),
                timeout=3.0,
            )

            return MessageToDict(
                res,
                preserving_proto_field_name=True,
            )

        except grpc.RpcError as e:
            self._err(e)

    @staticmethod
    def _err(e: grpc.RpcError):
        code = e.code()
        msg = e.details()

        if code == grpc.StatusCode.NOT_FOUND:
            raise HTTPException(404, msg)

        if code == grpc.StatusCode.INVALID_ARGUMENT:
            raise HTTPException(400, msg)

        raise HTTPException(500, msg)


chat_message_client = ChatMessageClient()
