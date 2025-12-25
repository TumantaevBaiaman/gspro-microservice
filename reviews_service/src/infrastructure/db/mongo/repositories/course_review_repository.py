from src.domain.repositories.course_review_repository import (
    ICourseReviewRepository,
)
from src.infrastructure.db.mongo.models.course_review import CourseReviewDocument


class CourseReviewRepository(ICourseReviewRepository):

    async def create(
        self,
        *,
        course_id: str,
        user_id: str,
        rating: int,
        comment: str,
        tags: list[str],
    ) -> CourseReviewDocument:
        doc = CourseReviewDocument(
            course_id=course_id,
            user_id=user_id,
            rating=rating,
            comment=comment,
            tags=tags,
        )
        await doc.insert()
        return doc

    async def list_by_course(
        self,
        *,
        course_id: str,
        limit: int,
        offset: int,
    ):
        query = CourseReviewDocument.find(
            CourseReviewDocument.course_id == course_id
        )

        total = await query.count()

        items = await (
            query
            .skip(offset)
            .limit(limit)
            .to_list()
        )

        return items, total

    async def exists_by_user_and_course(
        self,
        *,
        course_id: str,
        user_id: str,
    ) -> bool:
        return await CourseReviewDocument.find(
            CourseReviewDocument.course_id == course_id,
            CourseReviewDocument.user_id == user_id,
        ).exists()

    async def get_course_rating(
        self,
        *,
        course_id: str,
    ):
        pipeline = [
            {"$match": {"course_id": course_id}},
            {
                "$group": {
                    "_id": None,
                    "avg_rating": {"$avg": "$rating"},
                    "count": {"$sum": 1},
                }
            },
        ]

        result = await CourseReviewDocument.aggregate(pipeline).to_list()

        if not result:
            return 0.0, 0

        return float(result[0]["avg_rating"]), int(result[0]["count"])
