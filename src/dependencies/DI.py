from src.dependencies.ServiceProvider import ServiceProvider
from src.dependencies.ActionProvider import ActionProvider
from src.dependencies.RepositoryProvider import RepositoryProvider
from src.dependencies.ValidatorProvider import ValidatorProvider

from src.Enviroment import Enviroment
from flask_jwt_extended import JWTManager
from flask_mongoengine import MongoEngine
from src.core.shared.infrastructure.database.db import db, initialize_db

class DI:
    def __init__(self, app):
        self.app = app
        self.db = db
        self.jwt = JWTManager(app)
        initialize_db(app)
        self.enviroment = app.enviroment

        self.repository_provider = RepositoryProvider(self.db)
        self.validator_provider = ValidatorProvider(self.repository_provider)
        self.service_provider = ServiceProvider(self.enviroment, self.repository_provider, self.validator_provider)
        self.actions_provider = ActionProvider(self.service_provider)

    def repository(self):
        return self.repository_provider

    def actions(self):
        return self.actions_provider
    
    def services(self):
        return self.service_provider
    
    def validator(self):
        return self.validator_provider

    def database(self):
        return self.db


