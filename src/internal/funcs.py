import sys
class Funcs:
    def ThrowError(msg: str, type: str, line: str, num: int):
        print('')
        print('---<<< Ventura Interpreter Error >>>---')
        print(f'{type}: {msg}')
        print(f'Line: {line}')
        print(f'Number: {str(num)}')
        sys.exit()
