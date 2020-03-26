from src.core.shared.domain.validators.EmailValidator import EmailValidator
from src.core.shared.domain.validators.TextValidator import TextValidator
from src.core.shared.domain.validators.EmailNotInDbValidator import EmailNotInDbValidator
from src.core.auth.domain.UserRegisterValidator import UserRegisterValidator

from src.dependencies.RepositoryProvider import RepositoryProvider

class ValidatorProvider:
    def __init__(self, repository_provider: RepositoryProvider):
        self.repository_provider = repository_provider

    def email(self) -> EmailValidator:
        return EmailValidator()

    def text(self) -> TextValidator:
        return TextValidator()

    def emailNotInDbValidator(self) -> EmailNotInDbValidator:
        return EmailNotInDbValidator(self.repository_provider.users())

    def userRegisterValidator(self) -> UserRegisterValidator:
        return UserRegisterValidator(
            self.email(),
            self.emailNotInDbValidator(),
            self.text()
        )


