from src.domain.dto.course_dto import CourseCreateDTO
from src.domain.entities.course_entity import CourseEntity
from src.domain.repositories.course_repository import ICourseRepository


class CourseRepository(ICourseRepository):

    async def create_course(self, dto: CourseCreateDTO) -> CourseEntity:
        course = CourseEntity(**dto.model_dump())
        return await course.insert()

    async def get_course_by_id(self, course_id: str) -> CourseEntity:
        return await CourseEntity.get(course_id)