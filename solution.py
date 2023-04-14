import heat_equation as he
import wave_equation as we
import sympy

#БОЖЕ МОЙ, ЭТА ЧЕРТОВА ФУНКЦИЯ МОЕ СПАСЕНИЕ
from sympy.simplify.fu import TRpower

def get_result(controller):
    phi1 = TRpower(sympy.sympify(controller['phi1']))
    phi2 = TRpower(sympy.sympify(controller['phi2']))
    if controller['f'] == '':
        f = None
    else:
        f = TRpower(sympy.sympify(controller['f']))
    a = sympy.sympify(controller['a'])
    l = sympy.sympify(controller['l'])

    if controller['kind'] == 0 and controller['type'] == 0:
        return he.solve_linear_combination_Dirichlet(phi1, a, f), controller

    if controller['kind'] == 0 and controller['type'] == 1:
        return he.solve_linear_combination_Neiman(phi1, a, f), controller

    if controller['kind'] == 1 and controller['type'] == 0:
        return we.solve_linear_combination_Dirichlet(phi1, phi2, a, f), controller

    if controller['kind'] == 1 and controller['type'] == 1:
        return we.solve_linear_combination_Neiman(phi1, phi2, a, f), controller
