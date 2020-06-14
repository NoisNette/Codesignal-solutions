def inversePermutation(permutation):
    res = [0] * len(permutation)
    for i in range(len(permutation)): res[permutation[i] - 1] = i + 1
    return res
