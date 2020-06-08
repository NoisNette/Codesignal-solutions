def bubbleSort(items):

    def swap(firstIndex, secondIndex):
        temp = items[firstIndex]
        items[firstIndex] = items[secondIndex]
        items[secondIndex] = temp

    length = len(items)

    for i in range(length):
        j = 0
        stop = length
        while j < stop - 1:
            if items[j] > items[j + 1]:
                swap(j, j + 1)
            j += 1
    return items
