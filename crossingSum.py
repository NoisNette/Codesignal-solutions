def crossingSum(matrix, a, b):
    s = sum(matrix[a])
    for i in range(len(matrix)): s += matrix[i][b]
    return s - matrix[a][b]
