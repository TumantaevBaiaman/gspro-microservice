from typing import Protocol, Tuple


class MediaProvider(Protocol):
    def generate_stream_url(
        self,
        video_id: str,
        expires_in_seconds: int = 300,
    ) -> Tuple[str, int]:
        ...
