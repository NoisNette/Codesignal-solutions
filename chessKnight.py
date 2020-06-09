def chessKnight(cell):
    row = ord(cell[1]) - ord('0')
    column = ord(cell[0]) - ord('a') + 1
    steps = [
            [-2, -1], [-1, -2], [1, -2], [2, -1],
            [2, 1], [1, 2], [-1, 2], [-2, 1]
            ]
    answer = 0
    for i in range(len(steps)):
        tmpRow = row + steps[i][0]
        tmpColumn = column + steps[i][1]
        if (tmpRow >= 1 and tmpRow <= 8 and
            tmpColumn >= 1 and tmpColumn <= 8):
            answer += 1
    return answer
