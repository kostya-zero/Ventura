import sys, os, hashlib
from internal.exceptions import SyntaxError, PackageError, MemoryError, TypeError
import internal.formater as Formater
from internal.funcs import Funcs


Funcs = Funcs()


cpdef md5(args: str, memory: dict):
    if Funcs.IsVar(args) and Funcs.CheckVar(args, memory) and not args.startswith('$__'):
        if Funcs.IsTextVar(args, memory):
            word = memory[args]["value"]
            word = word.encode()
            word = hashlib.md5(word).hexdigest()
            memory[args]["value"] = word
            return memory
        else:
            raise TypeError('Variable are not text.')
    else:
        raise TypeError('Bad argument format. Variable not exists or its a reserved type.')


cpdef sha1(args: str, memory: dict):
    if Funcs.IsVar(args) and Funcs.CheckVar(args, memory) and not args.startswith('$__'):
        if Funcs.IsTextVar(args, memory):
            word = memory[args]["value"]
            word = word.encode()
            word = hashlib.sha1(word).hexdigest()
            memory[args]["value"] = word
            return memory
        else:
            raise TypeError('Variable are not text.')
    else:
        raise TypeError('Bad argument format. Variable not exists or its a reserved type.')


cpdef sha512(args: str, memory: dict):
    if Funcs.IsVar(args) and Funcs.CheckVar(args, memory) and not args.startswith('$__'):
        if Funcs.IsTextVar(args, memory):
            word = memory[args]["value"]
            word = word.encode()
            word = hashlib.sha512(word).hexdigest()
            memory[args]["value"] = word
            return memory
        else:
            raise TypeError('Variable are not text.')
    else:
        raise TypeError('Bad argument format. Variable not exists or its a reserved type.')
