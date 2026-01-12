from pymongo import DESCENDING

from src.domain.entities.course_entity import CourseEntity
from src.domain.repositories.course_repository import ICourseRepository


class CourseRepository(ICourseRepository):

    async def get_course_by_id(self, course_id: str) -> CourseEntity:
        return await CourseEntity.get(course_id)

    async def list(self, limit: int, offset: int):
        query = CourseEntity.find()

        total = await query.count()

        items = await (
            query
            .sort([
                ("is_promoted", DESCENDING),
                ("created_at", DESCENDING),
            ])
            .skip(offset)
            .limit(limit)
            .to_list()
        )

        return items, total

