import jwt
from fastapi import HTTPException
from app.core.config import settings


def decode_jwt_token(token: str):
    try:
        payload = jwt.decode(
            token,
            settings.jwt.JWT_SECRET_KEY,
            algorithms=[settings.jwt.JWT_ALGORITHM],
        )
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
