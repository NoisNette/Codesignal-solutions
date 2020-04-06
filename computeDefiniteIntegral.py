import math
def computeDefiniteIntegral(l, r, p):
    R = 0
    L = 0
    for i in range(1, len(p)+1):
        R += p[i-1]*math.pow(r, i)/i
        L += p[i-1]*math.pow(l, i)/i
    return R - L
