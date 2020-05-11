def arrayMaximalAdjacentDifference(inputArray):
    mx = 0
    for i in range(1, len(inputArray)):
        if abs(inputArray[i] - inputArray[i-1]) > mx: mx = abs(inputArray[i] - inputArray[i-1])
    return mx
