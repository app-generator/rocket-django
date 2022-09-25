# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os

DIR_ROOT          = os.path.dirname(os.path.dirname(__file__))
DIR_SRC           = os.path.join(DIR_ROOT    , 'src'  )
DIR_DJ_CORE       = os.path.join(DIR_SRC     , 'core' )

FILE_DJ_MANAGE    = os.path.join(DIR_SRC     , 'manage.py'  )
FILE_DJ_SETTINGS  = os.path.join(DIR_DJ_CORE , 'settings.py')

class COMMON:

    NULL              = None # not set
    NA                = -1   # not set
    OK                =  0   # All good   (unix style)
    ERR               =  1   # Err bumped (unix style)
    NOT_FOUND         =  2   # file or directory not found
    INPUT_ERR         =  3   # file or directory not found

    # Settings vars typologies 
    CFG_VAR_NA        = 10 # Type is undetected
    CFG_VAR_SIMPLE    = 11 # Ex: SECRET_KEY
    CFG_VAR_LIST      = 12 # Ex: INSTALLED_APPS, MIDDLEWARE
    CFG_VAR_MIXED     = 13 # List of Dicts, Ex: AUTH_PASSWORD_VALIDATORS 

# Recover errors for COMMON class
def errInfo( aErrorCode ):

    if COMMON.NA         == aErrorCode: return 'Not Set'
    if COMMON.ERR        == aErrorCode: return 'Error Generic'
    if COMMON.OK         == aErrorCode: return 'OK'
    if COMMON.NOT_FOUND  == aErrorCode: return 'Not Found'
    if COMMON.INPUT_ERR  == aErrorCode: return 'Input error'

    return str( aErrorCode )

def commonTxt( aCode ):

    if COMMON.CFG_VAR_NA     == aCode: return 'CFG Var unknown typology'
    if COMMON.CFG_VAR_SIMPLE == aCode: return 'CFG Var SIMPLE'
    if COMMON.CFG_VAR_LIST   == aCode: return 'CFG Var LIST'
    if COMMON.CFG_VAR_MIXED  == aCode: return 'CFG Var MIXT (list of dicts)'

    return str( aErrorCode )
 
