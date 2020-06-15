def findTheRemainder(a, b):
    return a % b
    
              |
# BUGFIX PART V

def findTheRemainder(a, b):   
    while a >= b:
        a -= b
    return a
