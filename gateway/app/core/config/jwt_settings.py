
from .base_config import BaseConfig
from pydantic import Field


class JWTSettings(BaseConfig):
    JWT_SECRET_KEY: str = Field(..., min_length=32, description="Secret key for JWT")
    JWT_ALGORITHM: str = Field("HS256", description="JWT encryption algorithm")
