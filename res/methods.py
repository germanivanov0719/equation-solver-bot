from res.number_classes import *

def solve_quadratic_eq(a, b, c):
    D = b ** 2 - (4 * a * c)
    if a == 0 and b == 0 and c == 0:
        return AllRealNumbers()
    elif a == 0 and b == 0:
        return []
    elif a == 0:
        return -c/b
    elif D == 0:
        square1 = (-b + D ** 0.5) / (2 * a)
        return square1
    elif D > 0:
        square1 = (-b + D ** 0.5) / (2 * a)
        square2 = (-b - D ** 0.5) / (2 * a)
        return [square1, square2]
    else:
        return ImaginaryNumbers()
