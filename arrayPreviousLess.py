def arrayPreviousLess(items):
    result = []
    for i in range(len(items)):
        substitute = -1
        for j in range(i):
            if items[j] < items[i]:
                substitute = items[j]
        result.append(substitute)

    return result
