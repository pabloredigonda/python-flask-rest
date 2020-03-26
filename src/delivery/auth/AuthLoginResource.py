from flask import request
from flask_restful import Resource
from src.core.user.domain.User import User
from src.core.user.domain.UserBuilder import UserBuilder
from src.core.shared.domain.errors.DomainError import DomainError

class AuthLoginResource(Resource):

    def __init__(self, **kwargs):
        self.login_user_action = kwargs['login_user_action']

    def post(self) -> dict:
        try:
            json_data = request.get_json(force=True)
            user = UserBuilder().fromJson(json_data)
            token = self.login_user_action.execute(user)
            return {
                'accessToken': token
            }

        except DomainError as err:
            return {
                'error': err.code(),
                'message': err.message()
            }, err.httpcode()

        except BaseException as err:
            return {
                'error': 'ServerError',
                'message': "Something's got wrong",
                'detail' : err

            }, 500

        