import sys, os
from internal.exceptions import SyntaxError, PackageError
from internal.formater import Formater
from internal.funcs import Funcs
class text:
    def init(args: str, memory: dict):
        if Funcs.IsVar(args):
            if Funcs.CheckVar(args, memory):
                memory[args] = ''
                return memory
            else:
                raise MemoryError(f'Variable are not registred -> {args}.')
        else:
            raise TypeError('Bad argument format.')

    def cls_all(args: str, memory: dict):
        if Funcs.IsVar(args):
            if Funcs.CheckVar(args, memory):
                memory[args] = str(memory[args]).strip()
                return memory
            else:
                raise MemoryError(f'Variable are not registred -> {args}.')
        else:
            raise TypeError('Bad argument format.')

    def cls_left(args: str, memory: dict):
        if Funcs.IsVar(args):
            if Funcs.CheckVar(args, memory):
                memory[args] = str(memory[args]).lstrip()
                return memory
            else:
                raise MemoryError(f'Variable are not registred -> {args}.')
        else:
            raise TypeError('Bad argument format.')

    def cls_right(args: str, memory: dict):
        if Funcs.IsVar(args):
            if Funcs.CheckVar(args, memory):
                memory[args] = str(memory[args]).rstrip()
                return memory
            else:
                raise MemoryError(f'Variable are not registred -> {args}.')
        else:
            raise TypeError('Bad argument format.')

    def replace(args: str, memory: dict):
        if args.count(',') == 2:
            split = args.split(',')


    def lower(args: str, memory: dict):
        if Funcs.IsVar(args):
            if Funcs.CheckVar(args, memory):
                memory[args] = str(memory[args]).lower()
                return memory
            else:
                raise MemoryError(f'Variable are not registred -> {args}.')
        else:
            raise TypeError('Bad argument format.')

    def upper(args: str, memory: dict):
        if Funcs.IsVar(args):
            if Funcs.CheckVar(args, memory):
                memory[args] = str(memory[args]).upper()
                return memory
            else:
                raise MemoryError(f'Variable are not registred -> {args}.')
        else:
            raise TypeError('Bad argument format.')
