import platform
cpdef CheckArch():
    cdef str arch = platform.architecture()[0]
    if arch == '64bit':
        pass
    else:
        exit(0)