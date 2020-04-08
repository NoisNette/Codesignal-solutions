def arrayMaxConsecutiveSum2(inputArray):
    precalc = [0]
    min_value = float('inf')
    res = float('-inf')

    for n in inputArray:
        precalc.append(precalc[-1] + n)
    
    for i, n in enumerate(precalc):
        if i != 0:
            min_value = min(min_value, precalc[i - 1])
        res = max(res, n - min_value)
    
    return res
