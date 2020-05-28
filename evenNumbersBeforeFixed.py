def evenNumbersBeforeFixed(sequence, fixedElement):

    result = 0

    for i in range(len(sequence)):
        if sequence[i] % 2 == 0 and sequence[i] != fixedElement:
            result += 1
        if sequence[i] == fixedElement:
            return result

    return -1
