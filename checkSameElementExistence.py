def checkSameElementExistence(arr1, arr2):
    return bool(len(set(arr1).intersection(set(arr2))))
