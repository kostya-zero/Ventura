import sys, os
from internal.exceptions import SyntaxError, PackageError, TypeError, MemoryError
import internal.formater as Formater
from internal.funcs import Funcs


funcs = Funcs()


class Text:
    def init(args: str, memory: dict):
        if funcs.IsVar(args) and funcs.CheckVar(args, memory) and not args.startswith('$__'):
            memory[args]["type"] = 'text'
            memory[args]["value"] = ''
            return memory
        else:
            raise TypeError('Bad argument format. Variable not exists or its a reserved type.')


    def cls_all(args: str, memory: dict):
        if funcs.IsVar(args) and funcs.CheckVar(args, memory) and not args.startswith('$__'):
            if funcs.IsTextVar(args, memory):
                memory[args]["type"] = 'text'
                memory[args]["value"] = str(memory[args]["value"]).strip()
                return memory
            else:
                raise TypeError('Variable are not text. Initialize with "init" function.')
        else:
            raise TypeError('Bad argument format. Variable not exists or its a reserved type.')


    def cls_left(args: str, memory: dict):
        if funcs.IsVar(args) and funcs.CheckVar(args, memory) and not args.startswith('$__'):
            if funcs.IsTextVar(args, memory):
                memory[args]["type"] = 'text'
                memory[args]["value"] = str(memory[args]["value"]).lstrip()
                return memory
            else:
                raise TypeError('Variable are not text. Initialize with "init" function.')
        else:
            raise TypeError('Bad argument format. Variable not exists or its a reserved type.')


    def cls_right(args: str, memory: dict):
        if funcs.IsVar(args) and funcs.CheckVar(args, memory) and not args.startswith('$__'):
            if funcs.IsTextVar(args, memory):
                memory[args]["type"] = 'text'
                memory[args]["value"] = str(memory[args]["value"]).rstrip()
                return memory
            else:
                raise TypeError('Variable are not text. Initialize with "init" function.')
        else:
            raise TypeError('Bad argument format. Variable not exists or its a reserved type.')


    def replace(args: str, memory: dict):
        spl = args.split(',')
        var = spl[0].strip()
        w1 = spl[1].strip()
        w2 = spl[2].strip()

        if funcs.IsVar(var) and funcs.CheckVar(var, memory) and funcs.IsText(w1) and funcs.IsText(w2):
            pass
        else:
            raise TypeError('Bad argument format.')

        w1 = Formater.FormatString(w1.strip('"'))
        w2 = Formater.FormatString(w2.strip('"'))

        if not var.startswith('$__'):
            if funcs.IsTextVar(var, memory):
                memory[var]["type"] = 'text'
                memory[var]["value"] = str(memory[var]["value"]).replace(w1, w2)
                return memory
            else:
                raise TypeError('Variable are not text. Initialize with "init" function.')
        else:
            raise TypeError('Variable a reserved type.')


    def lower(args: str, memory: dict):
        if funcs.IsVar(args) and funcs.CheckVar(args, memory) and not args.startswith('$__'):
            if funcs.IsTextVar(args, memory):
                memory[args]["type"] = 'text'
                memory[args]["value"] = str(memory[args]["value"]).lower()
                return memory
            else:
                raise TypeError('Variable are not text. Initialize with "init" function.')
        else:
            raise TypeError('Bad argument format. Variable not exists or its a reserved type.')


    def upper(args: str, memory: dict):
        if funcs.IsVar(args) and funcs.CheckVar(args, memory) and not args.startswith('$__'):
            if funcs.IsTextVar(args, memory):
                memory[args]["type"] = 'text'
                memory[args]["value"] = str(memory[args]["value"]).upper()
                return memory
            else:
                raise TypeError('Variable are not text. Initialize with "init" function.')
        else:
            raise TypeError('Bad argument format. Variable not exists or its a reserved type.')
