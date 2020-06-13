def arrayMaximalDifference(inputArray):
    ans = 0
    for el1 in inputArray:
        for el2 in inputArray:
            if el1 - el2 > ans: ans = el1 - el2
    return ans
