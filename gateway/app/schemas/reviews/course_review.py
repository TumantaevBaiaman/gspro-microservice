from pydantic import BaseModel, Field
from typing import List


class CreateReviewRequestSchema(BaseModel):
    rating: int = Field(ge=1, le=5)
    comment: str | None = None
    tags: list[str] = []


class ListReviewsQuerySchema(BaseModel):
    limit: int = Field(default=20, ge=1, le=100)
    offset: int = Field(default=0, ge=0)


class SetCourseReviewRequirementSchema(BaseModel):
    required_reviews_count: int = Field(ge=1)


class ReviewSchema(BaseModel):
    id: str
    course_id: str
    user_id: str

    rating: int
    comment: str
    tags: List[str]

    created_at: int


class ListReviewsResponseSchema(BaseModel):
    items: List[ReviewSchema]
    total: int


class CourseRatingSchema(BaseModel):
    course_id: str
    average_rating: float
    reviews_count: int


class CourseReviewRequirementSchema(BaseModel):
    course_id: str
    required_reviews_count: int
    current_reviews_count: int
    is_satisfied: bool
