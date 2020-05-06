def isSkewSymmetricMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            if matrix[i][j] != -matrix[j][i]: return False
    return True
