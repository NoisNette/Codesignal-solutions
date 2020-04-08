def longestCommonSubstring(s, t):
    modulo = 10 ** 9 + 7
    prime = 103
    s = [ord(x) for x in s]
    t = [ord(x) for x in t]
    def rolling_hash(f, m):
        tmp = {}
        k, power = 0, 1
        for i in range(m) :
            k, power = k % modulo + f[i] * power % modulo, power * prime % modulo
        tmp[k] = ~-m
        for i in range(m, len(f) ): 
            k = (k + f[i] * power -  f[i-m]) * 572815538 % modulo
            tmp[k] = i
        return tmp
    def binary_search(m):
        hash = rolling_hash(s, m)
        for k, j in rolling_hash(t, m).items():
            if k in hash and s[hash[k] - m + 1: hash[k] + 1] == t[j - m + 1 : j + 1] : return 1
        return 0
    left = 0
    right = min(len(s), len(t))
    while left < right:
        middle = left + right + 1 >> 1
        if binary_search(middle):
            left = middle
        else:
            right = middle - 1
    
    return left
