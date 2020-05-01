def matrixTrace(matrix):

    result = 0
    for i in range(len(matrix)):
        result += matrix[i][i]
    return result
