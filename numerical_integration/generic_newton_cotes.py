import sympy as sp


def combination(n, k):
    acc = 1
    fact = 1
    for i in range(k):
        acc *= n - i
        fact *= i + 1

    acc = acc / fact

    return acc


def delta_r_rec(k, i):
    if k == 0:
        return sp.Symbol('r_{}'.format(i))
    
    return delta_r_rec(k-1, i+1) - delta_r_rec(k-1, i)


def delta_r_iter(k, i, x=0):
    acc = 0
    for i in range(k+1):
        acc += (-1)**i * combination(k, i) * sp.Symbol('r_{}'.format(k-i+x))

    return acc


def generic_newton_cotes(p, a, b):

    s = sp.Symbol('s')
    h = (b - a) / p
    formula = 0
    for k in range(p+1):
        formula += combination(s, k) * delta_r_iter(k, 0)

    integral = sp.integrate(formula, (s, 0, p))
    integral = h * integral

    return integral


if __name__ == '__main__':

    sp.init_printing()
    x = sp.Symbol('x')

    for i in range(1, 5, 1):
        formula = generic_newton_cotes(i, 0, 1)
        sp.pprint(formula)
