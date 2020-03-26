from .User import User
from .UsersRepository import UsersRepository
from src.core.shared.domain.errors.NotFoundError import NotFoundError

class UserService:

    def __init__(self, repository: UsersRepository):
        self.repository = repository

    def getById(self, id: str) -> User:
        return self.repository.getByIdOrFail(id)