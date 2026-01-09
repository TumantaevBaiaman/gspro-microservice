import jwt
from datetime import datetime, timedelta
from src.core.config import settings


def create_access_token(user_id: str, role: str):
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {"sub": user_id, "exp": expire, "type": "access", "role": role}
    return jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)


def create_refresh_token(user_id: str, role: str):
    expire = datetime.utcnow() + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    payload = {"sub": user_id, "exp": expire, "type": "refresh", "role": role}
    return jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)


def verify_refresh_token(token: str):
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM]
        )

        if payload.get("type") != "refresh":
            raise ValueError("Token is not a refresh token")

        return payload

    except jwt.ExpiredSignatureError:
        raise ValueError("Refresh token expired")
    except jwt.InvalidTokenError:
        raise ValueError("Invalid refresh token")
