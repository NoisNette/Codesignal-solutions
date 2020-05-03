def maxSubmatrixSum(matrix, n, m):

    result = 0
    for i in range(len(matrix) - n + 1):
        for j in range(len(matrix[0]) - m + 1):
            sumValue = 0
            for x in range(n):
                for y in range(m):
                    sumValue += matrix[i+x][j+y]
            if i == 0 and j == 0 or sumValue > result:
                result = sumValue

    return result
