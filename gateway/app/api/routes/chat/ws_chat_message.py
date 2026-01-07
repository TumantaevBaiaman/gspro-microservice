from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends

from app.clients.chat.chat_message_client import chat_message_client
from app.api.dependencies.auth import get_current_user

ws_chat_router = APIRouter()


@ws_chat_router.websocket("/ws/chat/messages")
async def chat_message_ws(
    websocket: WebSocket,
):
    print("WS HANDLER HIT")
    await websocket.accept()

    try:
        while True:
            data = await websocket.receive_json()

            """
            Ожидаемый payload от клиента:

            {
              "chat_id": "optional",
              "chat_type": "course_private | course_group | direct",
              "course_id": "optional",
              "student_id": "optional",
              "peer_id": "optional",
              "text": "hello"
            }
            """

            res = chat_message_client.send_message(
                chat_id=data.get("chat_id"),
                chat_type=data["chat_type"],
                course_id=data.get("course_id"),
                student_id=data.get("student_id"),
                peer_id=data.get("peer_id"),
                sender_id=user.id,
                text=data["text"],
            )

            await websocket.send_json(
                {
                    "event": "message_sent",
                    "data": res,
                }
            )

    except WebSocketDisconnect:
        pass

@ws_chat_router.websocket("/test")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")


