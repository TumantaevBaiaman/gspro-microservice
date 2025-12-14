from .base import DomainError


class ModuleNotFoundError(DomainError):
    pass


class ModuleAlreadyExistsError(DomainError):
    pass


class ModuleValidationError(DomainError):
    pass
