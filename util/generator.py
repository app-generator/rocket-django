# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import sys

from .common  import *
from .helpers import *
from .cli     import *

def project_create():

    if not dir_exists( 'src' ):
        dir_create( 'src' )

    ROOT = os.getcwd()
    os.chdir('src')
    SRC = os.getcwd()

    # Create project (SRC folder)
    result, stdout, stderr = exec_cmd( 'django-admin startproject core .' )

    if COMMON.OK != result:
        print(' *** Err creating project: ' + stderr)
        exit(1)

    # Migrate db
    result, stdout, stderr = exec_cmd( 'python manage.py migrate' )

    if COMMON.OK != result:
        print(' *** Err migrate DB: ' + stderr)
        exit(1)        

    # Start project
    result, stdout, stderr = exec_cmd( 'python manage.py runserver ' )

    if COMMON.OK != result:
        print(' *** Err start the project: ' + stderr)
        exit(1)
 