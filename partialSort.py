def partialSort(input, k):
    answer = []
    infinity = 10 ** 9

    for i in range(k):
        index = 0
        j = 0
        for j in range(len(input)):
            if input[j] < input[index]:
                index = j
        answer.append(input[index])
        input[index] = infinity
    for i in range(len(input)):
        if input[i] != infinity:
            answer.append(input[i])

    return answer
