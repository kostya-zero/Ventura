import sys
import os
import platform
cpdef resolve():
    cdef str arg = sys.argv[1]
    if arg == '-V' or arg == '--version':
        print('1.1')
        sys.exit(0)
    elif arg == '-gvt' or arg == '--generate-vt':
        path = input('Enter absolute path for new file: ')
        if os.path.isabs(path):
            if os.path.exists(path):
                print('VENTURA: Element with this path already exists.')
                sys.exit()
            elif not path.endswith('.vt'):
                print('VENTURA: File must have .vt extension.')
                sys.exit()
            else:
                fp = open(path, 'w')
                fp.write(""";extend main
;prog_name "script"
;entry
    &out: "Hello World!""")
                fp.close()
                print(f'Success! Script file was created by this path: {path}')
                sys.exit()
        else:
            print('VENTURA: Path is not absolute.')
            sys.exit()
    elif arg == '-A' or arg == '--authors':
        print('Authors of Ventura:')
        print('Konstantin ".ZERO" Zhigailo')
        sys.exit()
    elif arg == '-S' or arg == '--system':
        print(f'OS Type: {platform.system()} {platform.version()}')
        print(f'Architecture: {platform.architecture()[0]}')
        print(f'Host Name: {platform.node()}')
        print(f'CPU Architecture: {os.environ["PROCESSOR_ARCHITECTURE"]}')
        print(f'CPU Identifier: {os.environ["PROCESSOR_IDENTIFIER"]}')
        sys.exit()
    elif arg == '-H' or arg == '--help':
        print('Ventura usage:')
        print('ventura [path_to_file]')
        print('')
        print('Commands:')
        print('-H, --help: Shows help.')
        print('-V, --version: Version of Ventura.')
        print('-A, --authors: Shows authors of Ventura.')
        print('-S, --system: Shows info about current machine.')
        print('-gvt: Generates .vt file at location.')
        sys.exit()