def cyclicQueue(commands):

    maxSize = 10
    queue = [0] * maxSize
    answer = []
    head = 0
    tail = 0
    currentSum = 0

    for i in range(len(commands)):
        if commands[i] == '-':
            currentSum -= queue[head]
            head = (head + 1) % maxSize
        else:
            value = 0
            value += int(commands[i][1:])
            currentSum += value
            queue[tail] = value
            tail = (tail + 1) % maxSize
        answer.append(currentSum)

    return answer
