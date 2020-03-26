from src.core.shared.actions.PrivateAction import PrivateAction
from src.core.user.domain.UserService import UserService
from src.core.auth.domain.TokenService import TokenService
from src.core.user.domain.User import User

class GetUserAction(PrivateAction):
    def __init__(self, service: UserService, tokenService: TokenService):
        super().__init__(service, tokenService)

    def execute(self) -> User:
        return self.getCurrentUser()