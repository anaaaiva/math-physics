import check
import nonuniformity as non_u
import sympy
from sympy.core.expr import Expr

def solve_linear_combination_Dirichlet(expression1: Expr, expression2: Expr, a, nonuniformity: Expr = None):
    t, x = sympy.symbols('t x')

    additional = sympy.Number(0) if (nonuniformity == None) else non_u.calculate_partial_solution(*non_u.devide_into_two(nonuniformity), a)

    expression1 = expression1 + additional.subs(t, 0)

    ans = sympy.Number(0)

    #For phi1
    if (expression1.func.is_Mul or expression1.func == sympy.sin or expression1.func == sympy.cos):
        expression1 = sympy.Add(0, expression1, evaluate=False)
    elif (not expression1.func.is_Add):
        raise Exception('Failed to solve linear Combination')

    logger1 = []

    for component in expression1.args :
        if (component.is_zero):
            continue

        coef, n = check.correct_form(component)

        logger1.append(f'c{len(logger1)} * {sympy.cos(a * n * t) * sympy.sin(n * x)}')

        ans = ans + coef * sympy.cos(a * n * t) * sympy.sin(n * x)

    #For phi2
    if (expression2.func.is_Mul or expression2.func == sympy.sin or expression2.func == sympy.cos):
        expression2 = sympy.Add(0, expression2, evaluate=False)
    elif (not expression2.func.is_Add):
        raise Exception('Failed to solve linear Combination')

    logger2 = []

    for component in expression2.args :
        if (component.is_zero):
            continue

        coef, n = check.correct_form(component)

        logger2.append(f'c{len(logger1) + len(logger2)} * {sympy.sin(a * n * t) * sympy.sin(n * x)}')

        ans = ans + coef * sympy.sin(a * n * t) * sympy.sin(n * x)

    return ans - additional



def solve_linear_combination_Neiman(expression1: Expr, expression2: Expr, a, nonuniformity: Expr = None):
    t, x = sympy.symbols('t x')

    additional = sympy.Number(0) if (nonuniformity == None) else non_u.calculate_partial_solution(*non_u.devide_into_two(nonuniformity), a)

    expression1 = expression1 + additional.subs(t, 0)

    ans = sympy.Number(0)

    #For phi1
    if (expression1.func.is_Mul or expression1.func == sympy.sin or expression1.func == sympy.cos):
        expression1 = sympy.Add(0, expression1, evaluate=False);
    elif (not expression1.func.is_Add):
        raise Exception('Failed to solve linear Combination')

    logger1 = []

    for component in expression1.args :
        if (component.is_zero) : continue

        coef, n = check.correct_form(component)

        logger1.append(f'c{len(logger1)} * {sympy.cos(a * n * t) * sympy.cos(n * x)}')

        ans = ans + coef * sympy.cos(a * n * t) * sympy.cos(n * x)

    #For phi2
    if (expression2.func.is_Mul or expression2.func == sympy.sin or expression2.func == sympy.cos):
        expression2 = sympy.Add(0, expression2, evaluate=False);
    elif (not expression2.func.is_Add):
        raise Exception('Failed to solve linear Combination')

    logger2 = []

    for component in expression2.args :
        if (component.is_zero):
            continue

        coef, n = check.correct_form(component)

        if (n != 0):
            logger2.append(f'c{len(logger1) + len(logger2)} * {sympy.sin(a * n * t) * sympy.cos(n * x)}')
        else:
            logger2.append(f'c{len(logger1) + len(logger2)} * {t}')

        if (n != 0):
            ans = ans + coef * sympy.sin(a * n * t) * sympy.cos(n * x)
        else:
            ans = ans + coef * t

    return ans - additional