import time, sys, platform
from os import system, path

sys.dont_write_bytecode = True

try:
    import internal.arch as arch
except:
    print('Ventura got an exceptions while starting, because arch.pyd is missing.')
    sys.exit()

import internal.args as args
from internal.parser import Parser

if platform.architecture()[1] == "WindowsPE":
    system('title Ventura 1.3')
else:
    pass

def ParseFile(arg):
    if path.exists(arg):
        if path.isfile(arg):
            if path.basename(arg).endswith('.vt'):
                with open(arg, 'r', encoding='utf8') as fp:
                    lines = fp.readlines()
                    fp.close()
                pr.Parse(lines)
            else:
                print(f'VENTURA: Ventura can execute only .vt files.')
                sys.exit()
        else:
            print(f'VENTURA: Element is not file: {arg}')
            sys.exit()
    else:
        print(f'VENTURA: Cant find element: {arg}')
        sys.exit()

arch.CheckArch()
if len(sys.argv) == 1:
    print(f'Ventura Interpreter 1.3 Phoenix Build 74\nUsage of interpreter:\nventura [path_to_file]\nor\nventura [option]\nTo show help, write "ventura -H" or "ventura --help" to the command line.')
    sys.exit()
else:
    arg = sys.argv[1]
    args.resolve(arg)
    pr = Parser(arg)
    scr_start = time.time()
    ParseFile(arg)
    scr_end = time.time()
    print(f"\n-------------------------------------\nVentura ended work. Script are ended.\nTotal working time: {str(scr_end - scr_start)}")
    sys.exit()
