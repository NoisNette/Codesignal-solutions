def addDigits(a, b, n):
    rem = a % b

    result = []
    result.append(str(a))

    for i in range(n):
        best = -1
        for digit in range(9, -1, -1):
            if (rem * 10 + digit) % b == 0:
                best = digit
                break
        if best == -1:
            break
        result.append(str(best))
        rem = (rem * 10 + best) % b

    return ''.join(result)
