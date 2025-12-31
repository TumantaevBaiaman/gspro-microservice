from app.clients.media.media_client import MediaClient


def enrich_courses_with_cover(
    *,
    courses: list[dict],
    media_client: MediaClient,
) -> list[dict]:

    media_ids = [
        c["cover_image_id"]
        for c in courses
        if c.get("cover_image_id")
    ]

    if not media_ids:
        return courses

    media_items = media_client.get_media_batch(
        media_ids=list(set(media_ids))
    )

    media_map = {m["id"]: m for m in media_items}

    for course in courses:
        cover_id = course.get("cover_image_id")
        course["cover_image"] = media_map.get(cover_id)["metadata"]["thumb_medium_url"] if cover_id and cover_id in media_map else None

    return courses


from app.clients.media.media_client import MediaClient


def enrich_course_with_cover(
    *,
    course: dict,
    media_client: MediaClient,
) -> dict:

    cover_id = course.get("cover_image_id")
    if not cover_id:
        course["cover_image"] = None
        return course

    media = media_client.get_media(media_id=cover_id)

    course["cover_image"] = (
        media.get("original_url", {})
        if media else None
    )

    return course

