import platform, os, getpass
import internal.formater as Formater
from .exceptions import InternalError, SyntaxError, PackageError, TypeError, MemoryError, ExtendError
from .funcs import Funcs
import internal.logic as Logic
Funcs = Funcs()

class Parser(object):
    def __init__(self, filepath: str):
        self.memory = {
            "$__filename": os.path.basename(filepath),
            "$__filepath": filepath,
            "$__filedir": os.path.dirname(filepath),
            "$__filenamenoext": os.path.basename(os.path.splitext(filepath)[0]),

            "$__username": getpass.getuser(),
            "$__hostname": platform.node(),

            "$__cpuarch": platform.architecture()[1]
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
        self.funcs = {}

        self.prog_name = ''
        self.prog_start = False
        self.prog_ignore = False
        self.prog_inloop = False

        self.main = None
        self.fstream = None
        self.text = None
        self.shell = None


    def Parse(self, lines: list):
        num = 0
        for line in lines:
            try:
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
                elif line == '}':
                    if self.prog_ignore:
                        self.prog_ignore = False
                    else:
                        raise InternalError('No function initialized!')
                elif line.startswith('@'):
                    if self.prog_inloop == True:
                        raise InternalError('You havent exited the loop')
                    elif line.startswith('@parse_line'):
                        if line.count(':') == 1:
                            split = line.split(':')
                            num = None
                            try: num = int(split[1])
                            except: raise InternalError('Value must be without any chars, only numbers.')
                            if num > len(lines):
                                raise InternalError('Line to parse are not in range.')
                            else:
                                tp = []
                                tp.append(lines[num - 1])
                                self.Parse(tp)
                        else:
                            raise TypeError(f'Function expression must have only one single ":".')

                    elif line.startswith('@func'):
                        split = line.split()
                        func_name = split[1].strip()
                        if split[2].strip() == '{':
                            func_lines = []
                            for i in range(num, len(lines)):
                                cur_line = lines[i - 1].strip()
                                if line == cur_line:
                                    pass
                                elif cur_line == '}':
                                    break
                                else:
                                    func_lines.append(cur_line)
                            self.funcs[func_name] = func_lines
                            self.prog_ignore = True
                        else:
                            raise InternalError("Function havent entry point.")

                    elif line.startswith('@call'):
                        split = line.split(' ')
                        if split[1].strip() in self.funcs.keys():
                            self.Parse(self.funcs[split[1].strip()])
                        else:
                            raise InternalError("Function not registred.")
                    
                    elif Logic.resolve(line, self.memory):
                        self.prog_inloop = True

                    else:
                        self.prog_inloop = True
                        self.prog_ignore = True
                elif self.prog_ignore:
                    pass
                elif line.startswith('>>'):
                    pass
                elif line.startswith('#'):
                    if self.prog_start == False:
                        if line.startswith('#extend'):
                            split = line.split(' ')

                            if split[1] == '<vio>':
                                from libs.lib_main import Main
                                self.main = Main
                                self.libs["main"] = True

                            elif split[1] == '<text>':
                                from libs.lib_text import Text
                                self.text = Text
                                self.libs["text"] = True

                            elif split[1] == '<fstream>':
                                from libs.lib_fstream import Fstream
                                self.fstream = Fstream
                                self.libs["fstream"] = True

                            elif split[1] == '<console>':
                                import libs.lib_console as Console
                                self.libs["console"] = True

                            elif split[1] == '<shell>':
                                from libs.lib_shell import Shell
                                self.shell = Shell
                                self.libs["shell"] = True

                            elif split[1] == '<hash>':
                                import libs.lib_hash as Hash
                                self.libs["hash"] = True

                            elif split[1] == '<dirsmgr>':
                                import libs.lib_dirsmgr as Dirsmgr
                                self.libs["dirsmgr"] = True

                            elif split[1] == '<env>':
                                import libs.lib_env as Env
                                self.libs["env"] = True

                            else:
                                raise ExtendError(f'Unknown library -> "{split[1]}".')
                        elif line.startswith('#prog_name'):
                            split = line.split(' ')
                            if split[1].startswith('"') and split[1].endswith('"'):
                                self.prog_name = split[1].strip('"')
                            else:
                                raise InternalError(f'Program name must be in double quotes.')
                        elif line.startswith('#start'):
                            if self.prog_start:
                                raise RuntimeError("Program already started.")
                            else:
                                self.prog_start = True
                        elif line.startswith('#new'):
                            split = line.split(' ')
                            if split[1].startswith('$__'):
                                raise TypeError(f'Variable name cant have name like reserved variable.')
                            elif split[1].startswith('$'):
                                self.memory[split[1]] = ''
                            else:
                                raise TypeError(f'Variable name must starts with "$".')
                        else:
                            raise TypeError(f'Unknown expression for internal function -> {line}.')
                    else: raise InternalError('Program already started.')
                elif line.startswith('&'):
                    if self.libs["main"] == True:
                        act = ''
                        if line.count(':') == 1:
                            act = line.split(':')[0].strip()
                        elif line.count(':') >= 2:
                            raise PackageError(f'Function expression must have only one single ":".')
                        else: act = line

                        if act == '&skip': pass
                        elif act == '&out': self.main.out(line, self.memory)
                        elif act == '&lnout': self.main.lnout(line, self.memory)
                        elif act == '&sv': self.memory = self.main.sv(line, self.memory)
                        elif act == '&exit': self.main.exit()
                        elif act == '&void': self.memory = self.main.void(line, self.memory)
                        elif act == '&zero': self.memory = self.main.zero(line, self.memory)
                        elif act == '&wipe': self.main.wipe()
                        elif act == '&get_in': self.memory = self.main.get_in(line, self.memory)
                        elif act == '&execute': self.main.execute(line, self.memory)
                        else: raise TypeError(f'Unknown expression -> {line}.')
                        
                    else: raise InternalError(f'Main package are not used. Import it with ";extend" function.')
                else: 
                    if line.count(':') == 0 or line.count(':') >= 2:
                        raise PackageError(f'Function expression must have only one single ":".')
                    else:
                        split = line.split(':')
                        actname = split[0].strip()
                        args = split[1].strip()

                        if args .strip().startswith('(') and args .strip().endswith(')'):
                            pass
                        else:
                            raise TypeError("Arguments must be in brackets. New in 1.3 version.")

                        args = args.lstrip('(')
                        args = args.rstrip(')')
                        args = args.strip()

                        split_act = actname.split('.')
                        act_pkg = split_act[0].strip()
                        act_mdl = split_act[1].strip()

                        if act_pkg == 'text':
                            if self.libs["text"]:
                                if act_mdl == 'init': self.memory = self.text.init(args, self.memory)
                                elif act_mdl == 'cls_all': self.memory = self.text.cls_all(args, self.memory)
                                elif act_mdl == 'cls_left': self.memory = self.text.cls_left(args, self.memory)
                                elif act_mdl == 'cls_right': self.memory = self.text.cls_right(args, self.memory)
                                elif act_mdl == 'lower': self.memory = self.text.lower(args, self.memory)
                                elif act_mdl == 'upper': self.memory = self.text.upper(args, self.memory)
                                elif act_mdl == 'append_start': self.memory = self.text.append_start(args, self.memory)
                                elif act_mdl == 'append_end': self.memory = self.text.append_end(args, self.memory)
                                elif act_mdl == 'set': self.memory = self.text.set(args, self.memory)
                                else: raise TypeError(f'Unknown expression -> {line}.')
                            else: raise InternalError(f'text package are not used. Import it with ";extend" function.')

                        elif act_pkg == 'fstream':
                            if self.libs["fstream"]:
                                if act_mdl == 'create': self.fstream.create(args, self.memory)
                                elif act_mdl == 'read': self.memory = self.fstream.read(args, self.memory)
                                elif act_mdl == 'read_utf8': self.memory = self.fstream.read_utf8(args, self.memory)
                                elif act_mdl == 'wr': self.fstream.wr(args, self.memory)
                                elif act_mdl == 'wra': self.fstream.wra(args, self.memory)
                                elif act_mdl == 'remove': self.fstream.remove(args, self.memory)
                                elif act_mdl == 'exist': self.memory = self.fstream.exist(args, self.memory)
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
                                else:
                                    raise TypeError(f'Unknown expression -> {line}.')
                            else:
                                raise InternalError(f'console package are not used. Import it with ";extend" function.')

                        elif act_pkg == 'shell':
                            if self.libs["shell"]:
                                if act_mdl == 'execute': self.shell.execute(args, self.memory)
                                elif act_mdl == 'start_cmd': self.shell.start_cmd()
                                elif act_mdl == 'start_ps': self.shell.start_ps()
                                elif act_mdl == 'start_process': self.shell.start_process(args, self.memory)
                                else:
                                    raise TypeError(f'Unknown expression -> {line}.')
                            else:
                                raise InternalError(f'shell package are not used. Import it with ";extend" function.')

                        elif act_pkg == 'hash':
                            if self.libs["hash"]:
                                if act_mdl == 'md5': self.memory = Hash.md5(args, self.memory)
                                elif act_mdl == 'sha1': self.memory = Hash.sha1(args, self.memory)
                                elif act_mdl == 'sha512': self.memory = Hash.sha512(args, self.memory)
                                else:
                                    raise TypeError(f'Unknown expression -> {line}.')
                            else:
                                raise InternalError(f'hash package are not used. Import it with ";extend" function.')

                        elif act_pkg == 'dirsmgr':
                            if self.libs["dirsmgr"]:
                                if act_mdl == 'mk': Dirsmgr.mk(args, self.memory)
                                elif act_mdl == 'rm': Dirsmgr.rm(args, self.memory)
                                elif act_mdl == 'rm_tree': Dirsmgr.rm_tree(args, self.memory)
                                else:
                                    raise TypeError(f'Unknown expression -> {line}.')
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
                                    raise TypeError(f'Unknown expression -> {line}.')
                            else:
                                raise InternalError(f'env package are not used. Import it with ";extend" function.')
                        else:
                            raise InternalError(f'Unknown package use -> {act_pkg}. See list of available packges.')
            except InternalError as ie:
                Funcs.ThrowError(str(ie), 'InternalError', line, num)
                break

            except ExtendError as ee:
                Funcs.ThrowError(str(ee), 'ExtendError', line, num)
                break

            except TypeError as te:
                Funcs.ThrowError(str(te), 'TypeError', line, num)
                break

            except MemoryError as me:
                Funcs.ThrowError(str(me), 'MemoryError', line, num)
                break

            except PackageError as pe:
                Funcs.ThrowError(str(pe), 'PackageError', line, num)
                break

            except RuntimeError as re:
                Funcs.ThrowError(str(re), 'RuntimeError', line, num)
                break
