from flask import Blueprint
from flask_restful import Api, Resource
from src.delivery.user.UserResource import UserResource

bp = Blueprint('user', __name__)
api = Api(bp)

def config(app):
    api.add_resource(
        UserResource, 
        '/user/me',
        resource_class_kwargs={ 'get_user_action': app.actionProvider.get_user() }
    )

    app.register_blueprint(bp)