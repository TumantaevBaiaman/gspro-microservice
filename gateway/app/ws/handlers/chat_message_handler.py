from app.ws.connection_manager import manager
from app.clients.chat.chat_message_client import chat_message_client
from grpc import RpcError, StatusCode


async def handle_send_message(sender_id: str, data: dict):

    try:
        res = chat_message_client.send_message(
            sender_id=sender_id,
            chat_id=data.get("chat_id", None),
            text=data.get("text", None),
            chat_type=data.get("chat_type"),
            course_id=data.get("course_id", None),
            student_id=data.get("student_id"),
            peer_id=data.get("peer_id"),
        )

    except RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            await manager.send_to_user(sender_id, {
                "event": "error",
                "code": "NOT_CHAT_PARTICIPANT",
            })
            return

        await manager.send_to_user(sender_id, {
            "event": "error",
            "code": "SEND_MESSAGE_FAILED",
        })
        return

    participants = res.get("participant_ids", [])

    payload = {
        "event": "new_message",
        "chat_id": res["chat_id"],
        "chat_type": data.get("chat_type"),
        "message": {
            "id": res["message_id"],
            "text": data.get("text", ""),
            "sender_id": sender_id,
        }
    }
    await manager.send_to_users(participants, payload)
