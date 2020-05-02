def knapsackLight(v1, w1, v2, w2, maxW):
    if w1 + w2 <= maxW:
        return v1 + v2
    else:
        if v1 > v2:
            if w1 <= maxW:
                return v1
            elif w2 <= maxW:
                return v2
            else:
                return 0
        elif v1 < v2:
            if w2 <= maxW:
                return v2
            elif w1 <= maxW:
                return v1
            else:
                return 0
        else:
            return v1
