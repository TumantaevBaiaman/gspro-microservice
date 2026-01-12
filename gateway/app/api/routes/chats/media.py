from fastapi import APIRouter, UploadFile, File

from app.clients.media import media_client
from app.services.media.image_upload_service import upload_image
from app.services.media.thumbnail_service import create_thumbnails
from app.utils.file_validation import validate_file
from app.utils.image_validation import validate_image
from app.services.media.file_upload_service import upload_file
from app.services.media.voice_upload_service import upload_voice
from app.utils.validate_voice import validate_voice

chat_media_router = APIRouter(prefix="/chat/media", tags=["Chat Media"])


@chat_media_router.post(
    "/upload/image",
    summary="Upload chat media image",
    description="Endpoint to upload a chat media image."
)
async def upload_image_endpoint(file: UploadFile = File(...),):
    image_bytes = await validate_image(file)

    thumbnails = create_thumbnails(image_bytes)

    _, urls = await upload_image(
        original=image_bytes,
        thumbnails=thumbnails,
        path_prefix="chat/uploads/images",
    )

    media = media_client.create_media(
        kind="image",
        usage="message",
        original_url=urls["original"],
        metadata={
            "filename": file.filename,
            "thumb_small_url": urls.get("small"),
            "thumb_medium_url": urls.get("medium"),
        },
    )

    return {
        "id": media["id"],
        "url": media["original_url"],
        "kind": media["kind"],
    }

@chat_media_router.post(
    "/upload/voice",
    summary="Upload chat voice message",
    description="Endpoint to upload a chat voice message."
)
async def upload_voice_endpoint(
    file: UploadFile = File(...),
):
    voice_bytes = await validate_voice(file)

    file_id, url = await upload_voice(
        data=voice_bytes,
        content_type=file.content_type or "audio/ogg",
        path_prefix="chat/uploads/voice",
    )

    media = media_client.create_media(
        kind="audio",
        usage="message",
        original_url=url,
        metadata={
            "filename": file.filename or "",
            "mime_type": file.content_type or "",
        },
    )

    return {
        "id": media["id"],
        "file_id": file_id,
        "url": url,
        "kind": media["kind"],
    }

@chat_media_router.post(
    "/upload/file",
    summary="Upload chat file",
    description="Endpoint to upload a chat file (pdf, doc, docx)."
)
async def upload_file_endpoint(
    file: UploadFile = File(...),
):
    file_bytes = await validate_file(file)

    file_id, url = await upload_file(
        data=file_bytes,
        filename=file.filename,
        content_type=file.content_type,
        path_prefix="chat/uploads/files",
    )

    media = media_client.create_media(
        kind="file",
        usage="message",
        original_url=url,
        metadata={
            "filename": file.filename,
            "mime_type": file.content_type,
            "size": str(len(file_bytes)),
        },
    )

    return {
        "id": media["id"],
        "file_id": file_id,
        "url": url,
        "kind": media["kind"],
        "filename": file.filename,
        "size": len(file_bytes),
    }