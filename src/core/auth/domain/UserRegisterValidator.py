from src.core.user.domain.User import User
from src.core.user.domain.UsersRepository import UsersRepository
from src.core.shared.domain.validators.EmailValidator import EmailValidator
from src.core.shared.domain.validators.EmailNotInDbValidator import EmailNotInDbValidator
from src.core.shared.domain.validators.TextValidator import TextValidator
from src.core.shared.domain.errors.InputError import InputError

class UserRegisterValidator:

    def __init__(self, emailValidator: EmailValidator, emailNotInDbValidator: EmailNotInDbValidator, textValidator: TextValidator):
        self.emailValidator = emailValidator
        self.emailNotInDbValidator = emailNotInDbValidator
        self.textValidator = textValidator

    def validate(self, user: User) -> bool:

        if self.emailValidator.validate(user.email) == False:
            return False
        if self.textValidator.validate(user.firstName) == False:
            return False
        if self.textValidator.validate(user.lastName) == False:
            return False
        if self.emailNotInDbValidator.validate(user.email) == False:
            return False
        
        return True
