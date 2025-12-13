from .base import DomainError


class CategoryNotFoundError(DomainError):
    pass


class CategoryAlreadyExistsError(DomainError):
    pass


class CategoryValidationError(DomainError):
    pass
