def countWaysToChangeDigit(value):
    answer = 0
    while value > 0:
        answer += 9 - value % 10
        value //= 10
    return answer
