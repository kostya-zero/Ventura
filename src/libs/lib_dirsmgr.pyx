from os import path, mkdir, rmdir
from shutil import rmtree
from internal.exceptions import SyntaxError, PackageError, MemoryError, TypeError
import internal.formater as Formater
from internal.funcs import Funcs


Funcs = Funcs()


cpdef mk(args: str, memory: dict):
    if Funcs.IsVar(args):
        if Funcs.CheckVar(args, memory) and Funcs.IsTextVar(args, memory):
            path = memory[args]["value"]
            mkdir(path)
        else:
            raise TypeError('Variable are not located or its not text type.')
    elif Funcs.IsText(args):
        args = args.strip('"')
        args = Formater.FormatString(args)
        mkdir(args)
    else:
        raise TypeError('Variable are not located or its not text type.')


cpdef rm(args: str, memory: dict):
    if Funcs.IsVar(args):
        if Funcs.CheckVar(args, memory) and Funcs.IsTextVar(args, memory):
            path = memory[args]["value"]
            rmdir(path)
        else:
            raise TypeError('Variable are not located or its not text type.')
    elif Funcs.IsText(args):
        args = args.strip('"')
        args = Formater.FormatString(args)
        rmdir(args)
    else:
        raise TypeError('Variable are not located or its not text type.')


cpdef rm_tree(args: str, memory: dict):
    if Funcs.IsVar(args):
        if Funcs.CheckVar(args, memory) and Funcs.IsTextVar(args, memory):
            path = memory[args]["value"]
            rmtree(path)
        else:
            raise TypeError('Variable are not located or its not text type.')
    elif Funcs.IsText(args):
        args = args.strip('"')
        args = Formater.FormatString(args)
        rmtree(args)
    else:
        raise TypeError('Variable are not located or its not text type.')
