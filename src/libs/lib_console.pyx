import sys, os
from internal.exceptions import SyntaxError, PackageError
import internal.formater as Formater
from internal.funcs import Funcs
Funcs = Funcs()
cpdef write(args: str, memory: dict):
    cdef str to_print = ''
    if Funcs.IsVar(args) and Funcs.CheckVar(args, memory):
        to_print = Funcs.GetVar(args, memory)
        to_print = Formater.FormatString(args)
        print(to_print)
    elif Funcs.IsText(args):
        to_print = Formater.FormatString(args)
        to_print = to_print.strip('"')
        print(to_print)
    else:
        raise TypeError('Bad argument format.')

cpdef clear():
    os.system('cls')

cpdef message(args: str, memory: dict):
    cdef str to_print = ''
    if Funcs.IsVar(args) and Funcs.CheckVar(args, memory):
        to_print = Funcs.GetVar(args, memory)
        to_print = Formater.FormatString(args)
        print(to_print)
    elif Funcs.IsText(args):
        to_print = Formater.FormatString(args)
        to_print = to_print.strip('"')
        print('[MESSAGE]: ' + to_print)
    else:
        raise TypeError('Bad argument format.')

cpdef error(args: str, memory: dict):
    cdef str to_print = ''
    if Funcs.IsVar(args) and Funcs.CheckVar(args, memory):
        to_print = Funcs.GetVar(args, memory)
        to_print = Formater.FormatString(args)
        print(to_print)
    elif Funcs.IsText(args):
        to_print = Formater.FormatString(args)
        to_print = to_print.strip('"')
        print('[ERROR]: ' + to_print)
    else:
        raise TypeError('Bad argument format.')

cpdef warning(args: str, memory: dict):
    cdef str to_print = ''
    if Funcs.IsVar(args) and Funcs.CheckVar(args, memory):
        to_print = Funcs.GetVar(args, memory)
        to_print = Formater.FormatString(args)
        print(to_print)
    elif Funcs.IsText(args):
        to_print = Formater.FormatString(args)
        to_print = to_print.strip('"')
        print('[WARNING]: ' + to_print)
    else:
        raise TypeError('Bad argument format.')