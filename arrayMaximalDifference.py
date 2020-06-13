def arrayMaximalDifference(inputArray):
    answer = 0
    for i in range(len(inputArray)):
        for j in range(len(inputArray)):
            if inputArray[i] - inputArray[j] > answer:
                answer = inputArray[i] - inputArray[j]
    return answer
