def binaryGenerator(s):
    t = [s]
    for i in range(len(s)):
        if s[i]=='0':
            aux = []
            for e in t:
                aux.append(e[:i]+'1'+e[i+1:])
                aux.append(e[:i]+'0'+e[i+1:])
            t = aux
    return(sorted(t))
