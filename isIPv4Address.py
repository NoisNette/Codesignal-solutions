def isIPv4Address(inputString):
    l = inputString.split('.')
    if len(l) != 4: return False
    for e in l:
        if e.isdigit() == False: return False
        if e == '' or (e.startswith('0') and e != '0') or int(e) > 255: return False
    return True
