class Formater:
    def ClearWhitespaces(text: str):
        text = text.strip()
        text = text.lstrip()
        text = text.rstrip()
        return text

    def FormatString(text: str):
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

