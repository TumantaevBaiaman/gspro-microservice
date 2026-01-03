from fastapi import FastAPI, APIRouter, Depends, Query, UploadFile, File, HTTPException

from app.api.dependencies.auth import get_current_user
from app.clients.media import media_client
from app.services.media.image_upload_service import upload_image
from app.services.media.thumbnail_service import create_thumbnails
from app.utils.image_validation import validate_image

user_portfolio_router = APIRouter(prefix="/users/me/portfolio", tags=["User Portfolio"])


@user_portfolio_router.get(
    "/",
    summary="Get Current User Portfolio",
    description="Endpoint to retrieve the portfolio information of the currently authenticated user."
)
async def get_user_portfolio(user=Depends(get_current_user)):
    user_id = user.get("sub")
    portfolio_items = media_client.list_media_by_owner(
        owner_service="user",
        owner_id=user_id,
        usage="portfolio",
        kind="image",
    )
    return [portfolio_items_item for portfolio_items_item in portfolio_items]


@user_portfolio_router.post(
    "/upload",
    summary="Upload User Portfolio Item",
    description="Endpoint to upload a new item to the user's portfolio."
)
async def upload_portfolio_item(file: UploadFile = File(...), user=Depends(get_current_user)):
    user_id = user.get("sub")
    image_bytes = await validate_image(file)

    thumbnails = create_thumbnails(image_bytes)

    _, urls = await upload_image(
        original=image_bytes,
        thumbnails=thumbnails,
        path_prefix="users/portfolio",
    )

    media = media_client.create_and_attach_media(
        owner_service="user",
        owner_id=user_id,
        kind="image",
        usage="portfolio",
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
