from PIL import Image
from io import BytesIO

THUMB_SIZES = {
    "small": (64, 64),
    "medium": (128, 128),
}


def create_thumbnails(image_bytes: bytes) -> dict[str, bytes]:
    image = Image.open(BytesIO(image_bytes)).convert("RGB")
    thumbnails: dict[str, bytes] = {}

    for name, size in THUMB_SIZES.items():
        img = image.copy()
        img.thumbnail(size)

        buffer = BytesIO()
        img.save(buffer, format="JPEG", quality=85)
        thumbnails[name] = buffer.getvalue()

    return thumbnails