import sys
class Funcs:
    def ThrowError(msg: str, type: str, line: str, num: int):
        print('')
        print('---<<< Ventura Interpreter Error >>>---')
        print(f'{type}: {msg}')
        print(f'Line: {line}')
        print(f'Number: {str(num)}')
        sys.exit()

    def CheckVar(var: str, memory: dict):
        if var.startswith('$__'):
            raise MemoryError(f'You cant clear reserved variables.')
        elif var.startswith('$'):
            if var in memory.keys():
                return True
            else:
                return False
        else:
            raise TypeError('Bad argument format.')

    def GetVar(var: str, memory: dict):
        Funcs.CheckVar(var, memory)
        value = memory[var]
        return value

    def IsVar(word: str):
        if word.startswith('$'):
            return True
        else:
            return False

    def IsText(word: str):
        if word.startswith('"') and word.endswith('"'):
            return True
        else:
            return False