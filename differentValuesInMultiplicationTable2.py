def differentValuesInMultiplicationTable2(n, m):
    found = [False] * (n * m + 1)
    result = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            found[i * j] = True

    for value in range(1, n * m + 1):
        if found[value]:
            result += 1

    return result
