from app.domain.entities.course_entity import CourseEntity


class CourseService:

    async def create_course(self, title: str, description: str | None):
        course = CourseEntity(
            title=title,
            description=description
        )
        await course.insert()
        return course

    async def get_course_by_id(self, course_id: str):
        course = await CourseEntity.get(course_id)
        return course
