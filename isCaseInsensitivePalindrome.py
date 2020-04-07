def isCaseInsensitivePalindrome(inputString):

    for i in range(len(inputString) // 2):
        c = [
                inputString[i],
                inputString[len(inputString) - i - 1]
        ]
        for j in range(2):
            if c[j] >= 'a' and c[j] <= 'z':
                c[j] = chr(
                        ord(c[j]) - ord('a') + ord('A')
                )
        if c[0] != c[1]:
            return False

    return True
