def countIncreasingSequences(n, k):
    dp = []
    ans = 0

    for i in range(n + 1):
        line = []
        for j in range(k + 1):
            line.append(0)
        dp.append(line)
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            for q in range(j):
                dp[i][j] += dp[i - 1][q]

    for j in range(1, k + 1):
        ans += dp[n][j]

    return ans
