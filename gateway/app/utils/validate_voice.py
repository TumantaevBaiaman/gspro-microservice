from fastapi import UploadFile, HTTPException

ALLOWED_MIME_TYPES = {
    "audio/ogg",
    "audio/mpeg",
    "audio/webm",
    "audio/wav",
}

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB


async def validate_voice(file: UploadFile) -> bytes:
    if file.content_type not in ALLOWED_MIME_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Unsupported audio format",
        )

    data = await file.read()

    if len(data) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail="Voice message is too large",
        )

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="Filename is required",
        )

    return data
