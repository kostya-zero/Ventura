import time, sys
from os import system, path

try:
    import internal.arch as arch
except:
    print('Ventura got an exceptions while starting, because arch.pyd is missing.')
    sys.exit()

try:
    import internal.args as args
except:
    print('Ventura got an exceptions while starting, because args.pyd is missing.')
    sys.exit()

sys.dont_write_bytecode = True

try:
    from internal.parser import Parser
except:
    print('Ventura got an exceptions while starting, because parser are missing.')
    sys.exit()

def ParseFile(arg):
    if path.exists(arg):
        if path.isfile(arg):
            if path.basename(arg).endswith('.vt'):
                fp = open(arg, 'r')
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

info = [
    'Ventura Interpreter 1.1 Sunraise Build 50\n',
    'Usage of interpreter:',
    'ventura [path_to_file]',
    'or',
    'ventura [option]',
    'To show help, write "ventura -H" or "ventura --help" to the command line.'
]      
        
arch.CheckArch()
if len(sys.argv) == 1:
    for info in info:
        print(info)
    sys.exit()
else:
    arg = sys.argv[1]
    args.resolve(arg)
    pr = Parser(arg)
    scr_start = time.time()
    ParseFile(arg)
    scr_end = time.time()
    ended_text = [
        '\n-------------------------------------',
        'Ventura ended work. Script are ended.',
        'Total working time: ' + str(scr_end - scr_start) + '.'
    ]
    for ended_text in ended_text:
        print(ended_text)
    sys.exit()
