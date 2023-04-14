import heat_equation as he
import sympy

def get_result(controller):
    phi1 = sympy.sympify(controller['phi1'])
    phi2 = sympy.sympify(controller['phi2'])
    if controller['f'] == '':
        f = None
    else:
        f = sympy.sympify(controller['f'])
    a = sympy.sympify(controller['a'])
    l = sympy.sympify(controller['l'])

    if controller['kind'] == 0 and controller['type'] == 0:
        return he.solve_linear_combination_Dirichlet(phi1, a, f), controller

    if controller['kind'] == 0 and controller['type'] == 1:
        return he.solve_linear_combination_Neiman(phi1, a, f), controller