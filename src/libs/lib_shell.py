import sys, os
from internal.exceptions import SyntaxError, PackageError, MemoryError, TypeError
import internal.formater as Formater
from internal.funcs import Funcs
funcs = Funcs()
class Shell:
    def execute(args: str, memory: dict):
        to_exec = ''
        if funcs.IsVar(args) and funcs.CheckVar(args, memory):
            to_exec = funcs.GetVar(args, memory)
            to_exec = Formater.FormatString(to_exec)
            os.system(to_exec)
        elif funcs.IsText(args):
            to_exec = args.strip('"')
            to_exec = Formater.FormatString(to_exec)
            os.system(to_exec)
        else:
            raise TypeError('Bad arguments format. \n                Argument can be variable or text value.')

    def start_cmd():
        os.system('cmd')

    def start_ps():
        os.system('powershell')

    def start_process(args: str, memory: dict):
        to_exec = ''
        if funcs.IsVar(args) and funcs.CheckVar(args, memory):
            to_exec = funcs.GetVar(args, memory)
            to_exec = Formater.FormatString(to_exec)
            os.system(f'start {to_exec}')
        elif funcs.IsText(args):
            to_exec = args.strip('"')
            to_exec = Formater.FormatString(to_exec)
            os.system(f'start {to_exec}')
        else:
            raise TypeError('Bad arguments format. \n                Argument can be variable or text value.')