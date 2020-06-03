def leapYear(year):
    from calendar import isleap
    return isleap(year)
    
# ALTERNATIVE
# def leapYear(year):
#     if year % 400 == 0: return True
#     if year % 100 == 0: return False
#     if year % 4 == 0: return True
#     return False
