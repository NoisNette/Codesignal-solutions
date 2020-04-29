def applesDistribution(apples, boxCapacity, maxResidue):
    result = 0
    for i in range(1, boxCapacity + 1):
        if apples % i <= maxResidue:
            result += 1
    return result
