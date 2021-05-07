import os
from django.core.exceptions import ValidationError

MAX_FILE_SIZE = 1024000
ALLOWED_EXTENSIONS = ['.jpg', '.png', '.svg']
BLACK_LISTED_NAME_CHARACTERS = ['*', '?', '|', '>', '<']


def validate_size(value):
    if value.size > MAX_FILE_SIZE:
        raise ValidationError(f'max file size is: {MAX_FILE_SIZE}')


def validate_extension(value):
    split_ext = os.path.splitext(value.name)

    if len(split_ext) > 1:
        ext = split_ext[1]
        if ext.lower() not in ALLOWED_EXTENSIONS:
            raise ValidationError(f'not allowed file, valid extensions: {ALLOWED_EXTENSIONS}')


def validate_name(value):
    for ch in value.name:
        if ch in BLACK_LISTED_NAME_CHARACTERS:
            raise ValidationError(f'not allowed character in name: {ch}')
