from dataclasses import dataclass


@dataclass(slots=True)
class CreateReviewDTO:
    course_id: str
    user_id: str
    rating: int
    comment: str
    tags: list[str]
