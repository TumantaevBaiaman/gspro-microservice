
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    APP_NAME: str = Field("Subscription Service", description="Application name")
    GRPC_HOST: str = Field("0.0.0.0", description="Service host")
    GRPC_PORT: int = Field(50057, description="Service port")

    MONGO_URL: str = Field(..., description="MongoDB connection URL")
    MONGO_DB_NAME: str = Field(..., description="MongoDB database name")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore"
    )


settings = Settings()