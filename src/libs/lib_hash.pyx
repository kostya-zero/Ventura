import sys, os, hashlib
from internal.exceptions import SyntaxError, PackageError, MemoryError, TypeError
import internal.formater as Formater
from internal.funcs import Funcs
Funcs = Funcs()
cpdef md5(args: str, memory: dict):
    if args.startswith('$') and not args.startswith('$__') and args in memory.keys():
        arg = memory[args]
        arg = arg.encode()
        arg = hashlib.md5(arg).hexdigest()
        memory[args] = arg
        return memory
    else:
        raise TypeError("Bad argument type.\n                Function require variable.")

cpdef sha1(args: str, memory: dict):
    if args.startswith('$') and not args.startswith('$__') and args in memory.keys():
        arg = memory[args]
        arg = arg.encode()
        arg = hashlib.sha1(arg).hexdigest()
        memory[args] = arg
        return memory
    else:
        raise TypeError("Bad argument type.\n                Function require variable.")

cpdef sha512(args: str, memory: dict):
    if args.startswith('$') and not args.startswith('$__') and args in memory.keys():
        arg = memory[args]
        arg = arg.encode()
        arg = hashlib.sha512(arg).hexdigest()
        memory[args] = arg
        return memory
    else:
        raise TypeError("Bad argument type.\n                Function require variable.")