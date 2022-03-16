import platform, os, getpass
from .formater import Formater
from .exceptions import *
from .funcs import Funcs

from libs.lib_main import Main
from libs.lib_fwriter import fwriter

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
            "main": False,
            "text": False,
            "fwriter": False
        }

        self.fwriter_file = ''

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
                            elif split[1] == 'text':
                                self.libs["text"] = True
                            elif split[1] == 'fwriter':
                                self.libs["fwriter"] = True
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
                        act = ''
                        if line.count(':') == 1:
                            act = line.split(':')[0].strip()
                        elif line.count(':') >= 2:
                            raise PackageError(f'Function expression must have only one single ":".')
                        else:
                            act = line

                        if act == '&skip': pass
                        elif act == '&out': Main.out(line, self.memory)
                        elif act == '&lnout': Main.lnout(line, self.memory)
                        elif act == '&sv': self.memory = Main.sv(line, self.memory)
                        elif act == '&exit': Main.exit()
                        elif act == '&void': self.memory = Main.void(line, self.memory)
                        elif act == '&zero': self.memory = Main.zero(line, self.memory)
                        elif act == '&wipe': Main.wipe()
                        elif act == '&get_in': self.memory = Main.get_in(line, self.memory)
                        elif act == '&execute': Main.execute(line, self.memory)
                        else: raise TypeError(f'Unknown expression -> {line}.')
                    else:
                        raise InternalError(f'Main package are not used.')
                else:
                    if line.count(':') == 0 or line.count(':') >= 2:
                        raise PackageError(f'Function expression must have only one single ":".')
                    else:
                        split = line.split(':')
                        actname = split[0].strip()
                        args = split[1].strip()

                        split_act = actname.split('->')
                        act_pkg = split_act[0].strip()
                        act_mdl = split_act[1].strip()

                        if act_pkg == 'fwriter':
                            if self.libs["fwriter"]:
                                if act_mdl == 'load': self.fwriter_file = fwriter.load(args, self.memory)
                                elif act_mdl == 'wr': fwriter.wr(args, self.fwriter_file, self.memory)
                                else: raise TypeError(f'Unknown expression -> {line}.')
                            else:
                                raise InternalError(f'fwriter package are not used.')
                        elif act_pkg == 'text':
                            if self.libs["text"]:
                                if act_mdl == 'init': pass
                                elif act_mdl == 'cls_all': pass
                                elif act_mdl == 'cls_left': pass
                                elif act_mdl == 'cls_right': pass
                                elif act_mdl == 'replace': pass
                                elif act_mdl == 'lower': pass
                                elif act_mdl == 'upper': pass
                                else: raise TypeError(f'Unknown expression -> {line}.')
                            else:
                                raise InternalError(f'text package are not used.')
                        else:
                            raise InternalError(f'Unknown package use -> {act_pkg}.')

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


