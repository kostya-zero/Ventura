import platform, os, getpass
import internal.formater as Formater
from .exceptions import InternalError, SyntaxError, PackageError, TypeError, MemoryError, ExtendError
from .funcs import Funcs
import internal.logic as Logic
Funcs = Funcs()

main = None
fstream = None
text = None
shell = None

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
            "fstream": False,
            "console": False,
            "shell": False,
            "hash": False,
            "dirsmgr": False,
            "env": False
        }

        self.prog_name = ''
        self.prog_start = False
        self.prog_ignore = False
        self.prog_inloop = False


    def Parse(self, lines: list):
        num = 0
        try:
            for line in lines:
                num += 1
                line = Formater.ClearWhitespaces(line)
                if line == '':
                    pass
                elif line.startswith('@close'):
                    if self.prog_inloop:
                        self.prog_ignore = False
                        self.prog_inloop = False
                    else:
                        raise InternalError('You havent been in a loop.')
                elif line.startswith('@'):
                    if self.prog_inloop == True:
                        raise InternalError('You havent exited the loop')
                    elif Logic.resolve(line, self.memory):
                        self.prog_inloop = True
                    else:
                        self.prog_inloop = True
                        self.prog_ignore = True
                elif self.prog_ignore:
                    pass
                elif line.startswith('>>'):
                    pass
                elif line.startswith(';'):
                    if self.prog_start == False:
                        if line.startswith(';extend'):
                            split = line.split(' ')

                            if split[1] == 'main':
                                from libs.lib_main import Main
                                main = Main
                                self.libs["main"] = True

                            elif split[1] == 'text':
                                from libs.lib_text import Text
                                text = Text
                                self.libs["text"] = True

                            elif split[1] == 'fstream':
                                from libs.lib_fstream import Fstream
                                fstream = Fstream
                                self.libs["fstream"] = True

                            elif split[1] == 'console':
                                import libs.lib_console as Console
                                self.libs["console"] = True

                            elif split[1] == 'shell':
                                from libs.lib_shell import Shell
                                shell = Shell
                                self.libs["shell"] = True

                            elif split[1] == 'hash':
                                import libs.lib_hash as Hash
                                self.libs["hash"] = True

                            elif split[1] == 'dirsmgr':
                                import libs.lib_dirsmgr as Dirsmgr
                                self.libs["dirsmgr"] = True

                            elif split[1] == 'env':
                                import libs.lib_env as Env
                                self.libs["env"] = True

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
                        elif act == '&out': main.out(line, self.memory)
                        elif act == '&lnout': main.lnout(line, self.memory)
                        elif act == '&sv': self.memory = main.sv(line, self.memory)
                        elif act == '&exit': main.exit()
                        elif act == '&void': self.memory = main.void(line, self.memory)
                        elif act == '&zero': self.memory = main.zero(line, self.memory)
                        elif act == '&wipe': main.wipe()
                        elif act == '&get_in': self.memory = main.get_in(line, self.memory)
                        elif act == '&execute': main.execute(line, self.memory)
                        else: raise TypeError(f'Unknown expression -> {line}.')
                    else:
                        raise InternalError(f'Main package are not used. Import it with ";extend" function.')
                else:
                    if line.count(':') == 0 or line.count(':') >= 2:
                        raise PackageError(f'Function expression must have only one single ":".')
                    else:
                        split = line.split(':')
                        actname = split[0].strip()
                        args = split[1].strip()

                        split_act = actname.split('.')
                        act_pkg = split_act[0].strip()
                        act_mdl = split_act[1].strip()

                        if act_pkg == 'text':
                            if self.libs["text"]:
                                if act_mdl == 'init': self.memory = text.init(args, self.memory)
                                elif act_mdl == 'cls_all': self.memory = text.cls_all(args, self.memory)
                                elif act_mdl == 'cls_left': self.memory = text.cls_left(args, self.memory)
                                elif act_mdl == 'cls_right': self.memory = text.cls_right(args, self.memory)
                                elif act_mdl == 'lower': self.memory = text.lower(args, self.memory)
                                elif act_mdl == 'upper': self.memory = text.upper(args, self.memory)
                                elif act_mdl == 'append_start': self.memory = text.append_start(args, self.memory)
                                elif act_mdl == 'append_end': self.memory = text.append_end(args, self.memory)
                                elif act_mdl == 'set': self.memory = text.set(args, self.memory)
                                else: raise TypeError(f'Unknown expression -> {line}.')
                            else:
                                raise InternalError(f'text package are not used. Import it with ";extend" function.')

                        elif act_pkg == 'fstream':
                            if self.libs["fstream"]:
                                if act_mdl == 'create': fstream.create(args, self.memory)
                                elif act_mdl == 'read': self.memory = fstream.read(args, self.memory)
                                elif act_mdl == 'read_utf8': self.memory = fstream.read_utf8(args, self.memory)
                                elif act_mdl == 'wr': fstream.wr(args, self.memory)
                                elif act_mdl == 'wra': fstream.wra(args, self.memory)
                                elif act_mdl == 'remove': fstream.remove(args, self.memory)
                                else: raise TypeError(f'Unknown expression -> {line}.')
                            else:
                                raise InternalError(f'fstream package are not used. Import it with ";extend" function.')

                        elif act_pkg == 'console':
                            if self.libs["console"]:
                                if act_mdl == 'write': Console.write(args, self.memory)
                                elif act_mdl == 'clear': Console.clear()
                                elif act_mdl == 'message': Console.message(args, self.memory)
                                elif act_mdl == 'error': Console.error(args, self.memory)
                                elif act_mdl == 'warning': Console.warning(args, self.memory)
                                else: raise TypeError(f'Unknown expression -> {line}.')
                            else:
                                raise InternalError(f'console package are not used. Import it with ";extend" function.')

                        elif act_pkg == 'shell':
                            if self.libs["shell"]:
                                if act_mdl == 'execute': shell.execute(args, self.memory)
                                elif act_mdl == 'start_cmd': shell.start_cmd()
                                elif act_mdl == 'start_ps': shell.start_ps()
                                elif act_mdl == 'start_process': shell.start_process(args, self.memory)
                            else:
                                raise InternalError(f'shell package are not used. Import it with ";extend" function.')

                        elif act_pkg == 'hash':
                            if self.libs["hash"]:
                                if act_mdl == 'md5': self.memory = Hash.md5(args, self.memory)
                                elif act_mdl == 'sha1': self.memory = Hash.sha1(args, self.memory)
                                elif act_mdl == 'sha512': self.memory = Hash.sha512(args, self.memory)
                            else:
                                raise InternalError(f'hash package are not used. Import it with ";extend" function.')

                        elif act_pkg == 'dirsmgr':
                            if self.libs["dirsmgr"]:
                                if act_mdl == 'mk': Dirsmgr.mk(args, self.memory)
                                elif act_mdl == 'rm': Dirsmgr.rm(args, self.memory)
                                elif act_mdl == 'rm_tree': Dirsmgr.rm_tree(args, self.memory)
                            else:
                                raise InternalError(f'hash package are not used. Import it with ";extend" function.')

                        elif act_pkg == 'dirsmgr':
                            if self.libs["dirsmgr"]:
                                if act_mdl == 'mk': Dirsmgr.mk(args, self.memory)
                                elif act_mdl == 'rm': Dirsmgr.rm(args, self.memory)
                                elif act_mdl == 'rm_tree': Dirsmgr.rm_tree(args, self.memory)
                            else:
                                raise InternalError(f'dirsmgr package are not used. Import it with ";extend" function.')

                        elif act_pkg == 'env':
                            if self.libs["env"]:
                                if act_mdl == 'envvar': self.memory = Env.envvar(args, self.memory)
                                elif act_mdl == 'os_ver': self.memory = Env.os_ver(args, self.memory)
                                elif act_mdl == 'os_release': self.memory = Env.os_release(args, self.memory)
                                elif act_mdl == 'os_type': self.memory = Env.os_type(args, self.memory)
                                elif act_mdl == 'os_cpu': self.memory = Env.os_cpu(args, self.memory)
                                elif act_mdl == 'os_machine': self.memory = Env.os_machine(args, self.memory)
                            else:
                                raise InternalError(f'env package are not used. Import it with ";extend" function.')

                        else:
                            raise InternalError(f'Unknown package use -> {act_pkg}. See list of available packges.')
        except InternalError as ie:
            Funcs.ThrowError(str(ie), 'InternalError', line, num)

        except ExtendError as ee:
            Funcs.ThrowError(str(ee), 'ExtendError', line, num)

        except TypeError as te:
            Funcs.ThrowError(str(te), 'TypeError', line, num)

        except MemoryError as me:
            Funcs.ThrowError(str(me), 'MemoryError', line, num)

        except PackageError as pe:
            Funcs.ThrowError(str(pe), 'PackageError', line, num)