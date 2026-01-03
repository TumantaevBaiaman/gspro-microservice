from fastapi import APIRouter, UploadFile, File, Form, HTTPException

from app.clients.media import media_client
from app.services.media.image_upload_service import upload_image
from app.services.media.thumbnail_service import create_thumbnails
from app.utils.image_validation import validate_image

router = APIRouter(prefix="/media", tags=["Media"])


@router.post("/upload")
async def upload_media(
    file: UploadFile = File(...),
):
    image_bytes = await validate_image(file)

    thumbnails = create_thumbnails(image_bytes)

    _, urls = await upload_image(
        original=image_bytes,
        thumbnails=thumbnails,
        path_prefix="users/avatar",
    )

    media = media_client.create_media(
        kind="image",
        usage="cover",
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
        "usage": media.get("usage"),
    }

