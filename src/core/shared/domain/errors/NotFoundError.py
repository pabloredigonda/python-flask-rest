from .DomainError import DomainError

class NotFoundError(DomainError):
    def code(self):
        return 'NOT_FOUND_ERROR'