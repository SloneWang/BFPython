#####################################################
#               BrainFuck Interpreter               #
#          File: BFInterpret.py                     #
#        Author: Slone Wang                         #
#       Version: 1.1                                #
#    LastChange: 2020/10/26                         #
# Copyright © 2020 Slone Wang. All Rights Reserved. #
#####################################################

from BFErrors import *

Memories = bytearray(1)
Pointer = 0 #type:int

def InputChar():
    Char = input("||::")
    Code = ord(Char[0])
    if (Code > 127) or (Code < 0):
        raise InputError(Char)
    else:
        return Code

def Interpret(code:str):
    global Operators, Splitters, Memories, Pointer
    DepthRepeating = -1 #type:int
    temp_Memories = Memories
    temp_Pointer = Pointer #type:int
    PrintList = str()
    Codes = code #type:str
    Start_Repeat = list()
    End_Repeat = list()
    try:
        if Codes.count('[') != Codes.count(']'):
            raise RepeatingError()
        else:
            Index = 0
            while(Index < len(Codes)):
                c = Codes[Index]
                if c in ['>', '<', '+', '-', '.', ',', '[', ']']:
                    if c == '>':
                        if temp_Pointer+1 == len(temp_Memories):
                            temp_Memories += bytearray(1) 
                        temp_Pointer += 1
                    elif c == '<':
                        if temp_Pointer == 0:
                            raise NullPointerError(Codes, Index)
                        else:
                            temp_Pointer -= 1
                    elif c == '+':
                        if temp_Memories[temp_Pointer] == 127:
                            raise DataOverLimiteError(Codes, Index, temp_Memories[temp_Pointer])
                        else:
                            temp_Memories[temp_Pointer] += 1
                    elif c == '-':
                        if temp_Memories[temp_Pointer] == 0:
                            raise DataOverLimiteError(Codes, Index, temp_Memories[temp_Pointer])
                        else:
                            temp_Memories[temp_Pointer] -= 1
                    elif c == '.':
                        PrintList += chr(temp_Memories[temp_Pointer])
                    elif c == ',':
                        temp_Memories[temp_Pointer] = InputChar()
                    elif c == '[':
                        DepthRepeating += 1
                        Start_Repeat += [Index]
                    elif c == ']':
                        if DepthRepeating > -1:
                            if temp_Memories[temp_Pointer] != 0:
                                Index = Start_Repeat[DepthRepeating]
                            else:
                                DepthRepeating -= 1
                                Start_Repeat = Start_Repeat[:-1]
                        else:
                            raise RepeatingError()
                elif c in [' ', '\t', '\n']:
                    pass
                else:
                    raise NonOperatorError(Codes, Index)
                Index += 1
            else:
                Memories = temp_Memories
                Pointer = temp_Pointer
                print(PrintList, sep = '', end = '')
    except Exception as Error:
        print(Error)