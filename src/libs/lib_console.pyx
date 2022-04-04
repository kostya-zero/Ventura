import sys, os
from platform import architecture
from internal.exceptions import SyntaxError, PackageError, MemoryError, TypeError
import internal.formater as Formater
from internal.funcs import Funcs


Funcs = Funcs()


cpdef write(args: str, memory: dict):
    if Funcs.IsVar(args) and Funcs.CheckVar(args, memory):
        if Funcs.IsTextVar(args, memory):
            text = memory[args]["value"]
            print(text)
        else:
            raise TypeError('console: Variable must be a text.')
    elif Funcs.IsText(args):
        text = args.strip('"')
        text = Formater.FormatString(text)
        print(text)
    else:
        raise TypeError('console: Bad argument format.')


cpdef clear():
    if architecture()[1] == "WindowsPE":
        os.system('cls')
    else:
        os.system('clear')


cpdef message(args: str, memory: dict):
    if Funcs.IsVar(args) and Funcs.CheckVar(args, memory):
        if Funcs.IsTextVar(args, memory):
            text = memory[args]["value"]
            print(text)
        else:
            raise TypeError('console: Variable must be a text.')
    elif Funcs.IsText(args):
        text = args.strip('"')
        text = Formater.FormatString(text)
        print(f'[MESSAGE]: {text}')
    else:
        raise TypeError('console: Bad argument format.')


cpdef error(args: str, memory: dict):
    if Funcs.IsVar(args) and Funcs.CheckVar(args, memory):
        if Funcs.IsTextVar(args, memory):
            text = memory[args]["value"]
            print(text)
        else:
            raise TypeError('console: Variable must be a text.')
    elif Funcs.IsText(args):
        text = args.strip('"')
        text = Formater.FormatString(text)
        print(f'[ERROR]: {text}')
    else:
        raise TypeError('console: Bad argument format.')


cpdef warning(args: str, memory: dict):
    if Funcs.IsVar(args) and Funcs.CheckVar(args, memory):
        if Funcs.IsTextVar(args, memory):
            text = memory[args]["value"]
            print(text)
        else:
            raise TypeError('console: Variable must be a text.')
    elif Funcs.IsText(args):
        text = args.strip('"')
        text = Formater.FormatString(text)
        print(f'[WARNING]: {text}')
    else:
        raise TypeError('console: Bad argument format.')
