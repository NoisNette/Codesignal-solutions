def arrayMinimumAboveBound(inputArray, bound):

    best = 100000
    for i in range(len(inputArray)):
        if (inputArray[i] > bound and
                (inputArray[i] < best)):
            best = inputArray[i]

    return best
