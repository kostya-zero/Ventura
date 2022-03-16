import sys, os
from internal.exceptions import SyntaxError, PackageError
from internal.formater import Formater
from internal.funcs import Funcs
class fwriter:
    def load(args: str, memory: dict):
        if args.startswith('"') and args.endswith('"'):
            args = args.strip('"')
            if os.path.exists(args):
                if os.path.isfile(args):
                    return args
                else:
                    raise PackageError('fwriter: element are not file.')
            else:
                raise PackageError('fwriter: element are not found.')
        elif args.startswith('$__'):
            raise MemoryError(f'You cant use reserved variables.')
        elif args.startswith('$'):
            if args in memory.keys():
                path = memory[args]
                if os.path.exists(path):
                    if os.path.isfile(path):
                        return path
                    else:
                        raise PackageError('fwriter: element are not file.')
                else:
                    raise PackageError('fwriter: element are not found.')
            else:
                raise MemoryError(f'Variable are not registred -> {args}.')
        else:
            raise TypeError('Bad argument format.')

    def wr(args: str, file: str, memory: dict):
        if args.startswith('"') and args.endswith('"'):
            args = args.strip('"')
            if os.path.exists(file):
                if os.path.isfile(file):
                    fp = open(file, 'w')
                    fp.write(args)
                    fp.close()
                else:
                    raise PackageError('fwriter: element are not file.')
            else:
                raise PackageError('fwriter: element are not found.')
        elif args.startswith('$__'):
            raise MemoryError(f'You cant use reserved variables.')
        elif args.startswith('$'):
            if args in memory.keys():
                path = memory[args]
                if os.path.exists(file):
                    if os.path.isfile(file):
                        fp = open(file, 'w')
                        fp.write(args)
                        fp.close()
                    else:
                        raise PackageError('fwriter: element are not file.')
                else:
                    raise PackageError('fwriter: element are not found.')
            else:
                raise MemoryError(f'Variable are not registred -> {args}.')
        else:
            raise TypeError('Bad argument format.')



