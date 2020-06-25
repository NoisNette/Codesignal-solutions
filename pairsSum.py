def pairsSum(a):
    setA = set(a)
    count = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] + a[j] in setA:
                count += 1
    return count
