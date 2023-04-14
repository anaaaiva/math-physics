import check
import sympy
from sympy.core.expr import Expr

def devide_into_two(expression: Expr):
    F, G = sympy.Number(1), sympy.Number(1)

    if (check.just_t(expression)):
        return expression, G
    elif (check.just_x(expression)):
        return F, expression

    if not expression.func.is_Mul:
        raise Exception('Complex nonuniform function')

    for arg in expression.args:
        if check.just_t(arg):
            F = F * (arg)
        elif check.just_x(arg):
            G = G * (arg)
        else:
            raise Exception('Complex nonuniform function')

    return F, G


# MUST BE TRUE : G''(x) == -(k**2) * G(x)
def calculate_partial_solution(F: Expr, G: Expr, a = 1):
    x, t, k, c1 = sympy.symbols('x t k C1')

    kSquared = sympy.solveset(sympy.Eq(G.diff(x, x), -(k) ** 2 * G), k ** 2).args[0]

    w = sympy.symbols('w', cls=sympy.Function)
    w = sympy.dsolve( sympy.Eq(w(t).diff(t), (a ** 2) * (-1) * kSquared * w(t) + F), w(t)).args[1]

    return w.subs(c1, 0) * G