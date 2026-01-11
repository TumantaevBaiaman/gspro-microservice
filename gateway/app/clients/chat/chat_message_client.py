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
        sender_id: str,
        chat_id: str | None,
        chat_type: str | None,
        course_id: str | None,
        student_id: str | None,
        peer_id: str | None,

        message_type: str,
        text: str | None = None,
        attachments: list[dict] | None = None,
    ) -> dict:

        attachments = attachments or []

        grpc_attachments = [
            pb2.ChatAttachment(
                file_id=a.get("file_id", ""),
                url=a.get("url", ""),
                mime_type=a.get("mime_type", ""),
                size=int(a.get("size", 0)),
                duration=int(a.get("duration", 0)),
            )
            for a in attachments
        ]

        try:

            request = pb2.SendMessageRequest(
                sender_id=sender_id,
                chat_id=chat_id or "",
                chat_type=chat_type or "",
                course_id=course_id or "",
                student_id=student_id or "",
                peer_id=peer_id or "",

                type=message_type,

                text=text or "",
                attachments=grpc_attachments,
            )

            res = self.stub.SendMessage(request, timeout=3.0)

            return MessageToDict(
                res,
                preserving_proto_field_name=True,
            )

        except grpc.RpcError as e:
            self._err(e)

    def list_messages(
            self,
            *,
            chat_id: str,
            limit: int = 10,
            offset: int = 0,
    ) -> dict:
        try:
            res = self.stub.ListMessages(
                pb2.ListMessagesRequest(
                    chat_id=chat_id,
                    limit=limit,
                    offset=offset,
                ),
                timeout=3.0,
            )

            return MessageToDict(
                res,
                preserving_proto_field_name=True,
            )

        except grpc.RpcError as e:
            print(e)
            self._err(e)

    @staticmethod
    def _err(e: grpc.RpcError):
        code = e.code()
        msg = e.details()

        if code == grpc.StatusCode.NOT_FOUND:
            raise HTTPException(404, msg)

        if code == grpc.StatusCode.INVALID_ARGUMENT:
            raise HTTPException(400, msg)

        if code == grpc.StatusCode.PERMISSION_DENIED:
            raise HTTPException(403, msg)

        raise HTTPException(500, msg)


chat_message_client = ChatMessageClient()
