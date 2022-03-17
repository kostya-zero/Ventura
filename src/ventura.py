import sys, os
import internal.arch as arch
import internal.args as args
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
        args.resolve()
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
