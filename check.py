import sympy
from sympy.core.expr import Expr
from sympy.functions.elementary.trigonometric import cos, sin

def check_validity(expression: Expr):
    for arg in expression.args:
        if len(arg.args) == 0:
            if not arg.is_number and arg != sympy.Symbol('x') and arg != sympy.Symbol('t'):
                raise NotImplementedError('Wrong input function in check validity')
        else:
            check_validity(arg)

def just_x(expression: Expr):
    for arg in expression.args :
        if len(arg.args) == 0:
            if not arg.is_number and arg != sympy.Symbol('x'):
                return False
        else:
            if not just_x(arg):
                return False
    return True


def just_t(expression: Expr):
    for arg in expression.args:
        if len(arg.args) == 0:
            if not arg.is_number and arg != sympy.Symbol('t'):
                return False
        else:
            if not just_t(arg):
                return False
    return True


def correct_form(expression: Expr):
    if expression.is_constant():
        return expression, 0
    coef, trig, n = sympy.Number(1), sympy.Number(1), sympy.Number(1)
    if expression.func.is_Mul:
        for arg in expression.args:
            if arg.is_constant():
                coef = coef * arg
            elif arg.func == sin or arg.func == cos:
                trig = trig * arg
            else:
                raise NotImplementedError('Unexpected expression in correct form 1')
    elif expression.func == sin or expression.func == cos:
        trig = expression
    else:
        raise NotImplementedError('Unexpected expression in correct form 2')

    for arg in trig.args[0].args:
        if arg.is_constant():
            n *= arg
    return coef, n