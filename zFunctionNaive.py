def zFunctionNaive(s):
    z = [0 for _ in range(len(s))]
    z[0] = len(s)
    for i in range(1, len(s)):
        while i + z[i] < len(s) and s[z[i]] == s[i + z[i]]: z[i] += 1
    return z
