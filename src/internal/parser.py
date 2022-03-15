import platform, os, getpass
from .formater import Formater
from .exceptions import *
from .funcs import Funcs

from libs.main import Main

class Parser(object):
    def __init__(self, filepath: str):
        self.memory = {
            "$__filename": os.path.basename(filepath),
            "$__filepath": filepath,
            "$__filedir": os.path.dirname(filepath),
            "$__filenamenoext": os.path.basename(os.path.splitext(filepath)[0]),

            "$__username": getpass.getuser(),
            "$__hostname": platform.node(),

            "$__cpuarch": os.environ["PROCESSOR_ARCHITECTURE"],
            "$__cpuident": os.environ["PROCESSOR_IDENTIFIER"],
            "$__cpulevel": os.environ["PROCESSOR_LEVEL"],
            "$__cpurevision": os.environ["PROCESSOR_REVISION"]
        }
        self.libs = {
            "main": False
        }

        self.illegal_symb = ['@', '#', '%', '^', '&', '*', '!']

        self.prog_name = ''
        self.prog_start = False


    def Parse(self, lines: list):
        num = 0
        try:
            for line in lines:
                num += 1
                line = Formater.ClearWhitespaces(line)
                if line == '':
                    pass
                elif line.startswith('>>'):
                    pass
                elif line.startswith(';'):
                    if self.prog_start == False:
                        if line.startswith(';extend'):
                            split = line.split(' ')
                            if split[1] == 'main':
                                self.libs["main"] = True
                            else:
                                raise ExtendError(f'Unknown library -> "{split[1]}".')
                        elif line.startswith(';prog_name'):
                            split = line.split(' ')
                            if split[1].startswith('"') and split[1].endswith('"'):
                                self.prog_name = split[1].strip('"')
                            else:
                                raise InternalError(f'Program name must be in double quotes.')
                        elif line.startswith(';entry'):
                            self.prog_start = True
                        elif line.startswith(';new'):
                            split = line.split(' ')
                            if split[1].startswith('$__'):
                                raise TypeError(f'Variable name cant have name like reserved variable.')
                            elif split[1].startswith('$'):
                                self.memory[split[1]] = ''
                            else:
                                raise TypeError(f'Variable name must starts with "$".')
                        else:
                            raise TypeError(f'Unknown expression for internal function -> {line}.')
                    else:
                        raise InternalError('Program already started.')
                elif line.startswith('&'):
                    if self.libs["main"] == True:
                        if line.startswith('&skip'): pass
                        elif line.startswith('&out'): Main.out(line, self.memory)
                        elif line.startswith('&lnout'): Main.lnout(line, self.memory)
                        elif line.startswith('&sv'): self.memory = Main.sv(line, self.memory)
                        elif line.startswith('&exit'): Main.exit()
                        elif line.startswith('&void'): self.memory = Main.void(line, self.memory)
                        elif line.startswith('&zero'): self.memory = Main.zero(line, self.memory)
                        elif line.startswith('&wipe'): Main.wipe()
                        elif line.startswith('&get_in'): self.memory = Main.get_in(line, self.memory)
                        elif line.startswith('&execute'): Main.execute(line, self.memory)
                        else: raise TypeError(f'Unknown expression -> {line}.')
                    else:
                        raise InternalError(f'Main package are not used.')
        except InternalError as ie:
            Funcs.ThrowError(ie, 'InternalError', line, num)

        except ExtendError as ee:
            Funcs.ThrowError(ee, 'ExtendError', line, num)

        except TypeError as te:
            Funcs.ThrowError(te, 'TypeError', line, num)

        except MemoryError as me:
            Funcs.ThrowError(me, 'MemoryError', line, num)

        except PackageError as pe:
            Funcs.ThrowError(pe, 'PackageError', line, num)



