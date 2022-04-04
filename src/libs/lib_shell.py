import sys, os
from internal.exceptions import SyntaxError, PackageError, MemoryError, TypeError
import internal.formater as Formater
from internal.funcs import Funcs

funcs = Funcs()


class Shell:
    def execute(args: str, memory: dict):
        if funcs.IsVar(args):
            if funcs.IsTextVar(args, memory) and funcs.CheckVar(args, memory) and not args.startswith('$__'):
                obj = funcs.GetVar(args, memory)
                text = Formater.FormatString(obj["value"])
                os.system(text)
            else:
                raise TypeError('Variable not registred, not text or reserved type.')
        elif funcs.IsText(args):
            args = args.strip('"')
            args = Formater.FormatString(args)
            os.system(args)
        else:
            raise TypeError('Bad arguments format.')
