from itertools import accumulate
def sumInRange(n, q):
    a ,res = tuple(accumulate([0]+n)),0
    for i,j in q:res += a[j+1]-a[i] 
    return res % 1000000007
