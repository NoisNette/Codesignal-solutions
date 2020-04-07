def houseNumbersSum(inputArray):
    sm = 0
    i = 0
    while inputArray[i] != 0:
        sm += inputArray[i]
        i += 1
    return sm
