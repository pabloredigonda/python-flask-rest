from src.core.user.domain.UserService import UserService
from src.core.user.domain.User import User
from src.core.auth.domain.TokenService import TokenService
from src.core.shared.domain.errors.UnauthorizedError import UnauthorizedError

class PrivateAction:
    def __init__(self, service: UserService, tokenService: TokenService):
        self.service = service
        self.tokenService = tokenService

    def getCurrentUser(self) -> User:

        try:
            userId = self.tokenService.getUser()
            return self.service.getById(userId)
        except Exception:
            raise UnauthorizedError()