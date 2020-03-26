from .DomainError import DomainError

class UnauthorizedError(DomainError):
    def code(self):
        return 'UNAUTHORIZED_ERROR'
    def httpcode(self) -> int:
        return 401