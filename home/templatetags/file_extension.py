from django import template
import os
from urllib.parse import quote

register = template.Library()

@register.filter
def file_extension(value):
    _, extension = os.path.splitext(value)
    return extension.lower()


@register.filter
def encoded_file_path(path):
    return path.replace('/', '%slash%')

@register.filter
def encoded_path(path):
    return path.replace('\\', '/')