def parkingCost(timeIn, timeOut):
    diff = (int(timeOut[:2]) * 60 +
        int(timeOut[3:]) -
        int(timeIn[:2]) * 60 -
        int(timeIn[3:]))
    if diff <= 30:
        return 0
    if diff <= 120:
        return (diff - 21) // 10
    return 9 + ((diff - 110) // 10) * 2
