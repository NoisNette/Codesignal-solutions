def isIdentityMatrix(matrix):

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if (matrix[i][j] != 1 and i == j
              or matrix[i][j] and i != j):
                return False
    return True
