def countDistantPairs(inputString, distance):
    answer = 0
    for i in range(len(inputString) - distance - 1):
        if inputString[i] == inputString[i + distance + 1]:
            answer += 1

    return answer
