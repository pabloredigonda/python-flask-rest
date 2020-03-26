from src.core.shared.domain.validators.AbstractValidator import AbstractValidator
from src.core.user.domain.User import User
from src.core.user.domain.UsersRepository import UsersRepository
from src.core.shared.domain.errors.NotFoundError import NotFoundError

class EmailNotInDbValidator(AbstractValidator):

    def __init__(self, repository: UsersRepository):
        self.repository = repository

    def validate(self, email: str) -> bool:
        try:
            self.repository.getByEmailOrFail(email)
            return False
        except NotFoundError:
            return True