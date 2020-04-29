def minSubstringWithAllChars(s, t):
    i = len(t)
    while i<=len(s):
        for j in range(i,len(s)+1):
            if all([True if e in s[j-i:j] else False for e in t]):
                return(s[j-i:j])
        i+=1
    return(False)
