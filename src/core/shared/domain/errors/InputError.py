from .DomainError import DomainError

class InputError(DomainError):
    def code(self):
        return 'INPUT_ERROR'