import sys, os, platform
from internal.exceptions import SyntaxError, PackageError, MemoryError, TypeError
import internal.formater as Formater
from internal.funcs import Funcs
Funcs = Funcs()
cpdef envvar(args: str, memory: dict):
    if args.count(',') == 1:
        split = args.split(',')
        arg1 = split[0].strip()
        arg2 = split[1].strip()
        if arg1.startswith('$') and arg1 in memory.keys():
            arg1 = memory[arg1]
        elif Funcs.IsText(arg1):
            arg1 = arg1.strip('"')
            arg1 = Formater.FormatString(arg1)
        else:
            raise TypeError("Bad argument type.\n                First argument of function require text or variable.")

        if arg1.startswith('$') and not arg1.startswith('$__') and arg1 in memory.keys():
            arg1 = memory[arg1]
        else:
            raise TypeError("Bad argument type.\n                First argument of function require text or variable.")

        var = os.environ[arg1]
        memory[arg2] = var
        return memory
    else:
        raise TypeError("Bad argument type.\n                Function require 2 arguments.")

cpdef os_ver(args: str, memory: dict):
    if args.startswith('$') and not args.startswith('$__') and args in memory.keys():
        memory[args] = platform.version()
        return memory
    else:
        raise TypeError("Bad argument type.\n                Function require variable.")

cpdef os_release(args: str, memory: dict):
    if args.startswith('$') and not args.startswith('$__') and args in memory.keys():
        memory[args] = platform.release()
        return memory
    else:
        raise TypeError("Bad argument type.\n                Function require variable.")

cpdef os_type(args: str, memory: dict):
    if args.startswith('$') and not args.startswith('$__') and args in memory.keys():
        memory[args] = platform.system()
        return memory
    else:
        raise TypeError("Bad argument type.\n                Function require variable.")

cpdef os_cpu(args: str, memory: dict):
    if args.startswith('$') and not args.startswith('$__') and args in memory.keys():
        memory[args] = platform.processor()
        return memory
    else:
        raise TypeError("Bad argument type.\n                Function require variable.")

cpdef os_machine(args: str, memory: dict):
    if args.startswith('$') and not args.startswith('$__') and args in memory.keys():
        memory[args] = platform.machine()
        return memory
    else:
        raise TypeError("Bad argument type.\n                Function require variable.")