import json
from functools import wraps
from string import punctuation

import html2text
from django.core.exceptions import ValidationError


def amazing_validator(*must_have_words):
    @wraps(amazing_validator)
    def validator(value):
        text_dict = json.loads(value.json_string)
        text_value = html2text.html2text(text_dict["html"])
        words_in_value = ''
        for i in text_value:
            if i in punctuation:
                words_in_value += ' '
            else:
                words_in_value += i

        words_in_value = set(words_in_value.lower().split())
        difference = set(must_have_words) - words_in_value

        if len(difference) == len(must_have_words):
            raise ValidationError(
                f'В {text_value} нет ни одного из слов {must_have_words}'
            )
        return value

    return validator
