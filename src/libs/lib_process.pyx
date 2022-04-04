import sys, os
from subprocess import run, getoutput
from internal.exceptions import SyntaxError, PackageError, MemoryError, TypeError
import internal.formater as Formater
from internal.funcs import Funcs

Funcs = Funcs()

cpdef start(args: str, memory: dict):
    if Funcs.IsVar(args):
        if Funcs.IsTextVar(args, memory) and Funcs.CheckVar(args, memory) and not args.startswith('$__'):
            text = Formater.FormatString(memory[args]["value"])
            run(text)
        else:
            raise TypeError('Variable not registered, not text or reserved type.')
    elif Funcs.IsText(args):
        args = args.strip('"')
        args = Formater.FormatString(args)
        run(args)
    else:
        raise TypeError('Bad arguments format.')


cpdef getout(args: str, memory: dict):
    if args.count(',') != 1:
        raise TypeError('Bad arguments format.')
    else:
        spl = args.split(',')
        var = spl[0].strip()
        cmd = spl[1].strip()

        if Funcs.IsVar(var):
            if Funcs.IsTextVar(var, memory) and Funcs.CheckVar(var, memory) and not var.startswith('$__'):
                text = Formater.FormatString(memory[var]["value"])
                var = text
            else:
                raise TypeError('Variable not registered, not text or reserved type.')
        else:
            raise TypeError('Bad arguments format.')

        if Funcs.IsVar(cmd):
            if Funcs.IsTextVar(cmd, memory) and Funcs.CheckVar(cmd, memory) and not cmd.startswith('$__'):
                text = Formater.FormatString(memory[cmd]["value"])
                cmd = text
            else:
                raise TypeError('Variable not registered, not text or reserved type.')
        elif Funcs.IsText(cmd):
            cmd = cmd.strip('"')
            cmd = Formater.FormatString(cmd)
        else:
            raise TypeError('Bad arguments format.')

        out = getoutput(cmd)
        memory[var]["value"] = out
        return memory
