from math import sin
from generic_newton_cotes import generic_newton_cotes


def newton_cotes(p, func, a, b, closed_interval=True):
    '''
        Aproximate <func> using a polynomial of degree <p>
        to integrate [<a>, <b>] if <closed_interval> is true,
        else (<a>, <b>)
    '''
    h = (b - a) / p
    x = lambda s: a + s * (h + int(not closed_interval))
    g = lambda s: func(x(s))

    if p == 1:
        return h/2 * (g(0) + g(1))
    elif p == 2:
        return h/3 * (g(0) + 4*g(1) + g(2))
    elif p == 3:
        return 3*h/8 * (g(0) + 3*g(1) + 3*g(2) + g(3))
    elif p == 4:
        return 2*h/45 * (7*g(0) + 32*g(1) + 12*g(2) + 32*g(3) + 7*g(4))
    elif p > 4:
        formula = generic_newton_cotes(p, a, b)
        symbols = {s: g(int(str(s).split('_')[1])) for s in formula.free_symbols}
        return formula.subs(symbols)


if __name__ == '__main__':

    for i in range(1, 10, 1):
        
        a, b = 0, 1
        print('grau {} = {}'.format(
            i, newton_cotes(i, lambda x: (sin(2*x) + 4*x**2 + 3*x)**2, a, b)))

        
