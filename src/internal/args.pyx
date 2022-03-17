import sys
import os
cpdef resolve():
    cdef str arg = sys.argv[1]
    if arg == '-v':
        print('0.9')
        exit(0)
    elif arg == '-gvt':
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
                fp.write(""";extend main
;prog_name "script"
;entry
    &out: "Hello World!"
""")
                fp.close()
                print(f'Success! Script file was created by this path: {path}')
                sys.exit()
        else:
            print('VENTURA: Path is not absolute.')
            sys.exit()
    elif arg == '-h':
        print('Ventura usage:')
        print('ventura [path_to_file]')
        print('')
        print('Commands:')
        print('-h: Shows help.')
        print('-v: Version of Ventura.')
        print('-gvt: Generates .vt file at location.')