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

    async def ListCoursesByIds(self, request, context):
        try:
            items = await self.service.list_by_ids.execute(request.ids)

            return pb2.ListCoursesByIdsResponse(
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
                ]
            )

        except Exception as e:
            await context.abort(grpc.StatusCode.INTERNAL, str(e))


    async def GetCourseLessons(self, request, context):
        try:
            lessons = await self.service.get_lessons.execute(
                course_id=request.course_id
            )

            return pb2.GetCourseLessonsResponse(
                items=[
                    pb2.CourseLesson(
                        id=str(lesson.id),
                        title=lesson.title,

                        type=lesson.type.value,
                        access_type=lesson.access_type.value,
                        duration=lesson.duration,

                        order_number=lesson.order_number,
                        is_active=lesson.is_active,
                    )
                    for lesson in lessons
                ]
            )

        except CourseNotFoundError as e:
            await context.abort(grpc.StatusCode.NOT_FOUND, str(e))

        except Exception as e:
            await context.abort(grpc.StatusCode.INTERNAL, str(e))
