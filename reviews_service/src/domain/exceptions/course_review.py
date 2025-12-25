from .base import DomainError


class ReviewAlreadyExistsError(DomainError):
    pass


class CourseReviewRequirementNotFoundError(DomainError):
    pass
