def maximalSquare(matrix):
    m, n = len(matrix), len(matrix[0]) if matrix else 0

    dp, maxWidth = [[0] * (n + 1) for _ in range(m + 1)], 0
    for i, row in enumerate(matrix, 1):
        for j, num in enumerate(row, 1):
            if num == '1':
                dp[i][j] = min(
                    dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                maxWidth = max(dp[i][j], maxWidth)
    return maxWidth * maxWidth
