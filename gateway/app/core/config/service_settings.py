
from .base_config import BaseConfig
from pydantic import Field


class ServiceSettings(BaseConfig):
    USER_SERVICE_HOST: str = Field(..., description="UserService host")
    USER_SERVICE_PORT: int = Field(..., description="UserService port")
