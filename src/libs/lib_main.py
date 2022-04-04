import sys, os
from internal.exceptions import SyntaxError, PackageError, MemoryError, TypeError
import internal.formater as Formater
from platform import architecture
from internal.funcs import Funcs
funcs = Funcs()
class Main:
    def out(args: str, memory: dict):
        if args.count(':') != 1:
            raise PackageError(f'Function expression must have only one single ":".')
        else:
            split = args.split(':')
            arg = split[1].strip().lstrip('(').rstrip(')').strip()
            if funcs.IsVar(arg):
                if funcs.CheckVar(arg, memory):
                    if funcs.IsTextVar(arg, memory):
                        obj = funcs.GetVar(arg, memory)
                        text = Formater.FormatString(obj["value"])
                        print(text)
                    else:
                        raise TypeError('You can output only text variables.')
                else:
                    raise MemoryError(f'Variable "{arg}" are not located in memory.')
            elif funcs.IsText(arg):
                arg = arg.strip('"')
                arg = Formater.FormatString(arg)
                print(arg)
            else:
                raise TypeError('Bad arguments format.')

    def lnout(args: str, memory: dict):
        if args.count(':') != 1:
            raise PackageError(f'Function expression must have only one single ":".')
        else:
            split = args.split(':')
            arg = split[1].strip().lstrip('(').rstrip(')').strip()
            if funcs.IsVar(arg):
                if funcs.CheckVar(arg, memory):
                    if funcs.IsTextVar(arg, memory):
                        obj = funcs.GetVar(arg, memory)
                        text = Formater.FormatString(obj["value"])
                        print(text)
                    else:
                        raise TypeError('You can output only text variables.')
                else:
                    raise MemoryError(f'Variable "{arg}" are not located in memory.')
            elif funcs.IsText(arg):
                arg = arg.strip('"')
                arg = Formater.FormatString(arg)
                print(arg)
            else:
                raise TypeError('Bad arguments format.')

    def sv(args: str, memory: dict):
        if args.count(':') != 1:
            raise PackageError(f'Function expression must have only one single ":".')
        else:
            split = args.split(':')
            arg = split[1].strip().lstrip('(').rstrip(')').strip()
            if arg.count(',') != 1:
                raise PackageError(f'Function require 2 arguments.')
            else:
                sp = arg.split(',')
                var = sp[0].strip()
                val = sp[1].strip()
                if funcs.IsVar(var) and funcs.CheckVar(var, memory) and not var.startswith('$__'):
                    if funcs.IsTextVar(var, memory) and funcs.IsText(val):
                        memory[var]["value"] = val.strip('"')
                        return memory
                    elif funcs.IsTextVar(val, memory) and funcs.IsVar(val) and funcs.CheckVar(val, memory) and memory[val]["type"] == "text":
                        memory[var]["value"] = memory[val]["value"]
                        return memory
                    else:
                        raise TypeError('Variable type doesnt match new value type.')
                else:
                    raise MemoryError(f'Variable "{var}" are not located in memory or its reserved variable.')

    def exit():
        sys.exit()

    def void(args: str, memory: dict):
        if args.count(':') == 0 or args.count(':') >= 2:
            raise PackageError(f'Function expression must have only one single ":".')
        else:
            split = args.split(':')
            var = split[1].strip().lstrip('(').rstrip(')').strip()
            if funcs.IsVar(var):
                if funcs.CheckVar(var, memory):
                    memory.pop(var)
                    return memory
                else:
                    raise MemoryError(f'Variable are not registred -> {var}. \n                Try write above ";entry" line ";new ${var.lstrip("$")}".')
            else:
                raise TypeError('Bad argument format. \n                Argument can be variable or text value.')

    def zero(args: str, memory: dict):
        if args.count(':') == 0 or args.count(':') >= 2:
            raise PackageError(f'Function expression must have only one single ":".')
        else:
            split = args.split(':')
            if split[1].strip().startswith('(') and split[1].strip().endswith(')'):
                pass
            else:
                raise TypeError("Arguments must be in brackets. New in 1.3 version.")
            var = split[1].strip().lstrip('(').rstrip(')').strip()
            if funcs.IsVar(var):
                if funcs.CheckVar(var, memory) and not var.startswith('$__'):
                    memory[var]["value"] = ''
                    return memory
                else:
                    raise MemoryError(f'Variable "{var}" are not located in memory or its reserved variable.')
            else:
                raise TypeError('Bad argument format. \n                Argument can be variable or text value.')

    def wipe():
        if architecture()[1] == "WindowsPE":
            os.system('cls')
        else:
            os.system('clear')

    def get_in(args: str, memory: dict):
        if args.count(':') == 0 or args.count(':') >= 2:
            raise PackageError(f'Function expression must have only one single ":".')
        else:
            split = args.split(':')
            var = split[1].strip().lstrip('(').rstrip(')').strip()
            if funcs.IsVar(var) and funcs.CheckVar(var, memory) and not var.startswith('$__'):
                if funcs.IsTextVar(var, memory):
                    memory[var]["value"] = input()
                    return memory
                else:
                    raise TypeError('You can use only text variables.')
            else:
                raise MemoryError(f'Variable "{var}" are not located in memory or its reserved variable.')

    def execute(args: str, memory: dict):
        if args.count(':') == 0 or args.count(':') >= 2:
            raise PackageError(f'Function expression must have only one single ":".')
        else:
            split = args.split(':')
            cmd = split[1].strip().lstrip('(').rstrip(')').strip()
            if funcs.IsVar(cmd) and funcs.CheckVar(cmd, memory) and not cmd.startswith('$__'):
                if funcs.IsTextVar(cmd, memory):
                    os.system(memory[cmd]["value"])
                else:
                    raise TypeError('You can use only text variables.')
            elif funcs.IsText(cmd):
                cmd = cmd.strip('"')
                cmd = Formater.FormatString(cmd)
                os.system(cmd)
            else:
                raise TypeError(f'Bad arguments format.')
