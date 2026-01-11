from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends, HTTPException

from app.api.ws.ws_auth import authenticate_ws
from app.ws.connection_manager import manager
from app.ws.handlers.chat_message_handler import handle_send_message
from app.ws.handlers.typing_handler import handle_typing

ws_chat_router = APIRouter()

@ws_chat_router.websocket("/ws/chats")
async def ws_chat(ws: WebSocket):
    user_id = await authenticate_ws(ws)
    if not user_id:
        await ws.close(code=1008)
        return

    await ws.accept()
    await manager.connect(user_id, ws)

    try:
        while True:
            data = await ws.receive_json()

            action = data.get("action")
            if not action:
                await ws.send_json({
                    "event": "error",
                    "code": "NO_ACTION",
                })
                continue

            if action == "send_message":
                await handle_send_message(user_id, data)

            elif action == "typing":
                await handle_typing(user_id, data)

            else:
                await ws.send_json({
                    "event": "error",
                    "code": "UNKNOWN_ACTION",
                })

    except WebSocketDisconnect:
        await manager.disconnect(user_id)


