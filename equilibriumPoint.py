def equilibriumPoint(arr):
    sumi = 0
    k = sum(arr)
    for i in range(len(arr)):
        if sumi == k - arr[i] - sumi: return i + 1
        sumi += arr[i]
    return -1
