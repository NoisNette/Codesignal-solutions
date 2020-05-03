def chessKnightMoves(cell):

    def isValid(pos):
        if 0 <= pos and pos < 8:
            return True
        return False

    def getX(pos):
        return ord(pos) - ord('a')

    def getY(pos):
        return ord(pos) - ord('1')

    current_x = getX(cell[0])
    current_y = getY(cell[1])
    result = 0

    for dx in range(-2, 3):
        for dy in range(-2, 3):
            if abs(dx * dy) == 2:
                if isValid(current_x + dx) and isValid(current_y + dy):
                    result += 1
    return result
