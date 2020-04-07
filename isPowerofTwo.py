def isPowerOfTwo(n):
    while n % 2 == 0:
        n >>= 1
    if n == 1:
        return True
    return False
