def candles(candlesNumber, makeNew):
    res, rem = 0, 0
    while candlesNumber > 0:
        res += candlesNumber
        rem += candlesNumber
        candlesNumber = rem // makeNew
        rem = rem % makeNew
    return res
