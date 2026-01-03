import grpc
from fastapi import HTTPException
from google.protobuf.json_format import MessageToDict

from generated.chat import chat_message_pb2 as pb2
from generated.chat import chat_message_pb2_grpc as pb2_grpc


class ChatClient:
    def __init__(self):
        self.channel = grpc.insecure_channel("chat_service:50055")
        self.stub = pb2_grpc.ChatMessageServiceStub(self.channel)

    def send_message(
        self,
        *,
        scope: int,
        sender_id: str,
        participants: list[dict],
        payload: dict,
        course_id: str | None = None,
        context: dict | None = None,
    ) -> dict:
        try:
            res = self.stub.SendMessage(
                pb2.SendMessageRequest(
                    scope=scope,
                    sender_id=sender_id,
                    participants=[
                        pb2.ChatParticipant(
                            user_id=p["user_id"],
                            role=p["role"],
                        )
                        for p in participants
                    ],
                    course_id=course_id or "",
                    payload=pb2.ChatMessagePayload(
                        type=payload["type"],
                        text=payload.get("text", ""),
                    ),
                    context=self._map_context(context),
                ),
                timeout=3.0,
            )

            return {
                "chat": MessageToDict(
                    res.chat,
                    preserving_proto_field_name=True,
                ),
                "message": MessageToDict(
                    res.message,
                    preserving_proto_field_name=True,
                ),
            }

        except grpc.RpcError as e:
            self._err(e)

    def list_messages(
        self,
        *,
        chat_id: str,
        limit: int,
        offset: int,
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
    def _map_context(context: dict | None):
        if not context:
            return pb2.ChatMessageContext()

        reference = context.get("reference")
        if not reference:
            return pb2.ChatMessageContext(
                reply_to_message_id=context.get(
                    "reply_to_message_id", ""
                )
            )

        return pb2.ChatMessageContext(
            reply_to_message_id=context.get(
                "reply_to_message_id", ""
            ),
            reference=pb2.MessageReference(
                type=reference["type"],
                id=reference["id"],
            ),
        )

    @staticmethod
    def _err(e: grpc.RpcError):
        code = e.code()
        msg = e.details()

        if code == grpc.StatusCode.NOT_FOUND:
            raise HTTPException(404, msg)

        if code == grpc.StatusCode.ALREADY_EXISTS:
            raise HTTPException(409, msg)

        raise HTTPException(400, msg)


chat_message_client = ChatClient()
