# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os

from celery import Celery

if os.environ.get('DJANGO_SETTINGS_MODULE'):

    app = Celery('config')

    # Using a string here means the worker doesn't have to serialize
    # the configuration object to child processes.
    # - namespace='CELERY' means all celery-related configuration keys
    #   should have a `CELERY_` prefix.
    app.config_from_object('django.conf:settings', namespace='CELERY')

    # Load task modules from all registered Django apps.
    app.autodiscover_tasks()

else:
    print(' ')
    print('Celery Configuration ERROR: ') 
    print('  > "DJANGO_SETTINGS_MODULE" not set in environment (value in manage.py)')
    print('  Hint: export DJANGO_SETTINGS_MODULE=project.settings ') 
    print(' ')