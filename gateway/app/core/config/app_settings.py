
from .base_config import BaseConfig
from pydantic import Field


class AppSettings(BaseConfig):
    APP_NAME: str = Field("Gateway Service", description="Application name")
    APP_PORT: int = Field(8000, description="Application port")
