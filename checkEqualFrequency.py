def checkEqualFrequency(inputArray):

    numberOfEqual = 1

    inputArray.sort()

    while (numberOfEqual < len(inputArray)
            and inputArray[numberOfEqual - 1] == inputArray[numberOfEqual]):
        numberOfEqual += 1

    if len(inputArray) % numberOfEqual != 0:
        return False

    for i in range(0, len(inputArray), numberOfEqual):
        if i > 0 and inputArray[i] == inputArray[i - 1]:
            return False
        j = i + 1
        while j < i + numberOfEqual:
            if inputArray[j] != inputArray[j - 1]:
                return False
            j += 1

    return True
