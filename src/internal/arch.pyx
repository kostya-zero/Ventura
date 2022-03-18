import platform
import sys
cpdef CheckArch():
    cdef str arch = platform.architecture()[0]
    if arch == '64bit':
        pass
    else:
        print('VENTURA: Unsupported architecture.')
        sys.exit(0)