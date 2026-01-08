from fastapi import WebSocket
import jwt
from app.core.security.auth_jwt import decode_jwt_token


async def authenticate_ws(ws: WebSocket) -> str | None:
    token = ws.query_params.get("token")
    if not token:
        return None

    try:
        payload = decode_jwt_token(token)
    except jwt.PyJWTError:
        return None

    user_id = payload.get("sub")
    if not user_id:
        return None

    return str(user_id)
