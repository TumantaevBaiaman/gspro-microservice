from app.clients.course.category_client import CategoryClient
from app.clients.media.media_client import MediaClient
from app.clients.review.course_review import ReviewClient


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


def enrich_course(
    *,
    course: dict,
    media_client: MediaClient,
    review_client: ReviewClient,
    category_client: CategoryClient,
    include_cover: bool = True,
    include_rating: bool = True,
    include_categories: bool = True,
) -> dict:

    if include_cover:
        cover_id = course.get("cover_image_id")
        if cover_id:
            media = media_client.get_media(media_id=cover_id)
            course["cover_image"] = media.get("original_url") if media else None
        else:
            course["cover_image"] = None

    if include_rating:
        rating = review_client.get_course_rating(course["id"])
        course["rating"] = {
            "average_rating": rating.get("average_rating"),
            "count": rating.get("reviews_count"),
        }

    if include_categories:
        category_ids = list(set(course.get("category_ids", [])))

        if category_ids:
            categories = category_client.get_categories_by_ids(category_ids)
            course["categories"] = categories
        else:
            course["categories"] = []

    return course

