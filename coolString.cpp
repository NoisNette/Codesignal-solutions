def coolString(inputString):

    def isLowercase(symbol):
        if 'a' <= symbol <= 'z':
            return True
        return False

    def isUppercase(symbol):
        if 'A' <= symbol <= 'Z':
            return True
        return False

    firstIsLowercase = isLowercase(inputString[0])
    firstIsUppercase = isUppercase(inputString[0])

    if not (firstIsLowercase or firstIsUppercase):
        return False

    for i in range(1, len(inputString)):
        if i % 2 != 0:
            if (isLowercase(inputString[i]) == firstIsLowercase or
                    isUppercase(inputString[i]) == firstIsUppercase):
                return False
        else:
            if (isLowercase(inputString[i]) != firstIsLowercase or
                    isUppercase(inputString[i]) != firstIsUppercase):
                return False

    return True
