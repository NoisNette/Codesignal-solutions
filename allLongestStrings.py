def allLongestStrings(inputArray):
    return [s for s in inputArray if len(s) == len(max(inputArray, key=len))]
