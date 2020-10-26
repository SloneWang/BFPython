#####################################################
#               BrainFuck Interpreter               #
#          File: BFPython.py                        #
#        Author: Slone Wang                         #
#       Version: 1.1                                #
#    LastChange: 2020/10/26                         #
# Copyright © 2020 Slone Wang. All Rights Reserved. #
#####################################################

import sys
from BFInterpret import *
from BFHelp import *

def REPL():
    while(True):
        Codes = input("::")
        Interpret(Codes)

def FILE(BFFile:str):
    Codes = ''
    with open(BFFile) as BFSourceFile:
        for line in BFSourceFile:
            Codes += line
        else:
            Interpret(Codes)

def main(argv:list):
    if len(argv) > 1:
        if argv[1] == '--help' or argv[1] == '-h':
            help()
        elif argv[1].endswith('.bf'):
            FILE(argv[1])
    else:
        REPL()

if __name__ == "__main__":
    main(sys.argv)
