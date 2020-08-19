def isSum(value):
    n = math.floor(math.sqrt(2 * value))
    return (n * (n + 1) // 2) == value
