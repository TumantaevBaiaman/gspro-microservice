from pymongo import DESCENDING

from src.domain.enums.course.price_type import PriceType
from src.domain.entities.course_entity import CourseEntity
from src.domain.repositories.course_repository import ICourseRepository


class CourseRepository(ICourseRepository):

    async def get_course_by_id(self, course_id: str) -> CourseEntity:
        return await CourseEntity.get(course_id)

    async def list(self, limit: int, offset: int, mode: str, author_id: str =None):
        query = CourseEntity.find()

        if mode == "free":
            query = query.find(
                CourseEntity.price.type == PriceType.FREE.value
            )

        if mode == "recommended":
            query = query.find(
                CourseEntity.is_promoted == True
            )

        if author_id is not None:
            query = query.find(
                CourseEntity.author_id == author_id
            )

        if mode == "popular":
            sort = [
                ("is_promoted", DESCENDING),
                ("created_at", DESCENDING),
            ]
        else:
            sort = [
                ("is_promoted", DESCENDING),
                ("created_at", DESCENDING),
            ]

        total = await query.count()

        items = await (
            query
            .sort(sort)
            .skip(offset)
            .limit(limit)
            .to_list()
        )

        return items, total

