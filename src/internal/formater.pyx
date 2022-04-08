from .funcs import Funcs
from .exceptions import TypeError
funcs = Funcs()
cpdef ClearWhitespaces(text: str):
    text = text.strip()
    text = text.lstrip()
    text = text.rstrip()
    return text

cpdef Format(text: str, memory: dict):
    if funcs.IsVar(text) and funcs.CheckVar(text, memory):
        return funcs.GetVar(text, memory)
    elif funcs.IsText(text):
        return text.strip('"')
    else:
        raise TypeError('Bad format.')

cpdef FormatArgument(arg: str, memory: dict):
    if funcs.IsVar(arg):
        if funcs.CheckVar(arg, memory):
            return memory[arg]
        else:
            raise TypeError(f'Variable {arg} are not located in memory.')
    elif funcs.IsText(arg):
        arg = arg.strip('"')
        arg = FormatString(arg)
        return arg
    elif funcs.IsNumber(arg):
        arg = arg.lstrip('*')
        arg = int(arg)
        return arg
    else:
        pass

cpdef FormatString(text: str):
    text = text.replace('%10', ' ')
    text = text.replace('%11', '!')
    text = text.replace('%12', '@')
    text = text.replace('%13', '#')
    text = text.replace('%14', '$')
    text = text.replace('%15', '№')
    text = text.replace('%16', ';')
    text = text.replace('%17', '%')
    text = text.replace('%18', '^')
    text = text.replace('%19', ':')
    text = text.replace('%20', '&')
    text = text.replace('%21', '?')
    text = text.replace('%22', '*')
    text = text.replace('%23', '/')
    text = text.replace('%24', '\\')
    return text