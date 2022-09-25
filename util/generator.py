# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import sys

from .common  import *
from .helpers import *
from .cli     import *

def project_create():

    if file_exists( FILE_DJ_MANAGE ):
        print('ERR: project exists, please delete first (runner.py delete)' )
        exit(1)  

    if not dir_exists( 'src' ):
        dir_create( 'src' )

    # Variables used from COMMON
    # DIR_ROOT, DIR_SRC, DIR_DJ_CORE, FILE_DJ_SETTINGS

    os.chdir( DIR_SRC )

    # Create project (SRC folder)
    result, stdout, stderr = exec_cmd( 'django-admin startproject core .' )

    if COMMON.OK != result:
        print('ERR: creating project: ' + stderr)
        exit(1)

    # Migrate db
    result, stdout, stderr = exec_cmd( 'python manage.py migrate' )

    if COMMON.OK != result:
        print('ERR: migrate DB: ' + stderr)
        exit(1)        
 
def project_start():

    if not file_exists( FILE_DJ_MANAGE ):
        print(' Err: project not created, (execute runner.py create)')
        exit(1)        

    os.chdir( DIR_SRC )

    # Migrate db
    result, stdout, stderr = exec_cmd( 'python manage.py migrate' )

    if COMMON.OK != result:
        print('ERR: migrate DB: ' + stderr)
        exit(1)        

    # Start project
    result, stdout, stderr = exec_cmd( 'python manage.py runserver ' )

    if COMMON.OK != result:
        print('ERR: start the project: ' + stderr)
        exit(1)
