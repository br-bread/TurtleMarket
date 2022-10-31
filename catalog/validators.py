from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class AmazingValidator:
    must_have_words = []

    def __init__(self, *must_have_words):
        self.must_have_words = must_have_words

    def __call__(self, value):
        value_words = value.lower().split()
        if self.must_have_words is not None:
            for i in self.must_have_words:
                if i.lower() in value_words:
                    return value

        raise ValidationError(f'There must be one of {self.must_have_words}')

    def __eq__(self, other):
        return (isinstance(
                other, AmazingValidator
                ) and self.must_have_words == other.must_have_words)
