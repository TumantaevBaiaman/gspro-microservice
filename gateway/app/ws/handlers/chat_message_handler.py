from app.clients.media import media_client
from app.ws.connection_manager import manager
from app.clients.chat.chat_message_client import chat_message_client
from grpc import RpcError, StatusCode


async def handle_send_message(sender_id: str, data: dict):
    payload = data.get("payload") or {}
    attachments = payload.get("attachments", [])

    context = None
    ctx = data.get("context")

    if ctx:
        ref = ctx.get("reference")
        if ref:
            ref_type = ref.get("type")
            ref_id = ref.get("id")

            if not ref_type or not ref_id:
                await manager.send_to_user(sender_id, {
                    "event": "error",
                    "code": "INVALID_CONTEXT",
                    "message": "reference.type and reference.id are required",
                })
                return

            context = {
                "reference": {
                    "type": ref_type,
                    "id": ref_id,
                }
            }

        if ctx.get("reply_to_message_id"):
            context = context or {}
            context["reply_to_message_id"] = ctx["reply_to_message_id"]

    try:
        res = chat_message_client.send_message(
            sender_id=sender_id,
            chat_id=data.get("chat_id"),
            chat_type=data.get("chat_type"),
            course_id=data.get("course_id"),
            student_id=data.get("student_id"),
            peer_id=data.get("peer_id"),

            message_type=payload.get("type"),
            text=payload.get("text"),
            attachments=attachments,
            context=context,
        )

    except RpcError as e:
        code = (
            "NOT_CHAT_PARTICIPANT"
            if e.code() == StatusCode.PERMISSION_DENIED
            else "SEND_MESSAGE_FAILED"
        )
        await manager.send_to_user(sender_id, {
            "event": "error",
            "code": code,
        })
        return

    participants = res.get("participant_ids", [])

    if attachments:
        for attachment in attachments:
            media_client.attach_media(
                owner_service="chat",
                owner_id=res["chat_id"],
                media_id=attachment["file_id"],
            )

    ws_message = {
        "event": "new_message",
        "chat_id": res["chat_id"],
        "chat_type": data.get("chat_type"),
        "message": {
            "id": res["message_id"],
            "sender_id": sender_id,
            "type": payload.get("type"),
            "text": payload.get("text"),
            "attachments": payload.get("attachments", []),
            "context": context,
        }
    }

    await manager.send_to_users(participants, ws_message)
