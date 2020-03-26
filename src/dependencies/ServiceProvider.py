from src.core.user.domain.UserService import UserService
from src.core.auth.domain.AuthService import AuthService
from src.core.auth.infrastructure.JwtTokenService import JwtTokenService
from src.Enviroment import Enviroment

from src.dependencies.RepositoryProvider import RepositoryProvider
from src.dependencies.ValidatorProvider import ValidatorProvider

class ServiceProvider:
    def __init__(self, enviroment: Enviroment, repository_provider: RepositoryProvider, validators_provider: ValidatorProvider):
        self.enviroment = enviroment
        self.repository_provider = repository_provider
        self.validators_provider = validators_provider

    def user(self) -> UserService:
        return UserService(self.repository_provider.users())

    def auth(self) -> AuthService:
        return AuthService(
            self.validators_provider.userRegisterValidator(),
            self.repository_provider.users(),
            self.jwtTokenService()
        )

    def jwtTokenService(self) -> JwtTokenService:
        return JwtTokenService()


