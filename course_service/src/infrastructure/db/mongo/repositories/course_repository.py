from typing import Iterable, List

from beanie.odm.operators.find.comparison import In
from bson import ObjectId
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

    async def list_by_ids(
        self,
        course_ids,
    ) -> List[CourseEntity]:

        if isinstance(course_ids, (str, ObjectId)):
            course_ids = [course_ids]

        normalized_ids: list[ObjectId] = []
        for cid in course_ids:
            if isinstance(cid, ObjectId):
                normalized_ids.append(cid)
            else:
                normalized_ids.append(ObjectId(str(cid)))

        if not normalized_ids:
            return []

        items = await (
            CourseEntity.find(
                In(CourseEntity.id, normalized_ids)
            )
            .to_list()
        )

        return items

