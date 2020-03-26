from src.core.user.domain.User import User

class UserBuilder:
    def fromJson(self, json_data):
        user = User()
        
        if 'id' in json_data:
            user.setId(json_data['id'])

        if 'firstName' in json_data:
            user.setFirstName(json_data['firstName'])

        if 'lastName' in json_data:
            user.setLastName(json_data['lastName'])

        if 'email' in json_data:
            user.setEmail(json_data['email'])

        if 'password' in json_data:
            user.setPassword(json_data['password'])

        return user