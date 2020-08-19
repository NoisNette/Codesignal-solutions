def extractEachKth(inputArray, k):
    return [inputArray[i - 1] for i in range(1, len(inputArray) + 1) if i % k]


# def extractEachKth(inputArray, k):
#     l = []
#     for i in range(1, len(inputArray)+1):
#         if (i) % k != 0:
#             l.append(inputArray[i-1])
#     return l
