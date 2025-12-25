import grpc

from generated.reviews import course_reviews_pb2 as pb2
from generated.reviews import course_reviews_pb2_grpc as pb2_grpc

from src.application.services.course_review_service import CourseReviewService
from src.domain.exceptions.course_review import (
    ReviewAlreadyExistsError,
    CourseReviewRequirementNotFoundError,
)


class CourseReviewHandler(pb2_grpc.ReviewServiceServicer):

    def __init__(self, service: CourseReviewService):
        self.service = service

    async def CreateReview(self, request, context):
        try:
            review = await self.service.create.execute(
                course_id=request.course_id,
                user_id=request.user_id,
                rating=request.rating,
                comment=request.comment,
                tags=list(request.tags),
            )

            return pb2.CreateReviewResponse(
                review=self._map_review(review)
            )

        except ReviewAlreadyExistsError as e:
            await context.abort(grpc.StatusCode.ALREADY_EXISTS, str(e))

    async def ListReviewsByCourse(self, request, context):
        items, total = await self.service.list_by_course.execute(
            course_id=request.course_id,
            limit=request.limit,
            offset=request.offset,
        )

        return pb2.ListReviewsByCourseResponse(
            items=[self._map_review(review) for review in items],
            total=total,
        )

    async def GetCourseRating(self, request, context):
        average, count = await self.service.get_course_rating.execute(
            course_id=request.course_id
        )

        return pb2.GetCourseRatingResponse(
            course_id=request.course_id,
            average_rating=average,
            reviews_count=count,
        )

    async def SetCourseReviewRequirement(self, request, context):
        requirement = await self.service.set_requirement.execute(
            course_id=request.course_id,
            required_reviews_count=request.required_reviews_count,
        )

        return pb2.SetCourseReviewRequirementResponse(
            requirement=self._map_requirement(requirement)
        )

    async def GetCourseReviewRequirement(self, request, context):
        try:
            requirement = await self.service.get_requirement.execute(
                course_id=request.course_id
            )

            return pb2.GetCourseReviewRequirementResponse(
                requirement=self._map_requirement(requirement)
            )

        except CourseReviewRequirementNotFoundError as e:
            await context.abort(grpc.StatusCode.NOT_FOUND, str(e))

    @staticmethod
    def _map_review(review):
        return pb2.Review(
            id=str(review.id),
            course_id=review.course_id,
            user_id=review.user_id,

            rating=review.rating,
            comment=review.comment or "",
            tags=review.tags or [],

            created_at=int(review.created_at.timestamp()),
        )

    @staticmethod
    def _map_requirement(requirement):
        return pb2.CourseReviewRequirement(
            course_id=requirement.course_id,
            required_reviews_count=requirement.required_reviews_count,
            current_reviews_count=requirement.current_reviews_count,
            is_satisfied=requirement.is_satisfied,
        )
