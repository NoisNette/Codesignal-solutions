def quadraticEquation(a, b, c):

    discriminant = b*b - 4*a*c
    if discriminant < 0:
        return []
    if discriminant == 0:
        return [- b / (2 * a)]
    roots = []
    roots.append((- b - math.sqrt(discriminant) ) / (2 * a))
    roots.append((- b + math.sqrt(discriminant) ) / (2 * a))
    if roots[0] > roots[1]:
        tmp = roots[1]
        roots[1] = roots[0]
        roots[0] = tmp
    return roots
