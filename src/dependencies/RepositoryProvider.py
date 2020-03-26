from src.core.user.infrastructure.MongoUsersRepository import MongoUsersRepository
from flask_mongoengine import MongoEngine

class RepositoryProvider:
    def __init__(self, db: MongoEngine):
        self.db = db

    def users(self) -> MongoUsersRepository:
        return MongoUsersRepository()