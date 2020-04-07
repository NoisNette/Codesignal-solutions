def subsetsSequence(sets):
    def isSubset(setA, setB):
        j = 0
        for i in range(len(setB)):
            if j < len(setA) and setA[j] == setB[i]:
                j += 1
        if j == len(setA):
            return True
        else:
            return False
    supersets = [0] * len(sets)
    for i in range(len(sets)):
        sets[i].sort()
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            if isSubset(sets[i], sets[j]):
                supersets[i] += 1
            if isSubset(sets[j], sets[i]):
                supersets[j] += 1
    supersets.sort()
    for i in range(len(sets)):
        if supersets[i] < i:
            return False
    return True
