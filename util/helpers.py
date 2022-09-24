# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os
import shutil
import fnmatch
import json

from .common  import *

def hello():
    print(' > Test ' + errInfo( COMMON.OK ) )

def dir_exists( path ):

    try:

        if os.path.exists( path) and os.path.isdir( path) :
            return True
        else:
            return False
        
    except:
        print ( ' *** DIR not found = ' + path )
        return False    

def dir_create( path ):

    if dir_exists( path ):
        print ( ' *** DIR exists = ' + path )
        return False    

    try:

        os.mkdir(path)
        return True
        
    except Exception as e:
        print ( ' *** Err creating DIR: ' + str(e) )
        return False    

def dir_copy(src, dst, symlinks=False, ignore=None):

    try:

        # Create destination 
        if not dir_exists( dst ):
            dir_create( dst )

        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, symlinks, ignore)
            else:
                shutil.copy2(s, d)

        return True

    except Exception as e:
        print ( ' *** Err copy DIR: ' + str(e) )
        return False 

def dir_subdirs( path ):

    # this includes also path
    all_dirs = [x[0] for x in os.walk( path )]    

    if path in all_dirs:
        all_dirs.remove( path )

    return all_dirs    
    
def file_exists( path ):

    try:

        if open( path, 'r'):
            print ( ' *** File exists = ' + path )
            return True

    except:
        print ( ' *** File not found = ' + path )
        return False    

def file_read( path, encoding='utf8' ):

    try:

        f = open( path, 'r', encoding=encoding)
        if f:

            content = f.read()    
            
            f.close()
            return content

    except UnicodeDecodeError as err:

        print(" *** UnicodeDecodeError: {0}".format(err))
        return None

    except:

        print (' *** Err loading file: ' + str(path) )
        return None

def file_load( path, as_list=False ):

    try:

        f = open( path, 'r')
        if f:

            if as_list:
                content = f.readlines()
            else:
                content = f.read()    
            
            f.close()
            return content

    except UnicodeDecodeError as err:

        print(" *** UnicodeDecodeError: {0}".format(err))

    except:

        print (' *** Err loading file: ' + str(path) )
        return None

def file_write( file_path, new_content, f_append=False ): 

    try:

        f = None

        if file_exists( file_path ):
            if f_append:    
                f = open( file_path, 'a+')
            else:
                f = open( file_path, 'w+')    
        else:
            f = open( file_path, 'w+')

        if not f:
            #'Err open file'
            return False

        f.seek(0) 
        f.write( new_content )
        f.truncate()

        f.close()
        return True

    except IOError:

        print( 'ERR file_write(): File IOError: ' + file_path )
        return False

    except:

        print ( ' *** Err processing file ' + str(file_path) )
        return False

def file_append( file_path, new_content):

    #print ( 'append content to file ' + file_path )
    return file_write( file_path, new_content, True ) 

def file_print( file_path ):

    try:

        f = open( file_path, 'r')
        if f:
            for line in f.readlines():
                print ( line.rstrip() )

        return True

    except:

        print ( ' *** Err loading file ' + str(file_path) )
        return False

def file_find( aDir, aFileName ):

    retCode      = COMMON.OK
    errorInfo    = 'NA'
    file_content = None
    DIR_LIST     = []

    # Validate Input
    if not os.path.isdir( aDir ):
        return COMMON.INPUT_ERR, 'Input not DIR = ' + aDir, None

    # Get all subdirs
    DIR_LIST.extend( get_subdirs( aDir ) )

    # Iterate on Dirs
    for d in DIR_LIST:

        # Iterate on files
        for f in get_files(d, '*'):
            
            #print ( 'Compare [' + aFileName + '] -> [' + f + ']' )

            # Files muct match a FULL_PATH
            if f.endswith(aFileName):
                return COMMON.OK, errorInfo, file_load( f )            

    return COMMON.NOT_FOUND, 'File not found = ' + aFileName, None

def files_get(dir_to_scan, ext='*'):

    matches = []

    for root, dirnames, filenames in os.walk( dir_to_scan ):

        for filename in fnmatch.filter(filenames, '*.'+ ext):

            item = os.path.join(root, filename)

            #print ' **** type(item) = ' + str( type ( item ) )
            matches.append( item )

    return matches
