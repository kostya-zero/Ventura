from os import path, mkdir, rmdir
from shutil import rmtree
from internal.exceptions import SyntaxError, PackageError, MemoryError, TypeError
import internal.formater as Formater
from internal.funcs import Funcs


Funcs = Funcs()


class Convert:
    cpdef to_text(args: str, memory: dict):
        if args.count(',') != 1:
            raise TypeError(f'')