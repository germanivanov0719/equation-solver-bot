from telegram import MessageEntity
from res.number_classes import *


def solve_quadratic_eq(a, b, c):
    D = b ** 2 - (4 * a * c)
    if a == 0 and b == 0 and c == 0:
        return [AllRealNumbers()]
    elif a == 0 and b == 0:
        return []
    elif a == 0:
        return [-c/b]
    elif D == 0:
        square1 = (-b + D ** 0.5) / (2 * a)
        return [square1]
    elif D > 0:
        square1 = (-b + D ** 0.5) / (2 * a)
        square2 = (-b - D ** 0.5) / (2 * a)
        return [square1, square2]
    else:
        return [ImaginaryNumbers()]


def format_as_code(str):
    return '<code>' + str + '</code>'


def solve(a, b, c):
    r = solve_quadratic_eq(a, b, c)
    ret = []
    for item in r:
        if isinstance(item, float):
            if item // 1 != item:
                ret.append(item)
            else:
                ret.append(int(item))
        else:
            ret.append(item)
    if len(ret) == 1:
        if isinstance(ret[0], ImaginaryNumbers):
            return 'x ∉ ℝ'
        elif isinstance(ret[0], AllRealNumbers):
            return 'x ∈ ℝ'
        return 'x = ' + str(ret[0])
    elif len(ret) == 2:
        s = (f'{format_as_code("┌")}\n'
             f'{format_as_code("│")} x₁ = {str(ret[0])}\n'
             f'{format_as_code("│")} x₂ = {str(ret[1])}\n'
             f'{format_as_code("└")} \n')
        return s
    else:
        return 'x ∉ ø'
