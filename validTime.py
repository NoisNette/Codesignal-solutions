def validTime(time):
    h,m = map(int, time.split(":"))
    return (0 <= h <= 23 and 0 <= m < 60) or (h == 23 and 0 <= m < 60)
