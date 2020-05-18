def maximalEven(inputArray):
    arr = reversed(sorted(inputArray))
    for i in arr:
        if i % 2 == 0: return i
