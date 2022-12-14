# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from .common  import *
from .helpers import *
from .cli     import *

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
        
        raw_content = ''
        
        for line in content:
        
            raw_content += line
        
        file_write( FILE_DJ_SETTINGS, raw_content)

    except Exception as e:

        retcode = COMMON.ERR

    return retcode

def settings_format( ):

    retcode = COMMON.OK

    try:    

        if not ( file_exists( FILE_DJ_SETTINGS ) ):
            print( 'Err locate project settings' )
            retcode = COMMON.ERR

        os.chdir( DIR_DJ_CORE )

        # Apply 'Black' sules over the file
        result, stdout, stderr = exec_cmd( 'black settings.py' )

        if COMMON.OK != result:
            print('Err formating settings: ' + stderr)
            exit(1)   

    except Exception as e:

        print('Err formating exeption: ' + str(e) )
        retcode = COMMON.ERR

    return retcode

def h_var_typology( content ):
    
    if not content:
        return COMMON.CFG_VAR_NA

    if '=' in content and '[' in content:
        return COMMON.CFG_VAR_LIST    

    if '=' in content and '{' in content:
        return COMMON.CFG_VAR_DICT  

    if '=' in content and not '[' in content and not '}' in content:
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

    return file_sections

def settings_imports():

    retcode = COMMON.OK
    imports = []

    retcode, content = settings_load()

    if COMMON.OK != retcode:

        print('Err loading settings file')
        return retcode, None

    for line in content:

        # import here    
        if 'from ' in line or 'import ' in line:
            imports.append ( h_del_lsep( line ) ) # strip line separators

    return retcode, imports

def settings_sections():

    retcode  = COMMON.OK
    sections = []

    retcode, content = settings_load()

    if COMMON.OK != retcode:

        print('Err loading settings file')
        return retcode, None

    for line in content:

        # import here    
        if '=' in line:
            sections.append( line.split('=')[0].strip() )

    return retcode, sections

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

def settings_section_get( section ):

    retcode = COMMON.NOT_FOUND

    retcode, content = settings_load()

    if COMMON.OK != retcode:

        print('Err loading settings file')
        return retcode

    section_content = []
    section_begin   = False 
    section_end     = False 
    retcode         = COMMON.NOT_FOUND

    # This is used to count [, {
    section_control_begin = '' 
    section_control_end   = '' 
    section_control_idx   = 0 

    for line in content:

        line = h_del_lsep( line )

        # We have an end here
        if section_end:
            break 

        # Computing is over
        if section_begin and section_control_idx == 0:
            section_end = True 
            retcode     = COMMON.OK
            continue 

        # Computing is active 
        if section_begin:

            section_content.append( line )

            if section_control_begin in line:
                section_control_idx += 1    

            if section_control_end in line:
                section_control_idx -= 1    

        # Other things
        if not section_begin and section not in line:
            continue 

        # Here is a match
        if '=' in line: 
            section_begin = True

        # Detect topology 
        var_typology = h_var_typology( line )

        # Simple, one-time 
        if COMMON.CFG_VAR_SIMPLE == var_typology:
            
            section_content.append( line )

            section_end = True 
            retcode     = COMMON.OK

        # Lists (we can have mixed types)
        if COMMON.CFG_VAR_LIST == var_typology:

            # save the first line            
            section_content.append( line )

            section_begin = True 

            retcode = COMMON.OK

            section_control_begin = '['
            section_control_end   = ']'
            section_control_idx   = 1 

        # Dicts (we can have mixed types)
        if COMMON.CFG_VAR_DICT == var_typology:

            # save the first line            
            section_content.append( line )

            section_begin = True 

            retcode = COMMON.OK

            section_control_begin = '{'
            section_control_end   = '}'
            section_control_idx   = 1 

    # Exit
    if COMMON.OK == retcode:
        print( ' ' )
        for item in section_content:
            print ( item )         
    else:    
        print( ' > Section ['+section+'] not found ' )

    # Exit point 
    return retcode, section_content

def settings_section_update( section, var_value ):

    retcode = COMMON.NOT_FOUND

    retcode, content = settings_load()

    if COMMON.OK != retcode:

        print('Err loading settings file')
        return retcode

    section_content = []
    section_begin   = False 
    section_end     = False 
    retcode         = COMMON.NOT_FOUND

    # This is used to count [, {
    section_control_begin = '' 
    section_control_end   = '' 
    section_control_idx   = 0 

    new_content = []
    for line in content:

        # line = h_del_lsep( line )

        # We have an end here
        if section_end:
            new_content.append( line )
            continue 

        # Computing is over
        if section_begin and section_control_idx == 0:

            # new content injected
            new_content.append( var_value + os.linesep )

            new_content.append( line )

            section_end = True 
            retcode     = COMMON.OK
            continue 

        # Computing is active 
        if section_begin:

            section_content.append( h_del_lsep( line ) )

            if section_control_begin in line:
                section_control_idx += 1    

            if section_control_end in line:
                section_control_idx -= 1    

        # Other things
        if not section_begin and section not in line:

            new_content.append( line )
            
            continue 

        # Here is a match
        if '=' in line: 
            section_begin = True

        # Detect topology 
        var_typology = h_var_typology( line )

        # Simple, one-time 
        if COMMON.CFG_VAR_SIMPLE == var_typology:
            
            new_content.append( var_value + os.linesep )
            
            section_content.append( h_del_lsep( line ) )

            section_end = True 
            retcode     = COMMON.OK

        # Lists (we can have mixed types)
        if COMMON.CFG_VAR_LIST == var_typology:

            # save the first line            
            section_content.append( h_del_lsep( line ) )

            section_begin = True 

            retcode = COMMON.OK

            section_control_begin = '['
            section_control_end   = ']'
            section_control_idx   = 1 

        # Dicts (we can have mixed types)
        if COMMON.CFG_VAR_DICT == var_typology:

            # save the first line            
            section_content.append( h_del_lsep( line ) )

            section_begin = True 

            retcode = COMMON.OK

            section_control_begin = '{'
            section_control_end   = '}'
            section_control_idx   = 1 

    # Exit
    if COMMON.OK == retcode:

        # Save the content
        settings_save( new_content )
        settings_format()

        print( ' ' )
        for item in section_content:
            print ( item )         
    else:    
        print( ' > Section ['+section+'] not found ' )

    # Exit point 
    return retcode, section_content

def settings_apps_list():

    retcode = COMMON.OK
    apps    = []

    # load INSTALLED_APPS
    retcode, section_content = settings_section_get('INSTALLED_APPS')

    if COMMON.OK != retcode:

        print('Err loading INSTALLED_APPS section')
        return retcode, None

    tmp = ''
    
    # list to str
    for x in section_content:
        tmp += x.strip(' ') 

    # cleanUP
    tmp = tmp.replace(' ', '')
    tmp = tmp.replace('=', '')
    tmp = tmp.replace('INSTALLED_APPS', '')
    tmp = tmp.replace('[', '')
    tmp = tmp.replace(']', '')

    tmp_list = tmp.split( "','" )
    for x in tmp_list:
        x = x.replace("'", '')
        x = x.replace(",", '')
        apps.append( x )

    return retcode, apps    

# Add a new app in the INSTALLED_APPS
def settings_apps_add( appName ):

    # Check app exists
    APP_DIR = os.path.join(DIR_SRC, appName )

    # Check app exists
    if not dir_exists( APP_DIR ):
        print('ERR: app not defined: ' + appName)
        return COMMON.NOT_FOUND, None

    # check for duplicates
    retcode, apps = settings_apps_list()

    if COMMON.OK != retcode:

        print('Err scanning current APPS')
        return retcode, None

    if appName in apps:
        print('App [' + appName + '] already defined')
        return retcode, None 

    # load INSTALLED_APPS
    retcode, section_content = settings_section_get('INSTALLED_APPS')

    if COMMON.OK != retcode:

        print('Err loading INSTALLED_APPS section')
        return retcode, None

    # Processing (LIST) type 
    section_content 
    section_content_str = '' 
    
    for line in section_content:
        
        # insert new app at the end
        if ']' in line:
            section_content_str += "    '" + appName + "'," + os.linesep

        section_content_str += line + os.linesep   

    retcode, section_content = settings_section_update('INSTALLED_APPS', section_content_str)

    # Exit
    if COMMON.OK == retcode:
        print( 'Section updated successfully' )
    else:
        print( 'Error updating section' )

    # Exit point 
    return retcode, section_content