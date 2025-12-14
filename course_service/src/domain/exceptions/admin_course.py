from .base import DomainError


class CourseNotFoundError(DomainError):
    pass


class CourseAlreadyExistsError(DomainError):
    pass


class CourseValidationError(DomainError):
    pass