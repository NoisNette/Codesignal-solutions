def digitDegree(n):

    def digitSum(n):
        sum = 0
        while n > 0:
            sum += n % 10
            n //= 10
        return sum

    result = 0

    while n > 9:
        result += 1
        n = sum(map(int, str(n)))

    return result
