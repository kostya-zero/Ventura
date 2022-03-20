import sys, os
from internal.exceptions import SyntaxError, PackageError, MemoryError, TypeError
import internal.formater as Formater
from internal.funcs import Funcs
Funcs = Funcs()
class fstream:
    def create(args: str, memory: dict):
        args = args.strip()
        if Funcs.IsVar(args) and Funcs.CheckVar(args, memory):
            file = open(memory[args], 'w+')
            file.close()
        elif Funcs.IsText(args):
            args = args.strip('"')
            args = Formater.FormatString(args)
            file = open(args, 'w+')
            file.close()
        else:
            raise TypeError('Bad arguments format. \n                Argument can be variable or text value.')

    def remove(args: str, memory: dict):
        args = args.strip()
        if Funcs.IsVar(args) and Funcs.CheckVar(args, memory):
            os.remove(memory[args])
        elif Funcs.IsText(args):
            args = args.strip('"')
            args = Formater.FormatString(args)
            os.remove(args)
        else:
            raise TypeError('Bad arguments format. \n                Argument can be variable or text value.')

    def read(args: str, memory: dict):
        args = args.strip()
        if args.count(',') == 1:
            splt = args.split(',')
            path = splt[0].strip()
            var = splt[1].strip()

            if Funcs.IsVar(path) and Funcs.CheckVar(path, memory):
                path = memory[path]
            else:
                path = path.strip('"')
                path = Formater.FormatString(path)

            if Funcs.IsVar(var) and Funcs.CheckVar(var, memory):
                pass
            else:
                raise TypeError(f'Variable not registred or bad format -> {var}.')

            fp = open(path, 'r')
            cont = fp.read()
            fp.close()
            memory[var] = cont
            return memory
        else:
            raise TypeError('Function require 2 arguments.')

    def read_utf8(args: str, memory: dict):
        args = args.strip()
        if args.count(',') == 1:
            splt = args.split(',')
            path = splt[0].strip()
            var = splt[1].strip()

            if Funcs.IsVar(path) and Funcs.CheckVar(path, memory):
                path = memory[path]
            else:
                path = path.strip('"')
                path = Formater.FormatString(path)

            if Funcs.IsVar(var) and Funcs.CheckVar(var, memory):
                pass
            else:
                raise TypeError(f'Variable not registred or bad format -> {var}.')

            fp = open(path, 'r', encoding='UTF-8')
            cont = fp.read()
            fp.close()
            memory[var] = cont
            return memory
        else:
            raise TypeError('Function require 2 arguments')

    def wr(args: str, memory: dict):
        args = args.strip()
        if args.count(',') == 1:
            splt = args.split(',')
            path = splt[0].strip()
            cont = splt[1].strip()
            if Funcs.IsVar(path) and Funcs.CheckVar(path, memory):
                path = memory[path]
            else:
                path = path.strip('"')
                path = Formater.FormatString(path)

            if Funcs.IsVar(cont) and Funcs.CheckVar(cont, memory):
                cont = memory[cont]
            else:
                cont = cont.strip('"')
                cont = Formater.FormatString(cont)

            fp = open(path, 'w')
            fp.write(cont)
            fp.close()
        else:
            raise TypeError('Function require 2 arguments')

    def wra(args: str, memory: dict):
        args = args.strip()
        if args.count(',') == 1:
            splt = args.split(',')
            path = splt[0].strip()
            cont = splt[1].strip()
            if Funcs.IsVar(path) and Funcs.CheckVar(path, memory):
                path = memory[path]
            else:
                path = path.strip('"')
                path = Formater.FormatString(path)

            if Funcs.IsVar(cont) and Funcs.CheckVar(cont, memory):
                cont = memory[cont]
            else:
                cont = cont.strip('"')
                cont = Formater.FormatString(cont)

            fp = open(path, 'a')
            fp.write(cont)
            fp.close()
        else:
            raise TypeError('Function require 2 arguments')
