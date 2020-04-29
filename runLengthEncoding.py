def runLengthEncoding(inputString):

    repeatLength = 1
    answer = []
    for i in range(1, len(inputString)):
        if inputString[i] != inputString[i - 1]:
            answer.append(str(repeatLength))
            answer.append(inputString[i-1])
            repeatLength = 1
        else:
            repeatLength += 1
    answer.append(str(repeatLength))
    answer.append(inputString[len(inputString) - 1])
    return ''.join(answer)
