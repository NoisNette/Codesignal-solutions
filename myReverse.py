def myReverse(inputString):

    i = 0
    while i < len(inputString):
        tmp = inputString[i]
        inputString[i] = inputString[len(inputString) - i - 1]
        inputString[len(inputString) - i - 1] = tmp
        i += 1
    return inputString[::-1]
