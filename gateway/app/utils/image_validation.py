from fastapi import UploadFile, HTTPException
from app.core.config import settings

ALLOWED_TYPES = {"image/jpeg", "image/png", "image/webp"}
MAX_SIZE = settings.media.STORAGE_MAX_FILE_SIZE_MB * 1024 * 1024  # Convert MB to bytes


async def validate_image(file: UploadFile) -> bytes:
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=400, detail="Invalid image type")

    data = await file.read()

    if len(data) > MAX_SIZE:
        raise HTTPException(status_code=400, detail="Image too large")

    return data