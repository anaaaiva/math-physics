import check
import nonuniformity as non_u
import sympy
from sympy.core.expr import Expr

def solve_linear_combination_Dirichlet (expression: Expr, a, nonuniformity: Expr = None) :
    t, x = sympy.symbols('t x')

    additional = sympy.Number(0) if nonuniformity == None else non_u.calculate_partial_solution(*non_u.devide_into_two(nonuniformity), a)

    expression = expression + additional.subs(t, 0)

    ans = sympy.Number(0)

    if (expression.func.is_Mul or expression.func == sympy.sin or expression.func == sympy.cos):
        expression = sympy.Add(0, expression, evaluate=False)
    elif (not expression.func.is_Add):
        raise Exception('Failed to solve linear Combination')

    logger = []

    for component in expression.args :
        if (component.is_zero):
            continue

        coef, n = check.correct_form(component)

        logger.append(f'c{len(logger)} * {sympy.exp(-a**2 * n**2 * t) * sympy.sin(n * x)}')

        ans +=  coef * sympy.exp(-a**2 * n**2 * t) * sympy.sin(n * x)
    return ans - additional

def solve_linear_combination_Neiman (expression: Expr, a, nonuniformity: Expr = None):
    t, x = sympy.symbols('t x')

    additional = sympy.Number(0) if (nonuniformity == None) else non_u.calculate_partial_solution(*non_u.devide_into_two(nonuniformity), a)

    expression = expression + additional.subs(t, 0)

    ans = sympy.Number(0)

    if (expression.func.is_Mul or expression.func == sympy.sin or expression.func == sympy.cos):
        expression = sympy.Add(0, expression, evaluate=False)
    elif (not expression.func.is_Add):
        raise Exception('Failed to solve linear Combination')

    logger = []

    for component in expression.args :
        if (component.is_zero):
            continue

        coef, n = check.correct_form(component)

        logger.append(f'c{len(logger)} * {sympy.exp(-a**2 * n**2 * t) * sympy.cos(n * x)}')

        ans = ans + coef * sympy.exp(-a**2 * n**2 * t) * sympy.cos(n * x)

    return ans - additional