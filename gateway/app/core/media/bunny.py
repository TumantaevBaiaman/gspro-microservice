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

        token_data = (
            f"{settings.media.BUNNY_VIDEO_SECURITY_KEY}"
            f"{video_id}"
            f"{expires_at}"
        )
        token = hashlib.sha256(token_data.encode()).hexdigest()

        embed_url = (
            f"https://iframe.mediadelivery.net/embed/"
            f"{settings.media.BUNNY_VIDEO_LIBRARY_ID}/{video_id}"
            f"?token={token}&expires={expires_at}"
        )

        return embed_url, expires_at
