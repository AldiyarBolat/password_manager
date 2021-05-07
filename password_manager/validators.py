import re
from django.core.exceptions import ValidationError


BLACK_LISTED_PASSWORDS = ['qazwsxedc', 'password', 'qwerty']
url_regex = "^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$"
BLACK_LISTED_LOGIN_CHARS = ['*', '?', '|', '>', '<']


def validate_password(value):
    if value in BLACK_LISTED_PASSWORDS:
        raise ValidationError('Too common password')


def validate_url(value):
    if not re.compile(url_regex).match(value):
        raise ValidationError('Invalid url')


def validate_login(value):
    for ch in value:
        if ch in BLACK_LISTED_LOGIN_CHARS:
            raise ValidationError(f'not allowed character in login: {ch}')
