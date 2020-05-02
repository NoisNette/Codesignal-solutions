def longestDigitsPrefix(inputString):
    pref = ""
    for l in inputString:
        if l.isdigit() == False: return pref
        else: pref += l
    return pref
