from src.core.shared.domain.errors.DomainError import DomainError

class InvalidCredentialsError(DomainError):
    def code(self):
        return 'INVALID_CREDENTIALS_ERROR'