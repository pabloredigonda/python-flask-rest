from src.core.auth.domain.AuthService import AuthService
from src.core.user.domain.User import User

class LoginUserAction:
    def __init__(self, service: AuthService):
        self.service = service

    def execute(self, user: User):
        #TODO Dispatch event user.registered
        return self.service.login(user)