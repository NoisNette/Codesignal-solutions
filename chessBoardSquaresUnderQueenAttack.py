def chessBoardSquaresUnderQueenAttack(a, b):

    def go(x, y, dx, dy):
        if x < 0 or x >= a or y < 0 or y >= b:
            return 0
        return go(x + dx, y + dy, dx, dy) + 1

    res = 0

    for i in range(a):
        for j in range(b):
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx != 0 or dy != 0:
                        res += go(i, j, dx, dy) - 1

    return res
