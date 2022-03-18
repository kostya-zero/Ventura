import sys, os
import internal.arch as arch
import internal.args as args
sys.dont_write_bytecode = True
from internal.parser import Parser

arch.CheckArch()
if len(sys.argv) == 1:
    print('Ventura Interpreter 1.1 Build 29')
    sys.exit()
else:
    args.resolve()
    arg = sys.argv[1]
    if os.path.exists(arg):
        if os.path.isfile(arg):
            if os.path.basename(arg).endswith('.vt'):
                pr = Parser(arg)
                fp = open(arg, 'r')
                lines = fp.readlines()
                fp.close()
                pr.Parse(lines)
            else:
                print(f'VENTURA: Ventura can execute only .vt files.')
        else:
            print(f'VENTURA: Element is not file: {arg}')
    else:
        print(f'VENTURA: Cant find element: {arg}')
