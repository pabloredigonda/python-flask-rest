from src.core.shared.domain.validators.AbstractValidator import AbstractValidator
import re 

class EmailValidator(AbstractValidator):
    def validate(self, email):
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        return re.search(regex,email)