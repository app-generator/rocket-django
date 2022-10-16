# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import sys

from .common  import *
from .helpers import *
from .cli     import *
from .parser  import *

def project_create():

    if file_exists( FILE_DJ_MANAGE ):
        print('ERR: project exists, please delete first (runner.py delete)' )
        sys.exit(1)  

    if not dir_exists( 'src' ):
        dir_create( 'src' )

    # Variables used from COMMON
    # DIR_ROOT, DIR_SRC, DIR_DJ_CORE, FILE_DJ_SETTINGS

    os.chdir( DIR_SRC )

    # Create project (SRC folder)
    result, stdout, stderr = exec_cmd( 'django-admin startproject core .' )

    if COMMON.OK != result:
        print('ERR: creating project: ' + stderr)
        sys.exit(1)

    # Migrate db
    result, stdout, stderr = exec_cmd( 'python manage.py migrate' )

    if COMMON.OK != result:
        print('ERR: migrate DB: ' + stderr)
        sys.exit(1)        
 
def project_start():

    if not file_exists( FILE_DJ_MANAGE ):
        print(' Err: project not created, (execute runner.py create)')
        sys.exit(1)        

    os.chdir( DIR_SRC )

    # Migrate db
    result, stdout, stderr = exec_cmd( 'python manage.py migrate' )

    if COMMON.OK != result:
        print('ERR: migrate DB: ' + stderr)
        sys.exit(1)        

    # Start project
    result, stdout, stderr = exec_cmd( 'python manage.py runserver ' )

    if COMMON.OK != result:
        print('ERR: start the project: ' + stderr)
        sys.exit(1)

def project_create_app( appName ):

    #print( 'Create app: ' + appName )
    
    APP_DIR = os.path.join(DIR_SRC, appName )

    # Check app exists
    if dir_exists( APP_DIR ):
        print('ERR: app already exists')
        sys.exit(1)        

    os.chdir( DIR_SRC )

    # Create project (SRC folder)
    result, stdout, stderr = exec_cmd( 'django-admin startapp ' + appName )

    if COMMON.OK != result:
        print('ERR: creating app: ' + stderr)
        sys.exit(1)

    # Update settings
    retcode, section_content = settings_apps_add( appName )

    if COMMON.OK != result:
        print('ERR updating configuration ')
        sys.exit(1) 

    print('App [' + appName + '] created successfully')

def project_delete_app( appName ):

    #print( 'Create app: ' + appName )
    
    APP_DIR = os.path.join(DIR_SRC, appName )

    # Check app exists
    if not dir_exists( APP_DIR ):
        print('ERR: app not defined: ' + appName)
        sys.exit(1)

    dir_delete( APP_DIR )
    print('App [' + appName + '] deleted successfully')
