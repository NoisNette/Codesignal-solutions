def isoscelesTriangle(sides):
    sides = sorted(sides)
    return sides[0] == sides[1] or sides[1] == sides[2]
