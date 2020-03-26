from src.core.user.domain.User import User
from src.core.user.domain.UsersRepository import UsersRepository
from src.core.shared.infrastructure.database.UserEntity import UserEntity
from src.core.shared.domain.errors.NotFoundError import NotFoundError

class MongoUsersRepository(UsersRepository):

    def create(self, user: User) -> User:
        userEntity = UserEntity(
            firstName=user.firstName,
            lastName=user.lastName,
            email=user.email,
            password=user.password
        ).save()

        id = userEntity.id

        user.setId(str(id))
        return user

    def getByEmailOrFail(self, email: str) -> User:
        u = UserEntity.objects(email=email).first()

        if u == None:
            raise NotFoundError()

        return self.buildUser(u)

    def getByIdOrFail(self, id: str) -> User:
        u = UserEntity.objects.get(id=id)
        if u == None:
            raise NotFoundError()

        return self.buildUser(u)

    def buildUser(self, userEntity) -> User:
        user = User(
            firstName=userEntity.firstName,
            lastName=userEntity.lastName,
            email=userEntity.email,
            password=userEntity.password
        )

        id = userEntity.id
        user.setId(str(id))
        return user
