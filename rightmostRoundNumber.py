def rightmostRoundNumber(inputArray):

    ans = -1
    for i in range(len(inputArray)):
        if inputArray[i] % 10 == 0:
            ans = i

    return ans
