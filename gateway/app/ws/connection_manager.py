from typing import Dict, Iterable
from starlette.websockets import WebSocket, WebSocketState
import asyncio

from app.core.logging import logger


class ConnectionManager:
    def __init__(self):
        self._connections: Dict[str, WebSocket] = {}
        self._lock = asyncio.Lock()

    async def connect(self, user_id: str, ws: WebSocket) -> None:
        async with self._lock:
            old_ws = self._connections.get(user_id)
            if old_ws and old_ws.client_state == WebSocketState.CONNECTED:
                try:
                    await old_ws.close(code=1000)
                except Exception:
                    pass

            self._connections[user_id] = ws
            logger.debug(f"WS connected: user_id={user_id}", user_id)

    async def disconnect(self, user_id: str) -> None:
        async with self._lock:
            self._connections.pop(user_id, None)
            logger.debug("WS disconnected: user_id=%s", user_id)

    async def send_to_user(self, user_id: str, payload: dict) -> bool:
        ws = self._connections.get(user_id)
        if not ws:
            return False

        if ws.client_state != WebSocketState.CONNECTED:
            await self.disconnect(user_id)
            return False

        try:
            await ws.send_json(payload)
            return True
        except Exception:
            await self.disconnect(user_id)
            return False

    async def send_to_users(
        self,
        user_ids: Iterable[str],
        payload: dict,
    ) -> None:
        for uid in user_ids:
            await self.send_to_user(uid, payload)

    def is_online(self, user_id: str) -> bool:
        ws = self._connections.get(user_id)
        return bool(ws and ws.client_state == WebSocketState.CONNECTED)

    def online_users(self) -> list[str]:
        return [
            uid
            for uid, ws in self._connections.items()
            if ws.client_state == WebSocketState.CONNECTED
        ]

manager = ConnectionManager()