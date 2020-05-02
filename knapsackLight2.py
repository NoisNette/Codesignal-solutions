def knapsackLight2(weight1, weight2, maxW):

    if weight1 + weight2 <= maxW:
        return 'both'
    if min(weight1, weight2) > maxW:
        return 'none'
    if max(weight1, weight2) <= maxW:
        return 'either'
    if weight1 <= maxW:
        return 'first'
    return 'second'
