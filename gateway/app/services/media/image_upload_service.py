import uuid
import aiohttp
from app.core.config import settings


async def _upload_bytes(data: bytes, path: str, content_type: str):
    upload_url = (
        f"{settings.media.STORAGE_ENDPOINT}/"
        f"{settings.media.STORAGE_ZONE}/"
        f"{path}"
    )

    headers = {
        "AccessKey": settings.media.STORAGE_API_KEY,
        "Content-Type": content_type,
    }

    async with aiohttp.ClientSession() as session:
        async with session.put(upload_url, data=data, headers=headers) as resp:
            if resp.status != 201:
                error_text = await resp.text()
                raise RuntimeError(
                    f"Bunny upload failed "
                    f"(status={resp.status}, body={error_text})"
                )


async def upload_image(
    original: bytes,
    thumbnails: dict[str, bytes],
    path_prefix: str,
) -> tuple[str, dict[str, str]]:

    image_id = str(uuid.uuid4())

    base_path = f"{path_prefix}/{image_id}"

    urls: dict[str, str] = {}

    original_path = f"{base_path}/original.jpg"
    await _upload_bytes(original, original_path, "image/jpeg")
    urls["original"] = f"{settings.media.STORAGE_CDN_BASE_URL}/{original_path}"

    for name, data in thumbnails.items():
        thumb_path = f"{base_path}/thumb_{name}.jpg"
        await _upload_bytes(data, thumb_path, "image/jpeg")
        urls[name] = f"{settings.media.STORAGE_CDN_BASE_URL}/{thumb_path}"

    return image_id, urls
