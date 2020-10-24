#####################################################
#               BrainFuck Interpreter               #
#          File: BFPython.py                        #
#        Author: Slone Wang                         #
#       Version: 1.0                                #
#    LastChange: 2020/10/24                         #
# Copyright © 2020 Slone Wang. All Rights Reserved. #
#####################################################

import sys
from BFInterpret import *
from BFHelp import *

def main(argv:list):
    if len(argv) > 1:
        if argv[1] == '--help' or argv[1] == '-h':
            help()
        elif argv[1].endswith('.bf'):
            Codes = ''
            with open(argv[1]) as BFSourceFile:
                for line in BFSourceFile:
                    Codes += line
                else:
                    Interpret(Codes)
    else:
        while(True):
            Codes = input("::")
            try:
                Interpret(Codes)
            except Exception as Error:
                print(Error)
                continue

if __name__ == "__main__":
    main(sys.argv)
