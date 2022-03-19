import internal.formater as Formater
from internal.exceptions import TypeError, MemoryError
cpdef resolve(args: str, memory: dict):
    if args.startswith('@'):
        if args.startswith('@if_equals'):
            if args.count(':') == 1:
                split = args.split(':')
                args = split[1].strip()
                if args.count(',') == 1:
                    split_args = args.split(',')
                    arg1 = split_args[0].strip()
                    arg2 = split_args[1].strip()

                    if arg1.startswith('$') and not arg1.startswith('$__'):
                        if arg1 in memory.keys():
                            arg1 = memory[arg1]
                        else:
                            raise MemoryError('Variable are not registered -> ' + arg1)
                    elif arg1.startswith('"') and arg1.endswith('"'):
                        arg1 = arg1.strip('"')
                        arg1 = Formater.FormatString(arg1)
                    else:
                        raise TypeError('Bad argument format.')
                    
                    if arg2.startswith('$') and not arg2.startswith('$__'):
                        if arg2 in memory.keys():
                            arg2 = memory[arg2]
                        else:
                            raise MemoryError('Variable are not registered -> ' + arg2)
                    elif arg2.startswith('"') and arg2.endswith('"'):
                        arg2 = arg2.strip('"')
                        arg2 = Formater.FormatString(arg2)
                    else:
                        raise TypeError('Bad argument format.')

                    if arg1 == arg2:
                        return True
                    else:
                        return False
                else:
                    raise TypeError('@if_equals can receive only two argument.')
            else:
                raise TypeError('@if_equals statement must have only one ":".')

        elif args.startswith('@if_notequals'):
            if args.count(':') == 1:
                split = args.split(':')
                args = split[1].strip()
                if args.count(',') == 1:
                    split_args = args.split(',')
                    arg1 = split_args[0].strip()
                    arg2 = split_args[1].strip()

                    if arg1.startswith('$') and not arg1.startswith('$__'):
                        if arg1 in memory.keys():
                            arg1 = memory[arg1]
                        else:
                            raise MemoryError('Variable are not registered -> ' + arg1)
                    elif arg1.startswith('"') and arg1.endswith('"'):
                        arg1 = arg1.strip('"')
                        arg1 = Formater.FormatString(arg1)
                    else:
                        raise TypeError('Bad argument format.')

                    if arg2.startswith('$') and not arg2.startswith('$__'):
                        if arg2 in memory.keys():
                            arg2 = memory[arg2]
                        else:
                            raise MemoryError('Variable are not registered -> ' + arg2)
                    elif arg2.startswith('"') and arg2.endswith('"'):
                        arg2 = arg2.strip('"')
                        arg2 = Formater.FormatString(arg2)
                    else:
                        raise TypeError('Bad argument format.')

                    if not arg1 == arg2:
                        return True
                    else:
                        return False
                else:
                    raise TypeError('@if_equals can receive only two argument.')
            else:
                raise TypeError('@if_equals statement must have only one ":".')
        else:
            raise TypeError('Bad statement for internal action.')
