def concatenationProcess(initialArray):

    while len(initialArray) > 1:
        minInd1 = 0
        minInd2 = len(initialArray) - 1

        for i in range(1, len(initialArray)):
            if len(initialArray[i]) < len(initialArray[minInd1]):
                minInd1 = i

        if minInd2 == minInd1:
            minInd2 -= 1

        for i in range(len(initialArray) - 2, -1, -1):
            if (len(initialArray[i]) < len(initialArray[minInd2])
            and i != minInd1):
                minInd2 = i

        initialArray.append(initialArray[minInd1] + initialArray[minInd2])
        initialArray = (initialArray[:max(minInd1, minInd2)] +
                        initialArray[max(minInd1, minInd2) + 1:])
        initialArray = (initialArray[:min(minInd1, minInd2)] +
                        initialArray[min(minInd1, minInd2) + 1:])

    return initialArray[0]
