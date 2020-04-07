def arrayMaxConsecutiveSum(inputArray, k):
    result = 0
    currentSum = 0
    for i in range(k - 1):
        currentSum += inputArray[i]
    for i in range(k - 1, len(inputArray)):
        currentSum += inputArray[i]
        if currentSum > result:
            result = currentSum
        currentSum -= inputArray[i - k + 1]
    return result
