def permutationShift(permutation):
    ans = []
    s = sorted(permutation)
    for i in range(len(permutation)):
        a = permutation[i]
        x = s.index(a) - i
        ans.append(x)
    return max(ans) - min(ans)
