
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    APP_NAME: str = Field("User Service", description="Application name")
    GRPC_HOST: str = Field("0.0.0.0", description="Service host")
    GRPC_PORT: int = Field(50051, description="Service port")

    DB_HOST: str = Field(..., description="PostgreSQL host")
    DB_PORT: int = Field(5432, description="PostgreSQL port")
    DB_USER: str = Field(..., description="PostgreSQL user")
    DB_PASSWORD: str = Field(..., description="PostgreSQL password")
    DB_NAME: str = Field("users_db", description="Database name for the service")

    @property
    def SYNC_DATABASE_URL(self) -> str:
        return (
            f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    @property
    def ASYNC_DATABASE_URL(self) -> str:
        return (
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore"
    )