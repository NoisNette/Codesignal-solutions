def capitalizeVowelsRegExp(inputString):

    lowercaseVowels = 'aeiouy'
    for i in range(len(lowercaseVowels)):
        regExp = re.compile(lowercaseVowels[i])
        inputString = re.sub(regExp, lowercaseVowels[i].upper(), inputString)

    return inputString
