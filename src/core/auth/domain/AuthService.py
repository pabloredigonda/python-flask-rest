from src.core.user.domain.User import User
from src.core.user.domain.UsersRepository import UsersRepository
from src.core.auth.domain.TokenService import TokenService
from src.core.auth.domain.UserRegisterValidator import UserRegisterValidator
from src.core.shared.domain.errors.NotFoundError import NotFoundError
from src.core.shared.domain.errors.InputError import InputError

from src.core.auth.domain.InvalidCredentialsError import InvalidCredentialsError

class AuthService:

    def __init__(self, validator: UserRegisterValidator, repository: UsersRepository, tokenService: TokenService):
        self.validator = validator
        self.repository = repository
        self.tokenService = tokenService

    def register(self, user: User) -> str:

        if self.validator.validate(user) == False:
            raise InputError('Invalid Input')

        user = self.repository.create(user)
        return self.tokenService.createAccessToken(user.id)

    def login(self, user: User) -> str:

        try:
            maybeUser: User = self.repository.getByEmailOrFail(user.email)
            
            if maybeUser.password != user.password:
                raise InvalidCredentialsError()

            return self.tokenService.createAccessToken(maybeUser.id)

        except NotFoundError:
            raise InvalidCredentialsError()