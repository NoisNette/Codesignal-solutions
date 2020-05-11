def segmentSumsMatrix2(inputArray):

    answer = []
    for i in range(len(inputArray)):
        line = []
        for j in range(len(inputArray)):
            line.append(0)
        answer.append(line)

    for i in range(len(inputArray)):
        answer[i][i] = inputArray[i]
        for j in range(i + 1, len(inputArray)):
            answer[i][j] = answer[i][j - 1] + inputArray[j]

    for i in range(len(inputArray)):
        for j in range(i + 1, len(inputArray)):
            answer[j][i] = answer[i][j]

    return answer
