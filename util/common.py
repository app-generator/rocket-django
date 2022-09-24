# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

class COMMON:

    NULL        = None # not set
    NA          = -1   # not set
    OK          =  0   # all ok
    ERR         =  1   # not ok
    NOT_FOUND   =  2   # file or directory not found
    INPUT_ERR   =  3   # file or directory not found

# Recover errors for COMMON class
def errInfo( aErrorCode ):

    if COMMON.NA         == aErrorCode: return 'Not Set'
    if COMMON.ERR        == aErrorCode: return 'Error Generic'
    if COMMON.OK         == aErrorCode: return 'OK'
    if COMMON.NOT_FOUND  == aErrorCode: return 'Not Found'
    if COMMON.INPUT_ERR  == aErrorCode: return 'Input error'

    return str( aErrorCode )
