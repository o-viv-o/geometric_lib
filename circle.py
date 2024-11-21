import math


def area(r):
    if r >= 0:
        return math.pi * r * r
    else:
        raise ValueError("Radius must be greater than zero.")


def perimeter(r):
    if r >= 0:
        return 2 * math.pi * r
    else:
        raise ValueError("Radius must be greater than zero.")
