def properNounCorrection(noun):

    def isLowercase(symbol):
        if 'a' <= symbol and symbol <= 'z':
            return True
        return False

    result = []

    if isLowercase(noun[0]):
        result.append(chr(ord(noun[0])
            - ord('a') + ord('A')))
    else:
        result.append(noun[0])

    for i in range(1, len(noun)):
        if not isLowercase(noun[i]):
            result.append(chr(ord(noun[i])
                - ord('A') + ord('a')))
        else:
            result.append(noun[i])

    return ''.join(result)
