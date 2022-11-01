from string import punctuation

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class AmazingValidator:
    must_have_words = []

    def __init__(self, *must_have_words):
        self.must_have_words = must_have_words

    def __call__(self, value):
        words_in_value = ''
        for i in value:
            if i in punctuation:
                words_in_value += ' '
            else:
                words_in_value += i
        words_in_value = words_in_value.lower().split()

        if self.must_have_words is not None:
            for i in self.must_have_words:
                if i.lower() in words_in_value:
                    return value

        raise ValidationError(
            f'В {value} нет ни одного из слов {self.must_have_words}')

    def __eq__(self, other):
        return (isinstance(
                other, AmazingValidator
                ) and self.must_have_words == other.must_have_words)
