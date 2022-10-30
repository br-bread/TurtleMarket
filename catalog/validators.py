from django.core.exceptions import ValidationError


class AmazingValidator:
    def __init__(self, *must_have_words):
        self.must_have_words = must_have_words

    def call(self, value):
        value_words = value.lower().split()
        if self.must_have_words is not None:
            for i in self.must_have_words:
                if i.lower() not in value_words:
                    raise ValidationError(
                        f'There must be one of {self.must_have_words}')

        return value
