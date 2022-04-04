import sys, os, platform
from internal.exceptions import SyntaxError, PackageError, MemoryError, TypeError
import internal.formater as Formater
from internal.funcs import Funcs


Funcs = Funcs()


cpdef envvar(args: str, memory: dict):
    if args.count(',') != 1:
        raise PackageError('Function require 2 arguments.')
    else:
        spl = args.split(',')
        var = spl[0].strip()
        env = spl[1].strip()

        if Funcs.IsVar(var) and Funcs.CheckVar(var, memory) and not var.startswith('$__'):
            if Funcs.IsTextVar(var, memory):
                var = memory[var]["value"]
            else:
                raise TypeError('Variable are not text.')
        else:
            raise TypeError('Bad argument format. Argument number: 1')

        if Funcs.IsText(env):
            env = env.strip('"')
            env = Formater.FormatString(env)
        elif Funcs.IsVar(env) and Funcs.CheckVar(env, memory) and not env.startswith('$__'):
            if Funcs.IsTextVar(env, memory):
                env = memory[env]["value"]
            else:
                raise TypeError('Variable are not text.')
        else:
            raise TypeError('Bad argument format. Argument number: 2')

        try:
            envvar = os.environ
        except:
            raise TypeError(f'Cant find environment variable "{env}".')

        memory[var]["value"] = envvar
        return memory


cpdef os_ver(args: str, memory: dict):
    if Funcs.IsVar(args) and Funcs.CheckVar(args, memory) and not args.startswith('$__'):
        if Funcs.IsTextVar(args, memory):
            memory[args]["value"] = platform.version()
            return memory
        else:
            raise TypeError('Variable type doesnt match new value type.')
    else:
        raise MemoryError(f'Variable "{args}" are not located in memory or its reserved variable.')


cpdef os_release(args: str, memory: dict):
    if Funcs.IsVar(args) and Funcs.CheckVar(args, memory) and not args.startswith('$__'):
        if Funcs.IsTextVar(args, memory):
            memory[args]["value"] = platform.release()
            return memory
        else:
            raise TypeError('Variable type doesnt match new value type.')
    else:
        raise MemoryError(f'Variable "{args}" are not located in memory or its reserved variable.')


cpdef os_type(args: str, memory: dict):
    if Funcs.IsVar(args) and Funcs.CheckVar(args, memory) and not args.startswith('$__'):
        if Funcs.IsTextVar(args, memory):
            memory[args]["value"] = platform.system()
            return memory
        else:
            raise TypeError('Variable type doesnt match new value type.')
    else:
        raise MemoryError(f'Variable "{args}" are not located in memory or its reserved variable.')


cpdef os_cpu(args: str, memory: dict):
    if Funcs.IsVar(args) and Funcs.CheckVar(args, memory) and not args.startswith('$__'):
        if Funcs.IsTextVar(args, memory):
            memory[args]["value"] = platform.processor()
            return memory
        else:
            raise TypeError('Variable type doesnt match new value type.')
    else:
        raise MemoryError(f'Variable "{args}" are not located in memory or its reserved variable.')


cpdef os_machine(args: str, memory: dict):
    if Funcs.IsVar(args) and Funcs.CheckVar(args, memory) and not args.startswith('$__'):
        if Funcs.IsTextVar(args, memory):
            memory[args]["value"] = platform.machine()
            return memory
        else:
            raise TypeError('Variable type doesnt match new value type.')
    else:
        raise MemoryError(f'Variable "{args}" are not located in memory or its reserved variable.')
