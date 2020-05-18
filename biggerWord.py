def biggerWord(w0):

    w = list(w0)
    leftSwap = -1
    for i in range(len(w) - 2, -1, -1):
        if w[i] < w[i + 1]:
            leftSwap = i
            break

    if leftSwap == -1:
        return 'no answer'

    rightSwap = len(w) - 1
    while w[leftSwap] >= w[rightSwap]:
        rightSwap -= 1

    w[leftSwap], w[rightSwap] = w[rightSwap], w[leftSwap]
    leftSwap += 1
    rightSwap = len(w) - 1
    while leftSwap < rightSwap:
        w[leftSwap], w[rightSwap] = w[rightSwap], w[leftSwap]
        leftSwap += 1
        rightSwap -= 1

    return ''.join(w)
