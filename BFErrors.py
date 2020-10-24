#####################################################
#               BrainFuck Interpreter               #
#          File: BFErrors.py                        #
#        Author: Slone Wang                         #
#       Version: 1.0                                #
#    LastChange: 2020/10/24                         #
# Copyright © 2020 Slone Wang. All Rights Reserved. #
#####################################################

class InputError(Exception):
    def __init__(self, inputs:str):
        self.Input = inputs

    def __str__(self):
        return "\033[1;31mThe input character is not in ASCII.\nInput: {0}\n\033[0m".format(self.Input)

class NullPointerError(Exception):
    def __init__(self, code:str, index:int, pointer:int):
        self.Code = code
        self.Index = index
        self.Pointer = pointer

    def __str__(self):
        return "\033[1;31mThe pointer is pointing a null memory area.\n" + \
               "Max:{0}, Min:{1}, Now:{2}\n".format(65535, 0, self.Pointer) + \
               "{0}\033[4;31m{1}\033[0;31m{2}\n\033[0m".format(self.Code[:self.Index],\
                                                               self.Code[self.Index],\
                                                               self.Code[self.Index+1:])

class NonOperatorError(Exception):
    def __init__(self, code:str, index:int):
        self.Code = code
        self.Index = index

    def __str__(self):
        return "\033[1;31mThere is a non-operator character in codes.\n" + \
               "{0}\033[4;31m{1}\033[0;31m{2}\n\033[0m".format(self.Code[:self.Index],\
                                                               self.Code[self.Index],\
                                                               self.Code[self.Index+1:])

class DataOverLimiteError(Exception):
    def __init__(self, code:str, index:int, value:int):
        self.Code = code
        self.Index = index
        self.Value = value

    def __str__(self):
        return "\033[1;31mThe data is over the limitation (>127 or <0).\n" + \
               "Max:{0}, Min:{1}, Now:{2}\n".format(127, 0, self.Value) + \
               "{0}\033[4;31m{1}\033[0;31m{2}\n\033[0m".format(self.Code[:self.Index],\
                                                               self.Code[self.Index],\
                                                               self.Code[self.Index+1:])

class RepeatingError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "\033[1;31mThe repeaters' does not match.\n\033[0m"
