from src.dependencies.ServiceProvider import ServiceProvider
from src.core.user.actions.GetUserAction import GetUserAction
from src.core.auth.actions.RegisterUserAction import RegisterUserAction
from src.core.auth.actions.LoginUserAction import LoginUserAction

class ActionProvider:
    def __init__(self, service_provider: ServiceProvider):
        self.service_provider = service_provider

    def get_user(self) -> GetUserAction:
        return GetUserAction( service=self.service_provider.user(), tokenService=self.service_provider.jwtTokenService() )

    def register_user(self) -> RegisterUserAction:
        return RegisterUserAction( service=self.service_provider.auth() )

    def login_user(self) -> LoginUserAction:
        return LoginUserAction( service=self.service_provider.auth() )