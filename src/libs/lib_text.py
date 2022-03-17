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
            var = split[0].strip()
            new_v = split[2].strip()
            old_v = split[1].strip()
            if var.startswith('$') and Funcs.CheckVar(var):
                pass # TODO: Complete this section

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

    def append_start(args: str, memory: dict):
        if args.count(',') == 1:
            split = args.split(',')
            if Funcs.IsVar(split[0]):
                if Funcs.CheckVar(split[0], memory):
                    memory[split[0]] = Formater.Format(split[1]) + str(memory[split[0]])
                    return memory
                else:
                    raise MemoryError(f'Variable are not registred -> {args}.')
            else:
                raise TypeError('Bad argument format.')
        else:
            raise TypeError('Function require 2 arguments.')

    def append_end(args: str, memory: dict):
        if args.count(',') == 1:
            split = args.split(',')
            if Funcs.IsVar(split[0]):
                if Funcs.CheckVar(split[0], memory):
                    memory[split[0]] = str(memory[split[0]]) + Formater.Format(split[1])
                    return memory
                else:
                    raise MemoryError(f'Variable are not registred -> {args}.')
            else:
                raise TypeError('Bad argument format.')
        else:
            raise TypeError('Function require 2 arguments.')

    def set(args: str, memory: dict):
        if args.count(',') == 1:
            split = args.split(',')
            if Funcs.IsVar(split[0]):
                if Funcs.CheckVar(split[0], memory):
                    memory[split[0]] = Formater.Format(split[1])
                    return memory
                else:
                    raise MemoryError(f'Variable are not registred -> {args}.')
            else:
                raise TypeError('Bad argument format.')
        else:
            raise TypeError('Function require 2 arguments.')
