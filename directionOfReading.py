def directionOfReading(numbers):
    s = len(numbers)
    a = [list(str(i).zfill(s)) for i in numbers]
    d = [int("".join(i)) for i in zip(*a)]
    return d
