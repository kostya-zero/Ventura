cpdef IsText(str var, dict memory):
    if isinstance(memory[var], str):
        return True
    else:
        return False
