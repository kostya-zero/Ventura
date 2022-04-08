from os import path, mkdir, rmdir
from shutil import rmtree
from internal.exceptions import SyntaxError, PackageError, MemoryError, TypeError
import internal.formater as Formater
from internal.funcs import Funcs


Funcs = Funcs()


class Num:
    cpdef init(args: str, memory: dict):
        if Funcs.IsVar(args) and Funcs.CheckVar(args, memory) and not args.startswith('$__'):
            memory[args]["type"] = 'num'
            memory[args]["value"] = 0
            return memory
        else:
            raise TypeError('Bad argument format. Variable not exists or its a reserved type.')

    cpdef set(args: str, memory: dict):
        if args.count(',') != 1:
            raise TypeError('Function require 2 arguments!')
        else:
            pass

        split = args.split(',')
        var = split[0].strip()
        value = split[1].strip()

        if Funcs.IsVar(var) and Funcs.CheckVar(var, memory) and not var.startswith('$__'):
            pass
        else:
            raise TypeError('Bad argument format. Variable not exists or its a reserved type.')

        if Funcs.IsNumber(value):
            value = int(value.lstrip('*'))
        elif Funcs.IsVar(value) and Funcs.CheckVar(value, memory):
            if memory[value]["type"] == 'num':
                value = memory[value]["value"]
        else:
            raise TypeError('Bad argument. Number required')

        memory[var]["value"] = value
        return memory