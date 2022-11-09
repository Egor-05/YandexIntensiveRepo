from django.core.exceptions import ValidationError
from functools import wraps


def in_value_validator(*words):
    @wraps(in_value_validator)
    def func(value):
        for i in words:
            if i in value.lower():
                return value
        raise ValidationError("В описании отсутствуют требуемые слова")

    return func


def only_chars_validator(value):
    chars = list("qwertyuiopasdfghjklzxcvbnm1234567890-_")
    for i in value:
        if i not in chars:
            raise ValidationError("В тэге присутствуют запрещенные символы")
    return value


def num_compare_validator(value):
    if not 0 < int(value) < 32767:
        raise ValidationError("Недопустимое значение веса")
    return value
