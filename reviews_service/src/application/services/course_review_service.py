from src.application.commands.course_review.create_review import CreateReviewCommand
from src.application.queries.course_review.list_by_course import ListReviewsByCourseQuery
from src.application.queries.course_review.get_course_rating import GetCourseRatingQuery
from src.domain.repositories.course_review_repository import (
    ICourseReviewRepository,
)


class CourseReviewService:
    def __init__(self, repo: ICourseReviewRepository):
        self.create = CreateReviewCommand(repo)
        self.list_by_course = ListReviewsByCourseQuery(repo)
        self.get_course_rating = GetCourseRatingQuery(repo)