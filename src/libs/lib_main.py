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
            arg = split[1].strip()
            if funcs.IsVar(arg):
                if funcs.CheckVar(arg, memory):
                    to_print = funcs.GetVar(arg, memory)
                    to_print = Formater.FormatString(to_print)
                    print(to_print)
                else:
                    raise MemoryError(f'Variable are not registred -> {arg}.')
            elif funcs.IsText(arg):
                to_print = arg.strip('"')
                to_print = Formater.FormatString(to_print)
                print(to_print)
            else:
                raise TypeError('Bad argument format.')

    def lnout(args: str, memory: dict):
        if args.count(':') == 0 or args.count(':') >= 2:
            raise PackageError(f'Function expression must have only one single ":".')
        else:
            split = args.split(':')
            arg = split[1].strip()
            if funcs.IsVar(arg):
                if funcs.CheckVar(arg):
                    to_print = funcs.GetVar(arg, memory)
                    to_print = Formater.FormatString(to_print)
                    print(to_print)
                else:
                    raise MemoryError(f'Variable are not registred -> {arg}.')
            elif funcs.IsText(arg):
                to_print = arg.strip('"')
                to_print = Formater.FormatString(to_print)
                print(to_print)
            else:
                raise TypeError('Bad argument format.')

    def sv(args: str, memory: dict):
        if args.count(':') == 0 or args.count(':') >= 2:
            raise PackageError(f'Function expression must have only one single ":".')
        else:
            split = args.split(':')
            args2 = split[1].strip()
            if args2.count(',') == 0 or args2.count(',') >= 2:
                raise PackageError(f'Function require 2 arguments.')
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
                                raise MemoryError(f'Variable are not registred -> {new_value}.')
                        elif funcs.IsText(new_value):
                            new_value = new_value.strip('"')
                            memory[var] = new_value
                            return memory
                        else:
                            raise TypeError('Bad argument format.')
                    else:
                        raise MemoryError(f'Variable are not registred -> {var}.')
                else:
                    raise TypeError('Bad argument format.')

    def exit():
        sys.exit()

    def void(args: str, memory: dict):
        if args.count(':') == 0 or args.count(':') >= 2:
            raise PackageError(f'Function expression must have only one single ":".')
        else:
            split = args.split(':')
            var = split[1].strip()
            if funcs.IsVar(var):
                if funcs.CheckVar(var, memory):
                    memory.pop(var)
                    return memory
                else:
                    raise MemoryError(f'Variable are not registred -> {var}.')
            else:
                raise TypeError('Bad argument format.')

    def zero(args: str, memory: dict):
        if args.count(':') == 0 or args.count(':') >= 2:
            raise PackageError(f'Function expression must have only one single ":".')
        else:
            split = args.split(':')
            var = split[1].strip()
            if funcs.IsVar(var):
                if funcs.CheckVar(var, memory):
                    memory[var] = ''
                    return memory
                else:
                    raise MemoryError(f'Variable are not registred -> {var}.')
            else:
                raise TypeError('Bad argument format.')

    def wipe():
        os.system('cls')

    def get_in(args: str, memory: dict):
        if args.count(':') == 0 or args.count(':') >= 2:
            raise PackageError(f'Function expression must have only one single ":".')
        else:
            split = args.split(':')
            var = split[1].strip()
            if funcs.IsVar(var):
                if funcs.CheckVar(var, memory):
                    memory[var] = input()
                    return memory
                else:
                    raise MemoryError(f'Variable are not registred -> {var}.')
            else:
                raise TypeError('Bad argument format.')

    def execute(args: str, memory: dict):
        if args.count(':') == 0 or args.count(':') >= 2:
            raise PackageError(f'Function expression must have only one single ":".')
        else:
            split = args.split(':')
            act = split[1].strip()
            if funcs.IsVar(act):
                if funcs.CheckVar(act, memory):
                    os.system(memory[act])
                else:
                    raise MemoryError(f'Variable are not registred -> {act}.')
            elif funcs.IsText(act):
                act = act.strip('"')
                os.system(act)
            else:
                raise TypeError('Bad argument format.')
