def area(a, b, c):
    if a >= 0 and b >= 0 and c >= 0:
        return (a + b + c) / 2
    else:
        raise ValueError("Size must be > 0.")


def perimeter(a, b, c):
    if a >= 0 and b >= 0 and c >= 0:
        return a + b + c
    else:
        raise ValueError("Size must be > 0.")
