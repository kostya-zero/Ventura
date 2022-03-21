import sys, os, shutil
from internal.exceptions import SyntaxError, PackageError, MemoryError, TypeError
import internal.formater as Formater
from internal.funcs import Funcs
Funcs = Funcs()
cpdef mk(args: str, memory: dict):
    if Funcs.IsVar(args) and Funcs.CheckVar(args, memory):
        args = Funcs.GetVar(args, memory)
        if os.path.exists(args):
            raise PackageError("Directory with same name already exist.")
        else:
            os.mkdir(args)
    elif Funcs.IsText(args):
        args = args.strip('"')
        args = Formater.FormatString(args)
        if os.path.exists(args):
            raise PackageError("Directory with same name already exist.")
        else:
            os.mkdir(args)
    else:
        raise TypeError("Bad argument type.\n                Function require text or variable as argument.")

cpdef rm(args: str, memory: dict):
    if Funcs.IsVar(args) and Funcs.CheckVar(args, memory):
        args = Funcs.GetVar(args, memory)
        if os.path.exists(args):
            os.rmdir(args)
        else:
            raise PackageError(f"Cant find directory at path: {args}")
    elif Funcs.IsText(args):
        args = args.strip('"')
        args = Formater.FormatString(args)
        if os.path.exists(args):
            os.rmdir(args)
        else:
            raise PackageError(f"Cant find directory at path: {args}")
    else:
        raise TypeError("Bad argument type.\n                Function require text or variable as argument.")

cpdef rm_tree(args: str, memory: dict):
    if Funcs.IsVar(args) and Funcs.CheckVar(args, memory):
        args = Funcs.GetVar(args, memory)
        if os.path.exists(args):
            shutil.rmtree(args)
        else:
            raise PackageError(f"Cant find directory at path: {args}")
    elif Funcs.IsText(args):
        args = args.strip('"')
        args = Formater.FormatString(args)
        if os.path.exists(args):
            shutil.rmtree(args)
        else:
            raise PackageError(f"Cant find directory at path: {args}")
    else:
        raise TypeError("Bad argument type.\n                Function require text or variable as argument.")