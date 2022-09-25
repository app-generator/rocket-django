# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from .common  import *
from .helpers import *

def h_var_typology( content ):
    
    if not content:
        return COMMON.CFG_VAR_NA

    if '=' in content and '[' in content:
        return COMMON.CFG_VAR_LIST    

    if '=' in content and not '[' in content:
        return COMMON.CFG_VAR_SIMPLE

    # Default is unknown
    return COMMON.CFG_VAR_NA        

def h_extract_sections( content ):

    file_imports  = []
    file_sections = []

    for line in content:

        #print('> line: ' + line)

        # import here    
        if 'from ' in line or 'import ' in line:
            file_imports.append ( h_del_lsep( line ) ) # strip line separators

        # main sections here
        if '=' in line:
            file_sections.append( line.split('=')[0].strip() )

    print("Imports  : " + str( file_imports  ) )       
    print("Sections : " + str( file_sections ) ) 

def settings_load( ):

    retcode = COMMON.OK
    content = []

    # Variables used from COMMON
    # DIR_ROOT, DIR_SRC, DIR_DJ_CORE, FILE_DJ_SETTINGS

    settings_imports  = []
    settings_sections = []

    try:
        
        raw_content = file_load( FILE_DJ_SETTINGS, True ) # as list

        if not raw_content:
            print ('Err loading settings file')
            return COMMON.NOT_FOUND, None 

        # print('Content: ' + raw_content)    
        content = raw_content

    except Exception as e:

        print('Err loading settings: ' + str(e) )
        retcode = COMMON.ERR

    return retcode, content

def settings_save( content ):

    retcode = COMMON.OK

    # Variables used from COMMON
    # DIR_ROOT, DIR_SRC, DIR_DJ_CORE, FILE_DJ_SETTINGS 

    try:
        
        raw_content = '' #'# Note: processed_content ' + os.linesep
        
        for line in content:
        
            raw_content += line
        
        file_write( FILE_DJ_SETTINGS, raw_content)

    except Exception as e:

        retcode = COMMON.ERR

    return retcode

def settings_var_upd( var_name, var_value):

    retcode = COMMON.NOT_FOUND

    retcode, content = settings_load()

    if COMMON.OK != retcode:

        print('Err loading settings file')
        return retcode

    new_content = []
    for line in content:

        if var_name not in line:

            new_content.append( line )
            continue

        # variable found
        retcode = COMMON.OK 

        var_typology = h_var_typology( line )

        if COMMON.CFG_VAR_SIMPLE == var_typology:
            
            line = var_name + ' = ' + '"' + var_value + '"'
            
            print(' UPD -> ' + line)

            new_content.append( line + os.linesep )

    # Variable was found and successfully processed
    if COMMON.OK == retcode:
        settings_save( new_content )

    return retcode

def settings_var_print( var_name ):

    retcode = COMMON.NOT_FOUND

    retcode, content = settings_load()

    if COMMON.OK != retcode:

        print('Err loading settings file')
        return retcode

    new_content = []
    for line in content:

        if var_name not in line:

            new_content.append( line )
            continue
        
        else: 

            # variable found
            retcode = COMMON.OK 

            var_typology = h_var_typology( line )

            print(' > Var found    : ' + h_del_lsep( line )        )
            print(' > Var typology : ' + commonTxt( var_typology ) )

    if COMMON.OK != retcode:
         print(' > Var not found ')

    return retcode    
