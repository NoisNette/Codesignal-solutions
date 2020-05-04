def avoidObstacles(inputArray):
    step = 2
    while True:
        valid = True
        for num in inputArray:
            if num % step == 0:
                valid = False
                break
        if valid: return step
        step += 1
