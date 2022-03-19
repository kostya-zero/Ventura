import sys, os
from internal.exceptions import SyntaxError, PackageError, MemoryError, TypeError
import internal.formater as Formater
from internal.funcs import Funcs
funcs = Funcs()
class Shell:
    def execute(args: str, memory: dict):
        if funcs.IsVar(args) and funcs.CheckVar(args, memory):
            exec = funcs.GetVar(args, memory)
            exec = Formater.FormatString(exec)
            os.system(exec)
        elif funcs.IsText(args):
            exec = args.strip('"')
            exec = Formater.FormatString(exec)
            os.system(exec)
        else:
            raise TypeError('Bad arguments format.')

    def start_cmd():
        os.system('cmd')

    def start_ps():
        os.system('powershell')