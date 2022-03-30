import sys, os
from internal.exceptions import SyntaxError, PackageError, MemoryError, TypeError
import internal.formater as Formater
from internal.funcs import Funcs
funcs = Funcs()
class Main:
    def out(args: str, memory: dict):
        if args.count(':') == 0 or args.count(':') >= 2:
            raise PackageError(f'Function expression must have only one single ":".')
        else:
            split = args.split(':')
            if split[1].strip().startswith('(') and split[1].strip().endswith(')'):
                pass
            else:
                raise TypeError("Arguments must be in brackets. New in 1.3 version.")
            arg = split[1].strip()
            arg = arg.lstrip('(')
            arg = arg.rstrip(')')
            arg = arg.strip()
            if funcs.IsVar(arg):
                if funcs.CheckVar(arg, memory):
                    to_print = funcs.GetVar(arg, memory)
                    to_print = Formater.FormatString(to_print)
                    print(to_print)
                else:
                    raise MemoryError(f'Variable are not registred -> {arg}. \n                Try write above ";entry" line ";new ${arg.lstrip("$")}".')

            elif funcs.IsText(arg):
                to_print = arg.strip('"')
                to_print = Formater.FormatString(to_print)
                print(to_print)
            else:
                raise TypeError('Bad argument format. \n                Argument can be variable or text value.')

    def lnout(args: str, memory: dict):
        if args.count(':') == 0 or args.count(':') >= 2:
            raise PackageError(f'Function expression must have only one single ":".')
        else:
            split = args.split(':')
            if split[1].strip().startswith('(') and split[1].strip().endswith(')'):
                pass
            else:
                raise TypeError("Arguments must be in brackets. New in 1.3 version.")
            arg = split[1].strip()
            arg = arg.lstrip('(')
            arg = arg.rstrip(')')
            arg = arg.strip()
            if funcs.IsVar(arg):
                if funcs.CheckVar(arg):
                    to_print = funcs.GetVar(arg, memory)
                    to_print = Formater.FormatString(to_print)
                    print(to_print)
                else:
                    raise MemoryError(f'Variable are not registred -> {arg}. \n                Try write above ";entry" line ";new ${arg.lstrip("$")}".')
            elif funcs.IsText(arg):
                to_print = arg.strip('"')
                to_print = Formater.FormatString(to_print)
                print(to_print)
            else:
                raise TypeError('Bad argument format. \n                Argument can be variable or text value.')

    def sv(args: str, memory: dict):
        if args.count(':') == 0 or args.count(':') >= 2:
            raise PackageError(f'Function expression must have only one single ":".')
        else:
            split = args.split(':')
            if split[1].strip().startswith('(') and split[1].strip().endswith(')'):
                pass
            else:
                raise TypeError("Arguments must be in brackets. New in 1.3 version.")
            args2 = split[1].strip()
            args2 = args2.lstrip('(')
            args2 = args2.rstrip(')')
            args2 = args2.strip()
            if args2.count(',') == 0 or args2.count(',') >= 2:
                raise PackageError(f'Function require 2 arguments. \n                Variable and value (text or variable).')
            else:
                split_arg = args2.split(',')
                var = split_arg[0].strip()
                new_value = split_arg[1].strip()
                if funcs.IsVar(var):
                    if funcs.CheckVar(var, memory):
                        if funcs.IsVar(new_value):
                            if funcs.CheckVar(new_value, memory):
                                memory[var] = memory[new_value]
                                return memory
                            else:
                                raise MemoryError(f'Variable are not registred -> {new_value}. \n                Try write above ";entry" line ";new ${new_value.lstrip("$")}".')
                        elif funcs.IsText(new_value):
                            new_value = new_value.strip('"')
                            memory[var] = new_value
                            return memory
                        else:
                            raise TypeError('Bad argument format. \n                Argument can be variable or text value.')
                    else:
                        raise MemoryError(f'Variable are not registred -> {var}. \n                Try write above ";entry" line ";new ${var.lstrip("$")}".')
                else:
                    raise TypeError('Bad argument format. \n                Argument can be variable or text value.')

    def exit():
        sys.exit()

    def void(args: str, memory: dict):
        if args.count(':') == 0 or args.count(':') >= 2:
            raise PackageError(f'Function expression must have only one single ":".')
        else:
            split = args.split(':')
            if split[1].strip().startswith('(') and split[1].strip().endswith(')'):
                pass
            else:
                raise TypeError("Arguments must be in brackets. New in 1.3 version.")
            var = split[1].strip()
            var = var.lstrip('(')
            var = var.rstrip(')')
            var = var.strip()
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
            var = split[1].strip()
            var = var.lstrip('(')
            var = var.rstrip(')')
            var = var.strip()
            if funcs.IsVar(var):
                if funcs.CheckVar(var, memory):
                    memory[var] = ''
                    return memory
                else:
                    raise MemoryError(f'Variable are not registred -> {var}. \n                Try write above ";entry" line ";new ${var.lstrip("$")}".')
            else:
                raise TypeError('Bad argument format. \n                Argument can be variable or text value.')

    def wipe():
        os.system('cls')

    def get_in(args: str, memory: dict):
        if args.count(':') == 0 or args.count(':') >= 2:
            raise PackageError(f'Function expression must have only one single ":".')
        else:
            split = args.split(':')
            if split[1].strip().startswith('(') and split[1].strip().endswith(')'):
                pass
            else:
                raise TypeError("Arguments must be in brackets. New in 1.3 version.")
            var = split[1].strip()
            var = var.lstrip('(')
            var = var.rstrip(')')
            var = var.strip()
            if funcs.IsVar(var):
                if funcs.CheckVar(var, memory):
                    memory[var] = input()
                    return memory
                else:
                    raise MemoryError(f'Variable are not registred -> {var}. \n                Try write above ";entry" line ";new ${var.lstrip("$")}".')
            else:
                raise TypeError('Bad argument format. \n                Argument can be variable or text value.')

    def execute(args: str, memory: dict):
        if args.count(':') == 0 or args.count(':') >= 2:
            raise PackageError(f'Function expression must have only one single ":".')
        else:
            split = args.split(':')
            if split[1].strip().startswith('(') and split[1].strip().endswith(')'):
                pass
            else:
                raise TypeError("Arguments must be in brackets. New in 1.3 version.")
            act = split[1].strip()
            act = act.lstrip('(')
            act = act.rstrip(')')
            act = act.strip()
            if funcs.IsVar(act):
                if funcs.CheckVar(act, memory):
                    os.system(memory[act])
                else:
                    raise MemoryError(f'Variable are not registred -> {act}. \n                Try write above ";entry" line ";new ${act.lstrip("$")}".')
            elif funcs.IsText(act):
                act = act.strip('"')
                os.system(act)
            else:
                raise TypeError('Bad argument format. \n                Argument can be variable or text value.')
