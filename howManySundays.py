def howManySundays(n, startDay):

    week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday']
    startIndex = -1

    for i in range(len(week)):
        if week[i] == startDay:
            startIndex = i
            break

    return math.floor((n + startIndex) / len(week))
