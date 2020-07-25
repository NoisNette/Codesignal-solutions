def ballsRearranging(balls):
    balls.sort()
    i, mx = 0, 0
    for j in range(len(balls)):
        while balls[i] <= balls[j] - len(balls):
            i += 1
        mx = max(mx, j-i+1)
    return len(balls) - mx
