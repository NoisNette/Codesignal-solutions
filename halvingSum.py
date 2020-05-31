def halvingSum(n):
    sum = 0
    i = n
    while i > 0:
        sum += i
        i //= 2
    return sum
