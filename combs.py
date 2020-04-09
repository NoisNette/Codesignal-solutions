def combs(comb1, comb2):

    def getMask(comb):
        mask = 0
        for i in range(0, len(comb)):
            c = comb[i]
            mask = (mask << 1) + (c == '*')
        return mask

    m1 = getMask(comb1)
    m2 = getMask(comb2)
    len1 = len(comb1)
    len2 = len(comb2)
    answer = len1 + len2
    for i in range(-len1, len2 + 1):
        if i < 0:
            tmp = m2 << (-i) & m1
            length = max(-i + len2, len1)
        else:
            tmp = m1 << i & m2
            length = max(i + len1, len2)
        if tmp == 0 and answer > length:
            answer = length

    return answer
