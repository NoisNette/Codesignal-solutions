def isPermutation(n, inputArray):

    countOccurences = []

    for i in range(n):
        countOccurences.append(0)

    for i in range(len(inputArray)):
        if inputArray[i] - 1 < 0 or inputArray[i] - 1 >= n:
            return False
        countOccurences[ inputArray[i] - 1 ] += 1

    for i in range(n):
        if countOccurences[i] != 1:
            return False
    return True
