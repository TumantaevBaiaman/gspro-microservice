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


async def upload_voice(
    data: bytes,
    content_type: str,
    path_prefix: str,
) -> tuple[str, str]:

    voice_id = str(uuid.uuid4())
    ext = content_type.split("/")[-1]

    path = f"{path_prefix}/{voice_id}.{ext}"

    await _upload_bytes(data, path, content_type)

    url = f"{settings.media.STORAGE_CDN_BASE_URL}/{path}"
    return voice_id, url