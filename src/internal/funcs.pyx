import sys


cdef class Funcs:
    cpdef ThrowError(self, str msg, str type, str line, int num):
        print('')
        print('---<<< Ventura Interpreter Error >>>---')
        print(f'{type}: {msg}')
        print(f'Line expression: {line}')
        print(f'Line Number: {str(num)}')

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
                obj = memory[var]
                return obj
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

    cpdef IsNumber(self, str word):
        if word.startswith('*'):
            return True
        else:
            return False

    cpdef IsTextVar(self, str word, dict memory):
        if self.CheckVar(word, memory):
            if memory[word]["type"] == 'text':
                return True
            else:
                return False
        else:
            raise MemoryError(f'Variable are not registred -> {word}.')
