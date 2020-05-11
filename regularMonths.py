from datetime import datetime
def regularMonths(currMonth):

    d = datetime.strptime(currMonth, '%m-%Y')
    m = d.month
    y = d.year

    while True:
        if m % 12 == 0:
            y += 1
        m = (m % 12) + 1
        d = datetime(y, m, 1)
        print(d)
        if d.weekday() == 0:
            # Today is a Monday.
            return datetime.strftime(d, '%m-%Y')
