n, k, l = eval(dir()[0])
p = 1
m = 10**9 + 7
while l*k:
    l -= 1
    k -= 1
    p = p*n%m
    n -= 1
return p * pow(n, l, m) % m
