from flask import Flask
from src.dependencies.DI import DI
from .Enviroment import Enviroment

class Application:
    def __init__(self, enviroment: Enviroment):
        self.enviroment = enviroment

    def init(self):
        app = Flask(__name__)
        app.enviroment = self.enviroment
        app.config['MONGODB_SETTINGS'] = {
            'host': self.enviroment.mongoSettings
        }
        app.config['JWT_SECRET_KEY'] = self.enviroment.jwtSecret

        di = DI(app)
        app.di = di
        app.actionProvider = di.actions()
        app.serviceProvider = di.services()

        # Modules
        from src.delivery.user import bp as bp_user
        bp_user.config(app)

        from src.delivery.auth import bp as bp_auth
        bp_auth.config(app)

        return app