def fixedPointsPermutation(permutation):
    c = 0
    for i in range(len(permutation)):
        if permutation[i] == i+1: c += 1
    return c
