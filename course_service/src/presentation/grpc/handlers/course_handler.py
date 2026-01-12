import grpc

from generated.course import course_pb2 as pb2
from generated.course import course_pb2_grpc as pb2_grpc

from src.application.services.course_service import CourseService
from src.domain.exceptions.course import CourseNotFoundError


class CourseHandler(pb2_grpc.CourseServiceServicer):

    def __init__(self, service: CourseService):
        self.service = service

    async def GetCourse(self, request, context):
        try:
            course = await self.service.get.execute(request.id)
            lessons_count = await self.service.get_lessons_count.execute(request.id)
            return pb2.GetCourseResponse(
                id=str(course.id),
                title=course.title,
                description=course.description or "",

                author_id=str(course.author_id) if course.author_id else "",

                level=course.level.value,
                duration_minutes=course.duration_minutes,
                language=course.language.value,
                requires_experience=course.requires_experience,

                price=pb2.CoursePrice(
                    type=course.price.type.value,
                    amount=course.price.amount or 0,
                ),

                category_ids=list(course.category_ids),
                mentor_ids=list(course.mentor_ids),
                cover_image_id=course.cover_image_id or "",
                lessons_count=lessons_count,
                sections=[
                    pb2.CourseSection(
                        title=section.title,
                        items=section.items,
                    )
                    for section in course.sections
                ]
            )

        except CourseNotFoundError as e:
            await context.abort(grpc.StatusCode.NOT_FOUND, str(e))

    async def ListCourses(self, request, context):
        limit = request.limit or 10
        offset = request.offset or 0
        mode = request.mode or "all"
        author_id = request.author_id or None

        items, total = await self.service.list.execute(
            limit=limit,
            offset=offset,
            mode=mode,
            author_id=author_id,
        )

        return pb2.ListCoursesResponse(
            items=[
                pb2.Course(
                    id=str(course.id),
                    title=course.title,
                    description=course.description or "",

                    duration_minutes=course.duration_minutes,
                    language=course.language.value,

                    price=pb2.CoursePrice(
                        type=course.price.type.value,
                        amount=course.price.amount or 0,
                    ),

                    category_ids=list(course.category_ids),
                    cover_image_id=course.cover_image_id or "",
                    is_promoted=course.is_promoted or False,
                )
                for course in items
            ],
            total=total
        )
