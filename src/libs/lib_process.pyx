import sys, os
from internal.exceptions import SyntaxError, PackageError, MemoryError, TypeError
import internal.formater as Formater
from internal.funcs import Funcs
Funcs = Funcs()
cpdef start(args: str, memory: dict)