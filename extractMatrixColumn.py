def extractMatrixColumn(matrix, column):
    l = []
    for i in range(len(matrix)):
        l.append(matrix[i][column])
    return l
