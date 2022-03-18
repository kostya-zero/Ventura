import os
cpdef create(path: str):
    if os.path.exists(path):
        pass
    else:
        fp = open(path, 'w+')
        fp.close()
        del fp

cpdef write(path: str, content: str):
    if os.path.exists(path):
        fp = open(path, 'w')
        fp.write(content)
        fp.close()
        del fp
    else:
        pass
