def maxSubarray(inputArray):
        currentMax = 0
        result = 0
        for i in range(len(inputArray)):
                currentMax = max(0, currentMax + inputArray[i])
                result = max(result, currentMax)
        return result
