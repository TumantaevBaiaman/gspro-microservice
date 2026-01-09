from fastapi import APIRouter, Depends

from app.api.dependencies.auth import get_current_user
from app.clients.review import course_review_client

from app.schemas.reviews.course_review import (
    CreateReviewRequestSchema,
    ListReviewsQuerySchema,
    ListReviewsResponseSchema,
    ReviewSchema,
    CourseRatingSchema,
    CourseReviewRequirementSchema,
    SetCourseReviewRequirementSchema,
)

course_review_router = APIRouter(
    prefix="/courses/{course_id}/reviews",
    tags=["Course Reviews"],
)


@course_review_router.post(
    "",
    response_model=ReviewSchema,
    summary="Create a review for a courses",
    description="Create a review for a courses by providing rating, comment, and tags."
)
def create_review(
    course_id: str,
    data: CreateReviewRequestSchema,
    user=Depends(get_current_user),
):
    user_id = user.get("sub")
    return course_review_client.create_review(
        course_id=course_id,
        user_id=user_id,
        rating=data.rating,
        comment=data.comment or "",
        tags=data.tags,
    )


@course_review_router.get(
    "",
    response_model=ListReviewsResponseSchema,
    summary="List reviews for a courses",
    description="Retrieve a list of reviews for a specific courses with pagination support."
)
def list_reviews(
    course_id: str,
    query: ListReviewsQuerySchema = Depends(),
):
    return course_review_client.list_reviews_by_course(
        course_id=course_id,
        limit=query.limit,
        offset=query.offset,
    )


@course_review_router.get(
    "/rating",
    response_model=CourseRatingSchema,
    summary="Get courses rating",
    description="Retrieve the average rating and total number of reviews for a specific courses."
)
def get_course_rating(course_id: str):
    return course_review_client.get_course_rating(course_id)


@course_review_router.post(
    "/requirement",
    response_model=CourseReviewRequirementSchema,
    summary="Set courses review requirement",
    description="Set the required number of reviews for a specific courses.",
)
def set_course_review_requirement(
    course_id: str,
    data: SetCourseReviewRequirementSchema,
):
    return course_review_client.set_course_review_requirement(
        course_id=course_id,
        required_reviews_count=data.required_reviews_count,
    )


@course_review_router.get(
    "/requirement",
    response_model=CourseReviewRequirementSchema,
    summary="Get courses review requirement",
    description="Retrieve the required number of reviews for a specific courses.",
)
def get_course_review_requirement(course_id: str):
    return course_review_client.get_course_review_requirement(course_id)
