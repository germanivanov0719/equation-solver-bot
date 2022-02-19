class Math:
    class AllRealNumbers(BaseException()):
        pass

    class ImaginaryNumbers(BaseException):
        pass

    class NotAQuadraticEquationError(BaseException):
        pass

    def solve_quadratic_eq(self, a: float, b: float, c: float) -> list:
        D = b ** 2 - (4 * a * c)
        if a == 0:
            raise self.NotAQuadraticEquationError
        elif D == 0:
            solution = (-b + D ** 0.5) / (2 * a)
            return [solution]
        elif D > 0:
            solution1 = (-b + D ** 0.5) / (2 * a)
            solution2 = (-b - D ** 0.5) / (2 * a)
            return [solution1, solution2]
        else:
            return [self.ImaginaryNumbers()]

    def solve_biquadratic_eq(self, a: float, b: float, c: float) -> list:
        # Let x^2 == y, and solve for y
        q_solutions = self.solve_quadratic_eq(a, b, c)
        roots = []
        for root in q_solutions:
            if isinstance(root, float) and root >= 0:
                roots.append(root ** 0.5)
                roots.append(-root ** 0.5)
        if len(roots) == 0:
            return [self.ImaginaryNumbers()]
        else:
            return roots

    # y = kx + b type of equations solved (for x)
    def solve_linear_eq(self, y: float, k: float, b: float) -> list:
        if k == 0 and (y - b) == 0:
            return [self.AllRealNumbers()]
        elif k == 0:
            return [self.ImaginaryNumbers()]
        else:
            return [(y - b) / k]
