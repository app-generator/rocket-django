# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from util import *

'''
| ✅ | **Code basic structure** | `runner.py` (entry point) | - |
| ✅ | **Create a Django project** | `$ python runner.py` | Create & start new project `src` DIR |
| ❌ | **Add authentication** | `$ python runner.py XXX` | @Todo |
| ❌ | **Use SQLite** | `$ python runner.py XXX` | @Todo |
| ❌ | **Use MySql** | `$ python runner.py XXX` | @Todo |
| ❌ | **Docker** | `$ python runner.py docker <add/remove>` | Default argument: `add` |
| ❌ | **Themes List** | `$ python runner.py themes` | List all available themes |
| ❌ | **Theme Install** | `$ python runner.py theme volt` | Install `Volt` theme |
'''

ACTIONS = {
    'create' : ['NA'],
    'delete' : ['NA'],
    'start'  : ['NA'],
    'db'     : ['sqlite', 'mysql'],
    'auth'   : ['basic' , 'github', 'twitter'],
    'docker' : ['add'   , 'remove'],
}

def parse_input( sys_argv ):

    input_len  = len( sys_argv )
    input_argv = sys_argv

    COMMAND   = ''
    ARGUMENT  = None 

    if 1 == input_len:
        print( 'Usage: runner.py COMMAND Argument' )
        print( '  > COMMAND create: create a new project' )
        print( '  > COMMAND delete: delete the generated project' )
        print( '  > COMMAND db: set up SQLite or MySql' )
        print( '    "python runner.py db sqlite" -> activates SQLite persistence' )
        print( '    "python runner.py db mysql"  -> activates MySql persistence ' )
        print( '  > COMMAND auth: set up the authentication layer' )
        print( '    "python runner.py auth basic"  -> enables username/password persistence' )
        print( '    "python runner.py auth github" -> enables OAuth via Github' )
        print( '    "python runner.py auth twitter" -> enables OAuth via Twitter' )
        print( '  > COMMAND docker: add or remove Docker sctipts' )
        print( '    "python runner.py docker add" -> injects Docker support' )
        print( '    "python runner.py docker add" -> removes Docker support' )
        exit(0)

    COMMAND = input_argv[1].lower()

    if input_len > 2:
        ARGUMENT = input_argv[1].lower()

    if COMMAND not in ACTIONS.keys():

        print('ERR: Invalid command ['+COMMAND+']. Expected ' + str( ACTIONS.keys() ) )
        exit(1)

    if 'create' == COMMAND:

        project_create()
        exit(1)

    if 'start' == COMMAND:

        project_start()
        exit(1)

    if 'delete' == COMMAND:
        
        print('Delete SRC directory')
        dir_delete( DIR_SRC )
        print(' ...done')
        exit(1)

        project_start() 

    if 'db' == COMMAND:        
        print(' > Command not implemented')
        exit(1)

    if 'auth' == COMMAND:        
        print(' > Command not implemented')
        exit(1)

    if 'docker' == COMMAND:        
        print(' > Command not implemented')
        exit(1)        

# Entry point
if __name__ == "__main__": 
    parse_input( sys.argv )
