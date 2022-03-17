import os, sys
import internal.arch as arch
sys.dont_write_bytecode = True

from internal.parser import Parser

app = {
    "version": "0.9"
}

vt_script = """;extend main
;prog_name "script"
;entry
    &out: "Hello World!"
"""
arch.CheckArch()
if len(sys.argv) == 1:
    print('Ventura Interpreter')
    sys.exit()
else:
    arg = sys.argv[1]
    if arg.startswith('-'):
        if arg == '--help' or arg == '-h':
            print('Ventura usage:')
            print('ventura [path_to_file]')
            print('')
            print('Commands:')
            print('--help, -h: Shows help.')
            print('--version, -v: Version of Ventura.')
            print('--generate-vt: Generates .vt file at location.')
        elif arg == '--version' or arg == '-v':
            print(app["version"])
            sys.exit()
        elif arg == '--generate-vt':
            path = input('Enter absolute path for new file: ')
            if os.path.isabs(path):
                if os.path.exists(path):
                    print('VENTURA: Element with this path already exists.')
                    sys.exit()
                elif not path.endswith('.vt'):
                    print('VENTURA: File must have .vt extension.')
                    sys.exit()
                else:
                    fp = open(path, 'w+')
                    fp.write(vt_script)
                    fp.close()
                    print(f'Success! Script file was created by this path: {path}')
                    sys.exit()
            else:
                print('VENTURA: Path is not absolute.')
                sys.exit()
        else:
            print(f'VENTURA: Unknown argument: {arg}')
            sys.exit()
    else:
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
