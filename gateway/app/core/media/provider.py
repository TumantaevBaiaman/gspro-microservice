from app.core.media.bunny import BunnyMediaProvider
from app.core.media.base import MediaProvider


def get_media_provider() -> MediaProvider:
    return BunnyMediaProvider()
