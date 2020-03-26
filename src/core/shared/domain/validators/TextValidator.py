from .AbstractValidator import AbstractValidator

class TextValidator(AbstractValidator):
    def validate(self, text: str) -> bool:
        length = len(str(text))
        return  length > 0 & length < 100