# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import json
import os

from django import template
from django.conf import settings

register = template.Library()

def date_format(date):
    """
    Returns a formatted date string
    Format:  `Year-Month-Day-Hour-Minute-Second`
    Example: `2022-10-10-00-20-33`
    :param date datetime: Date object to be formatted
    :rtype: str
    """
    try:
        return date.strftime(r'%Y-%m-%d-%H-%M-%S')
    except:
        return date

register.filter("date_format", date_format)

def get_result_field(result, field: str):
    """
    Returns a field from the content of the result attibute in result 
    Example: `result.result['field']`
    :param result AbortableAsyncResult: Result object to get field from
    :param field str: Field to return from result object
    :rtype: str
    """
    result = json.loads(result.result)
    if result:
        return result.get(field)

register.filter("get_result_field", get_result_field)



def log_file_path(path):
    file_path = path.split("tasks_logs")[1]
    return file_path

register.filter("log_file_path", log_file_path)


def log_to_text(path):
    path = path.lstrip('/')

    full_path = os.path.join(settings.CELERY_LOGS_DIR, path)

    try:
        with open(full_path, 'r') as file:
            text = file.read()
        
        return text
    except:
        return 'NO LOGS'

register.filter("log_to_text", log_to_text)