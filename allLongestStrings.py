def allLongestStrings(inputArray):
    mx = 0
    for s in inputArray:
        if len(s) > mx: mx = len(s)
    ans = []
    for s in inputArray:
        if len(s) == mx: ans.append(s)
    return ans
