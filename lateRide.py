def lateRide(n):
    return sum(map(int, str(n // 60) + str(n % 60)))
