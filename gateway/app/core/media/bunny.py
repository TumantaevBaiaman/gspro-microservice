import hashlib
import time

from app.core.config import settings
from app.core.media.base import MediaProvider


class BunnyMediaProvider(MediaProvider):
    def generate_stream_url(
        self,
        video_id: str,
        expires_in_seconds: int = 300,
    ) -> tuple[str, int]:
        expires_at = int(time.time()) + expires_in_seconds

        path = f"/{video_id}/playlist.m3u8"

        token_data = (
            f"{settings.media.BUNNY_VIDEO_SECURITY_KEY}"
            f"{path}"
            f"{expires_at}"
        )
        token = hashlib.sha256(token_data.encode()).hexdigest()

        stream_url = (
            f"https://{settings.media.BUNNY_VIDEO_HOST}"
            f"{path}"
            f"?token={token}&expires={expires_at}"
        )

        return stream_url, expires_at
