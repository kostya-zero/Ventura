import sys
cdef class Funcs:
    cpdef ThrowError(self, str msg, str type, str line, int num):
        print('')
        print('---<<< Ventura Interpreter Error >>>---')
        print(f'{type}: {msg}')
        print(f'Line expression: {line}')
        print(f'Line Number: {str(num)}')
        print('')
        print('If you want to find a solution for this error, check')
        print('documentation of Ventura for solution. Or go to')
        print('official GitHub page and create an issue with your')
        print('question and code snippet.')

    cpdef CheckVar(self, str var, dict memory):
        if var.startswith('$'):
            if var in memory.keys():
                return True
            else:
                return False
        else:
            raise TypeError('Bad argument format.')

    cpdef GetVar(self, str var, dict memory):
        if var.startswith('$__'):
            raise MemoryError(f'You cant use reserved variables.')
        elif var.startswith('$'):
            if var in memory.keys():
                value = memory[var]
                return value
            else:
                raise MemoryError(f'Variable are not registred -> {var}.')
        else:
            raise TypeError('Bad argument format.')


    cpdef IsVar(self, str word):
        if word.startswith('$'):
            return True
        else:
            return False

    cpdef IsText(self, str word):
        if word.startswith('"') and word.endswith('"'):
            return True
        else:
            return False