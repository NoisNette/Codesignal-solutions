def bishopAndPawn(bishop, pawn):
    return abs(ord(bishop[0]) - ord(pawn[0])) == abs(int(bishop[1]) - int(pawn[1]))
