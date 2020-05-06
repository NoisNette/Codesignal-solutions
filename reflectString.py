def reflectString(inputString):

    result = []
    for i in range(len(inputString)):
        order = ord(inputString[i]) - ord('a')
        reflectedCharCode = ord('a') + 25 - order
        result.append( chr(reflectedCharCode))

    return ''.join(result)
