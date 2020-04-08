def findLongestSubarrayBySum(s, a):
    total = j = 0
    res = (0,-1)
    for i,v in enumerate(a):
        total += v
        while j<=i and total>s:
            total -= a[j]
            j += 1
        if (total == s) and (res[1]-res[0]<i-j):
            res=(j+1,i+1)
    return res if res[0] else [-1]
