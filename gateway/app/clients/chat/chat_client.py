import grpc
from fastapi import HTTPException
from google.protobuf.json_format import MessageToDict

from generated.chat import chat_pb2 as pb2
from generated.chat import chat_pb2_grpc as pb2_grpc


class ChatClient:
    def __init__(self):
        self.channel = grpc.insecure_channel("chat_service:50055")
        self.stub = pb2_grpc.ChatServiceStub(self.channel)

    def get_or_create(
        self,
        *,
        chat_type: str,
        sender_id: str | None = None,
        peer_id: str | None = None,
        course_id: str | None = None,
        student_id: str | None = None,
    ) -> dict:
        try:
            res = self.stub.GetOrCreateChat(
                pb2.GetOrCreateChatRequest(
                    chat_type=chat_type,
                    sender_id=sender_id or "",
                    peer_id=peer_id or "",
                    course_id=course_id or "",
                    student_id=student_id or "",
                ),
                timeout=3.0,
            )

            return MessageToDict(
                res,
                preserving_proto_field_name=True,
            )

        except grpc.RpcError as e:
            self._err(e)

    def get(self, chat_id: str) -> dict:
        try:
            res = self.stub.GetChat(
                pb2.GetChatRequest(chat_id=chat_id),
                timeout=3.0,
            )

            return MessageToDict(
                res,
                preserving_proto_field_name=True,
            )

        except grpc.RpcError as e:
            self._err(e)

    def list_user_chats(
            self,
            *,
            user_id: str,
            chat_type: str | None = None,
            limit: int = 20,
            offset: int = 0,
    ) -> dict:
        try:
            res = self.stub.ListUserChats(
                pb2.ListUserChatsRequest(
                    user_id=user_id,
                    chat_type=chat_type or "",
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
            self._err(e)

    def list_chat_participants(
            self,
            *,
            chat_id: str,
    ) -> dict:
        try:
            res = self.stub.ListChatParticipants(
                pb2.ListChatParticipantsRequest(chat_id=chat_id),
                timeout=3.0,
            )

            return MessageToDict(
                res,
                preserving_proto_field_name=True,
            )

        except grpc.RpcError as e:
            self._err(e)

    def list_private_chat_peers(
            self,
            *,
            course_id: str,
            me_id: str,
    ) -> list[str]:
        try:
            res = self.stub.ListPrivateChatPeers(
                pb2.ListPrivateChatPeersRequest(
                    course_id=course_id,
                    me_id=me_id,
                ),
                timeout=3.0,
            )

            data = MessageToDict(
                res,
                preserving_proto_field_name=True,
            )

            return data.get("peer_ids", [])

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

        raise HTTPException(500, msg)


chat_client = ChatClient()
