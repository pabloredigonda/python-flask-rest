from flask_restful import Resource
from src.core.shared.domain.errors.DomainError import DomainError

class UserResource(Resource):

    def __init__(self, **kwargs):
        self.get_user_action = kwargs['get_user_action']

    def get(self):
        try:
            user = self.get_user_action.execute()

            return {
                'firstName': user.firstName,
                'lastName': user.lastName,
                'email': user.email
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