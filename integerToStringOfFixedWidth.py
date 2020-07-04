def integerToStringOfFixedWidth(number, width):
    return str(number)[-width:] if len(str(number)) >= width else str(number).rjust(width, '0')
