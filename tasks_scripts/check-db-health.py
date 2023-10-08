#!/usr/bin/env python
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os, sys

def main(argv):

    try:
        
        print(' EXEC -> ' + os.path.basename(__file__)) 

        for i in range(1, len(argv)):
            print('argument:', i, 'value:', argv[i])        

        # Unix ErrCode
        exit(0)

    except Exception as e:

        print( 'Err: ' + str( e ) )
        exit(1)

if __name__ == '__main__':
    main(sys.argv)
