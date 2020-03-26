from flask import Blueprint
from flask_restful import Api, Resource
from src.delivery.auth.AuthLoginResource import AuthLoginResource
from src.delivery.auth.AuthRegisterResource import AuthRegisterResource

bp = Blueprint('auth', __name__)
api = Api(bp)

def config(app):
    api.add_resource(
        AuthLoginResource, 
        '/auth/login',
        resource_class_kwargs={ 'login_user_action': app.actionProvider.login_user() }
    )

    api.add_resource(
        AuthRegisterResource, 
        '/auth/register',
        resource_class_kwargs={ 'register_user_action': app.actionProvider.register_user() }
    )

    app.register_blueprint(bp)