class DomainError(Exception):
    def __init__(self, message=''):
        self._message = message
    
    def code(self) -> str:
        return 'DOMAIN_ERROR'

    def message(self) -> str:
        return self._message

    def httpcode(self) -> int:
        return 400