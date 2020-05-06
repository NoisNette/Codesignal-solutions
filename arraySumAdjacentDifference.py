def arraySumAdjacentDifference(inputArray):

    answer = 0
    for i in range(1, len(inputArray)):
        answer += abs(inputArray[i] - inputArray[i - 1])
    return answer
