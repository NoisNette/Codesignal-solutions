def chartFix(chart):
    def isIncreasing(cc):
        for j in range(len(cc)-1):
            if cc[j] >= cc[j+1]:
                return False
        return True
    
    if isIncreasing(chart):
        return 0

    dp = [0 for x in range(len(chart))]
    m = 1
    dp[0] = 1
    for i in range(1,len(chart)):
        dp[1] = 1
        for j in range(i-1,-1,-1):
            if (dp[j] + 1 > dp[i] and chart[j] < chart[i]):
                dp[i] = dp[j] + 1
            if (dp[i] > m):
                m = dp[i]
            
    return len(chart) - m
