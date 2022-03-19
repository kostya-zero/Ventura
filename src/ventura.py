try:
    import sys, os, time
    import internal.arch as arch
    import internal.args as args
    sys.dont_write_bytecode = True
    from internal.parser import Parser
except Exception as ex:
    print('Ventura got an exceptions while starting.')
    print('Exception: ' + ex)

arch.CheckArch()
if len(sys.argv) == 1:
    print('Ventura Interpreter 1.1 Preview Build 42')
    print('')
    print('Usage of interpreter:')
    print('ventura [path_to_file]')
    print('or')
    print('ventura [option]')
    print('To show help, write "ventura -H" or "ventura --help" to the command line.')
    sys.exit()
else:
    arg = sys.argv[1]
    args.resolve(arg)
    if os.path.exists(arg):
        if os.path.isfile(arg):
            if os.path.basename(arg).endswith('.vt'):
                pr = Parser(arg)
                fp = open(arg, 'r')
                lines = fp.readlines()
                fp.close()
                scr_start = time.time()
                pr.Parse(lines)
                scr_end = time.time()
                print('')
                print('-------------------------------------')
                print('Ventura ended work. Script are ended.')
                print('Total working time: ' + str(scr_end - scr_start) + '.')
            else:
                print(f'VENTURA: Ventura can execute only .vt files.')
        else:
            print(f'VENTURA: Element is not file: {arg}')
    else:
        print(f'VENTURA: Cant find element: {arg}')
