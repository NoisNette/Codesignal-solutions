def differentValuesInMultiplicationTable(n, m):
    result = 0
    for value in range(1, n * m):
        for i in range(1, min(n, m) + 1):
            if value % i == 0 and value / i <= max(n, m):
                result += 1
                break
    return result + 1
