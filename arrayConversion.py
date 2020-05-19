def arrayConversion(inputArray):

    operation = 1
    while len(inputArray) > 1:
        newArray = []
        for i in range(0, len(inputArray), 2):
            if operation % 2 == 1:
                newArray.append(inputArray[i] + inputArray[i + 1])
            else:
                newArray.append(inputArray[i] * inputArray[i + 1])
        inputArray = newArray
        operation += 1

    return inputArray[0]
