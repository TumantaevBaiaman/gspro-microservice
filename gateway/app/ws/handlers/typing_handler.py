from app.ws.connection_manager import manager
from app.clients.chat.chat_message_client import chat_message_client


async def handle_typing(sender_id: str, data: dict):
    chat_id = data.get("chat_id")
    if not chat_id:
        return

    res = await chat_message_client.get_chat_participants(
        chat_id=chat_id,
    )

    participants = [
        uid for uid in res.participant_ids
        if uid != sender_id
    ]

    payload = {
        "event": "typing",
        "chat_id": chat_id,
        "user_id": sender_id,
    }

    await manager.send_to_users(participants, payload)
