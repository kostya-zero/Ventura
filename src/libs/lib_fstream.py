import sys, os
from internal.exceptions import SyntaxError, PackageError, MemoryError, TypeError
import internal.formater as Formater
from internal.funcs import Funcs


Funcs = Funcs()


class Fstream:
    def create(args: str, memory: dict):
        if Funcs.IsVar(args) and Funcs.CheckVar(args, memory):
            if Funcs.IsTextVar(args, memory):
                path = memory[args]["value"]
                with open(path, 'w+') as fp:
                    fp.close()
            else:
                raise TypeError('fstream: Variable must be a text.')
        elif Funcs.IsText(args):
            path = args.strip('"')
            path = Formater.FormatString(path)
            with open(path, 'w+') as fp:
                fp.close()
        else:
            raise TypeError('fstream: Bad argument format.')


    def remove(args: str, memory: dict):
        if Funcs.IsVar(args) and Funcs.CheckVar(args, memory):
            if Funcs.IsTextVar(args, memory):
                path = memory[args]["value"]
                os.remove(path)
            else:
                raise TypeError('fstream: Variable must be a text.')
        elif Funcs.IsText(args):
            path = args.strip('"')
            path = Formater.FormatString(path)
            os.remove(path)
        else:
            raise TypeError('fstream: Bad argument format.')


    def read(args: str, memory: dict):
        if args.count(',') != 1:
            raise TypeError(f'fstream: Function require 2 arguments.')
        else:
            spl = args.split(',')
            var = spl[0].strip()
            path = spl[1].strip()

            if Funcs.IsVar(var) and Funcs.CheckVar(var, memory) and not var.startswith('$__'):
                if Funcs.IsTextVar(var, memory):
                    pass
                else:
                    raise TypeError(f'fstream: Variable must be a text.')
            else:
                raise TypeError(f'fstream: Bad argument format. Argument 1.')

            if Funcs.IsVar(path) and Funcs.CheckVar(path, memory):
                if Funcs.IsTextVar(path, memory):
                    path = memory[path]["value"]
                else:
                    raise TypeError('fstream: Variable must be a text.')
            elif Funcs.IsText(path):
                path = path.strip('"')
                path = Formater.FormatString(path)
            else:
                raise TypeError('fstream: Bad argument format.')

            with open(path, 'r') as fp:
                memory[path]["value"] = fp.read()

            return memory


    def read_utf8(args: str, memory: dict):
        if args.count(',') != 1:
            raise TypeError(f'fstream: Function require 2 arguments.')
        else:
            spl = args.split(',')
            var = spl[0].strip()
            path = spl[1].strip()

            if Funcs.IsVar(var) and Funcs.CheckVar(var, memory) and not var.startswith('$__'):
                if Funcs.IsTextVar(var, memory):
                    pass
                else:
                    raise TypeError(f'fstream: Variable must be a text.')
            else:
                raise TypeError(f'fstream: Bad argument format. Argument 1.')

            if Funcs.IsVar(path) and Funcs.CheckVar(path, memory):
                if Funcs.IsTextVar(path, memory):
                    path = memory[path]["value"]
                else:
                    raise TypeError('fstream: Variable must be a text.')
            elif Funcs.IsText(path):
                path = path.strip('"')
                path = Formater.FormatString(path)
            else:
                raise TypeError('fstream: Bad argument format.')

            with open(path, 'r', encoding='utf8') as fp:
                memory[path]["value"] = fp.read()

            return memory


    def wr(args: str, memory: dict):
        if args.count(',') != 1:
            raise TypeError(f'fstream: Function require 2 arguments.')
        else:
            spl = args.split(',')
            path = spl[0].strip()
            cont = spl[1].strip()

            if Funcs.IsVar(path) and Funcs.CheckVar(path, memory) and not path.startswith('$__'):
                if Funcs.IsTextVar(path, memory):
                    pass
                else:
                    raise TypeError(f'fstream: Variable must be a text.')
            elif Funcs.IsText(path):
                path = path.strip('"')
                path = Formater.FormatString(path)
            else:
                raise TypeError(f'fstream: Bad argument format. Argument 1.')

            if Funcs.IsVar(cont) and Funcs.CheckVar(cont, memory):
                if Funcs.IsTextVar(cont, memory):
                    cont = memory[cont]["value"]
                else:
                    raise TypeError('fstream: Variable must be a text.')
            elif Funcs.IsText(cont):
                cont = cont.strip('"')
                cont = Formater.FormatString(cont)
            else:
                raise TypeError('fstream: Bad argument format.')

            with open(path, 'w', encoding='utf8') as fp:
                fp.write(cont)


    def wra(args: str, memory: dict):
        if args.count(',') != 1:
            raise TypeError(f'fstream: Function require 2 arguments.')
        else:
            spl = args.split(',')
            path = spl[0].strip()
            cont = spl[1].strip()

            if Funcs.IsVar(path) and Funcs.CheckVar(path, memory) and not path.startswith('$__'):
                if Funcs.IsTextVar(path, memory):
                    pass
                else:
                    raise TypeError(f'fstream: Variable must be a text.')
            elif Funcs.IsText(path):
                path = path.strip('"')
                path = Formater.FormatString(path)
            else:
                raise TypeError(f'fstream: Bad argument format. Argument 1.')

            if Funcs.IsVar(cont) and Funcs.CheckVar(cont, memory):
                if Funcs.IsTextVar(cont, memory):
                    cont = memory[cont]["value"]
                else:
                    raise TypeError('fstream: Variable must be a text.')
            elif Funcs.IsText(cont):
                cont = cont.strip('"')
                cont = Formater.FormatString(cont)
            else:
                raise TypeError('fstream: Bad argument format.')

            with open(path, 'a', encoding='utf8') as fp:
                fp.write(cont)


    def exist(args: str, memory: dict):
        if args.count(',') != 1:
            raise TypeError(f'fstream: Function require 2 arguments.')
        else:
            spl = args.split(',')
            var = spl[0].strip()
            path = spl[1].strip()

            if Funcs.IsVar(var) and Funcs.CheckVar(var, memory) and not var.startswith('$__'):
                if Funcs.IsTextVar(var, memory):
                    pass
                else:
                    raise TypeError(f'fstream: Variable must be a text.')
            else:
                raise TypeError(f'fstream: Bad argument format. Argument 1.')

            if Funcs.IsVar(path) and Funcs.CheckVar(path, memory):
                if Funcs.IsTextVar(path, memory):
                    path = memory[path]["value"]
                else:
                    raise TypeError('fstream: Variable must be a text.')
            elif Funcs.IsText(path):
                path = path.strip('"')
                path = Formater.FormatString(path)
            else:
                raise TypeError('fstream: Bad argument format.')

            if os.path.exists(path):
                memory[var]["value"] = "1"
                return memory
            else:
                memory[var]["value"] = "0"
                return memory
