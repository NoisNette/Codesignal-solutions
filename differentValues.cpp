def differentValues(a, d):
    n = len(a)
    best = -1
    for i in range(n):
        for j in range(i + 1, n):
            diff = abs(a[i] - a[j])
            if diff <= d:
                if best == -1: best = diff
                else: best = max(best, diff)
                if best == d: break
    return best
