def maxSumSegments(inputArray):

    result = []
    for i in range(1, len(inputArray) + 1):
        sum = 0
        mxSum = 0
        index = -1
        for j in range(len(inputArray)):
            sum += inputArray[j]
            if j >= i:
                sum -= inputArray[j - i]
            if j >= i - 1 and (index == -1 or sum > mxSum):
                mxSum = sum
                index = j - i + 1
        result.append(index)
    return result
