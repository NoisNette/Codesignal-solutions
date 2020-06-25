def stringsCrossover(a, r):
    t = 0
    for i in range(len(a)):
        for j in range( i + 1, len(a)):
            for k in range(len(r)):
                if not (a[i][k] == r[k] or a[j][k] == r[k]):
                    break
            else:
                t += 1
    return t
