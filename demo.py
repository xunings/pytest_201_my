class MysteryError(Exception):
    pass

def add(a, b):
    if a == 99:
        raise MysteryError()
    return a + b

def subtract(a, b):
    return a - b
