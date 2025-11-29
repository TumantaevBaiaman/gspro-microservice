from src.domain.dto import CourseCreateDTO
from src.domain.entities.course_entity import CourseEntity


class CourseRepository:
    async def create_course(self, dto: CourseCreateDTO) -> CourseEntity:
        course = CourseEntity(**dto.dict())
        return await course.insert()

    async def get_course_by_id(self, course_id: str) -> CourseEntity:
        return await CourseEntity.get(course_id)