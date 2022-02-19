from telegram import MessageEntity
from res.math import *
from res.handlers import BIQUADRARIC_MODE


def format_as_code(str):
    return '<code>' + str + '</code>'


def solve(a, b, c):
    m = Math()
    try:
        if BIQUADRARIC_MODE:
            r = m.solve_biquadratic_eq(a, b, c)
        else:
            r = m.solve_quadratic_eq(a, b, c)
    except m.NotAQuadraticEquationError:
        return m.solve_linear_eq(0, b, -c)
    ret = []
    for item in r:
        if isinstance(item, float):
            if item // 1 != item:
                ret.append(item)
            else:
                ret.append(int(item))
        else:
            ret.append(item)
    ret = list(set(ret))
    if len(ret) == 1:
        if isinstance(ret[0], m.ImaginaryNumbers):
            return 'x ∉ ℝ'
        elif isinstance(ret[0], m.AllRealNumbers):
            return 'x ∈ ℝ'
        return 'x = ' + str(ret[0])
    elif len(ret) >= 2:
        s = [f'{format_as_code("┌")}',
             f'{format_as_code("└")} ']
        signs = '₁₂₃₄'
        i = 0
        for i in range(len(ret)):
            s.insert(-1, f'{format_as_code("│")} x{signs[i]} = {str(ret[i])}')
        return '\n'.join(s)
    else:
        return 'x ∉ ø'
