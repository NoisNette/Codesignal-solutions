def growingPlant(upSpeed, downSpeed, desiredHeight):
    height = 0
    days = 0
    while height < desiredHeight:
        height += upSpeed
        days += 1
        if height >= desiredHeight:
            return days
        height -= downSpeed
    return days
