from src.core.auth.domain.TokenService import TokenService
from flask_jwt_extended import (create_access_token, jwt_required, get_jwt_identity)

class JwtTokenService (TokenService):

    def createAccessToken(self, userId: str) -> str:
        return create_access_token(identity = userId)

    @jwt_required
    def getUser(self) -> str:
        return get_jwt_identity()