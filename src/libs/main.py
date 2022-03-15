import sys, os
from internal.exceptions import SyntaxError, PackageError, TypeError, MemoryError
from internal.formater import Formater
from internal.funcs import Funcs
class Main:
    def out(args: str, memory: dict):
        if args.count(':') == 0 or args.count(':') >= 2:
            raise PackageError(f'Function expression must have only one single ":".')
        else:
            split = args.split(':')
            arg = split[1].strip()
            if arg.startswith('"') and arg.endswith('"'):
                arg = Formater.ClearWhitespaces(arg)
                arg = arg.strip('"')
                arg = Formater.FormatString(arg)
                print(arg, end='')
            elif arg.startswith('$'):
                if arg in memory.keys():
                    print(memory[arg], end='')
                else:
                    raise MemoryError(f'Variable are not registred -> {arg}.')
            else:
                raise TypeError('Bad argument format.')

    def lnout(args: str, memory: dict):
        if args.count(':') == 0 or args.count(':') >= 2:
            raise PackageError(f'Function expression must have only one single ":".')
        else:
            split = args.split(':')
            arg = split[1].strip()
            if arg.startswith('"') and arg.endswith('"'):
                arg = Formater.ClearWhitespaces(arg)
                arg = arg.strip('"')
                arg = Formater.FormatString(arg)
                print(arg, end='\n')
            elif arg.startswith('$'):
                if arg in memory.keys():
                    print(memory[arg], end='\n')
                else:
                    raise MemoryError(f'Variable are not registred -> {arg}.')
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
                if var.startswith('$'):
                    if var in memory.keys():
                        if new_value.startswith('$'):
                            if new_value in memory.keys():
                                memory[var] = memory[new_value]
                                return memory
                            else:
                                raise MemoryError(f'Variable are not registred -> {new_value}.')
                        elif new_value.startswith('"') and new_value.endswith('"'):
                            new_value = new_value.strip('"')
                            new_value = Formater.FormatString(new_value)
                            memory[var] = new_value
                            return memory
                        elif new_value.startswith('*'):
                            new_value = new_value.lstrip('*')
                            try: memory[var] = int(new_value)
                            except: raise TypeError('New value are not number.')
                        else:
                            raise TypeError('Bad argument format.')
                    else:
                        raise MemoryError(f'Variable are not registred -> {var}.')
                else:
                    raise TypeError('No variable.')

    def exit():
        sys.exit()

    def void(args: str, memory: dict):
        if args.count(':') == 0 or args.count(':') >= 2:
            raise PackageError(f'Function expression must have only one single ":".')
        else:
            split = args.split(':')
            var = split[1].strip()
            if var.startswith('$__'):
                raise MemoryError(f'You cant delete reserved variables.')
            elif var.startswith('$'):
                if var in memory.keys():
                    memory.pop(var)
                    return memory
                else:
                    raise MemoryError(f'Variable are not registred -> {var}.')
            else:
                raise MemoryError(f'Variable are not registred -> {var}.')

    def zero(args: str, memory: dict):
        if args.count(':') == 0 or args.count(':') >= 2:
            raise PackageError(f'Function expression must have only one single ":".')
        else:
            split = args.split(':')
            var = split[1].strip()
            if var.startswith('$__'):
                raise MemoryError(f'You cant clear reserved variables.')
            elif var.startswith('$'):
                if var in memory.keys():
                    memory[var] = ''
                    return memory
                else:
                    raise MemoryError(f'Variable are not registred -> {var}.')
            else:
                raise MemoryError(f'Variable are not registred -> {var}.')

    def wipe():
        os.system('cls')

    def get_in(args: str, memory: dict):
        if args.count(':') == 0 or args.count(':') >= 2:
            raise PackageError(f'Function expression must have only one single ":".')
        else:
            if var.startswith('$__'):
                raise MemoryError(f'You cant use reserved variables.')
            elif var.startswith('$'):
                if var in memory.keys():
                    memory[var] = input()
                    return memory
                else:
                    raise MemoryError(f'Variable are not registred -> {var}.')
            else:
                raise MemoryError(f'Variable are not registred -> {var}.')

    def execute(args: str, memory: dict):
        if args.count(':') == 0 or args.count(':') >= 2:
            raise PackageError(f'Function expression must have only one single ":".')
        else:
            split = args.split(':')
            arg = split[1].strip()
            if arg.startswith('"') and arg.endswith('"'):
                arg = Formater.ClearWhitespaces(arg)
                arg = arg.strip('"')
                arg = Formater.FormatString(arg)
                os.system(arg)
            elif arg.startswith('$'):
                if arg in memory.keys():
                    os.system(arg)
                else:
                    raise MemoryError(f'Variable are not registred -> {arg}.')
            else:
                raise TypeError('Bad argument format.')

