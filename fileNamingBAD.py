# line 29 - INCOMPLETE - Codesignal Recover challenge - TODO 

def fileNaming(names):
    def calculateHash(inputString):
        P = 307
        M = 1000003
        hashValue = 0
        for i in range(len(inputString)):
            hashValue = (hashValue * P + ord(inputString[i])) % M
        return hashValue

    hashMapSize = len(names) * 2
    ##
    #     Information about the string in the hash map
    #     is stored in the following way:
    #     [string itself,
    #      its hash,
    #      the smallest possible integer to use with this name]
    ##
    hashMap = []
    result = []

    def searchHM(position, hashValue):
        while (hashMap[position][0] != ''
          and hashMap[position][1] != hashValue):
            position = (position + 1) % hashMapSize
        return position

    ...

    for i in range(len(names)):
        hashValue = calculateHash(names[i])
        startPos = searchHM(hashValue % hashMapSize, hashValue)
        if hashMap[startPos][0] == '':
            hashMap[startPos] = [names[i], hashValue, 1]
            result.append(names[i])
        else:
            newName = names[i] + '(' + str(hashMap[startPos][2]) + ')'
            newNameHash = calculateHash(newName)
            position = searchHM(newNameHash % hashMapSize, newNameHash)

            while hashMap[position][0] != '':
                hashMap[startPos][2] += 1
                newName = names[i] + '(' + str(hashMap[startPos][2]) + ')'
                newNameHash = calculateHash(newName)
                position = searchHM(newNameHash % hashMapSize, newNameHash)
            hashMap[position] = [newName, newNameHash, 1]
            result.append(newName)
            hashMap[startPos][2] += 1

    return result
