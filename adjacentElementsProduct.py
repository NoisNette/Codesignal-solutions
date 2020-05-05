def adjacentElementsProduct(inputArray):
    res = -1000000000
    for i in range(len(inputArray)-1):
        prod = inputArray[i] * inputArray[i+1]
        res = max(res, prod)
    return res
