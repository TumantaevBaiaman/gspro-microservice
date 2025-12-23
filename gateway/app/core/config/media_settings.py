
from .base_config import BaseConfig
from pydantic import Field


class MediaSettings(BaseConfig):
    # ===== IMAGES / FILE STORAGE =====
    STORAGE_PROVIDER: str = Field(..., description="Storage service provider name")

    STORAGE_ENDPOINT: str = Field(..., description="Storage service endpoint URL")
    STORAGE_ZONE: str = Field(..., description="Storage service zone or bucket name")
    STORAGE_API_KEY: str = Field(..., description="API key for storage service authentication")
    STORAGE_CDN_BASE_URL: str = Field(..., description="Base URL for CDN access to stored media")
    STORAGE_MAX_FILE_SIZE_MB: int = Field(5, description="Maximum file size for uploads in megabytes")

    BUNNY_VIDEO_LIBRARY_ID: str = Field(..., description="Bunny video library identifier")
    BUNNY_VIDEO_SECURITY_KEY: str = Field(..., description="Security key for Bunny video service")

