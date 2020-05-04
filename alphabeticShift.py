def alphabeticShift(inputString):

    chars = list(inputString)
    for i in range(len(chars)):
        number = ord(chars[i]) - ord('a')
        number = (number + 1) % 26
        chars[i] = chr(number + ord('a'))
    return ''.join(chars)
