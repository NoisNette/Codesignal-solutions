def isInsideTheCircle(xa, ya, xc, yc, rc):
    dist = (xa - xc) * (xa - xc) + (ya - yc) * (ya - yc)
    rc *= rc
    if dist < rc:
        return True
    return False
