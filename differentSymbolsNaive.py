def differentSymbolsNaive(s):
    un = ""
    for l in s:
        if l not in un: un += l
    return len(un)
