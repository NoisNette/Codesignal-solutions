def rightmostRoundNumber(arr):
    for i in range(len(arr)-1, -1, -1):
        if arr[i] % 10 == 0: return arr.index(arr[i])
    return -1
