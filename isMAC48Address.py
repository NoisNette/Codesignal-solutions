def isMAC48Address(inputString):
    for i in range(len(inputString)):
        if i % 3 == 2:
            if inputString[i] != '-':
                return False
        else:
            sym = inputString[i]
            if not ('0' <= sym and sym <= '9' or 'A' <= sym and sym <= 'F'):
                return False
    return len(inputString) == 17
