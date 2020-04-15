def swapCase(text):
    s = ""
    for l in text:
        if l.islower(): s += l.upper()
        else: s += l.lower()
    return s
