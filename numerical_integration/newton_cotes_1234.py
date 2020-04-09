from math import sin
from generic_newton_cotes import generic_newton_cotes


def newton_cotes(p, func, a, b, closed_interval=True):
    '''
        Aproximate <func> using a polynomial of degree <p>
        to integrate [<a>, <b>] if <closed_interval> is true,
        else (<a>, <b>)
    '''
    h = (b - a) / (p + 2*int(not closed_interval))
    x = lambda s: a + h * (s + int(not closed_interval))
    g = lambda s: func(x(s))

    if closed_interval:
        if p == 1:
            return h/2 * (g(0) + g(1))
        elif p == 2:
            return h/3 * (g(0) + 4*g(1) + g(2))
        elif p == 3:
            return 3*h/8 * (g(0) + 3*g(1) + 3*g(2) + g(3))
        elif p == 4:
            return 2*h/45 * (7*g(0) + 32*g(1) + 12*g(2) + 32*g(3) + 7*g(4))
    else:
        if p == 1:
            return 3*h/2 * (g(0) + g(1))
        elif p == 2:
            return 4*h/3 * (2*g(0) - g(1) + 2*g(2))
        elif p == 3:
            return 5*h/24 * (11*g(0) + g(1) + g(2) + 11*g(3))
        elif p == 4:
            return 6*h/20 * (11*g(0) - 14*g(1) + 26*g(2) -14*g(3) + 11*g(4))

    if p > 4:
        formula = generic_newton_cotes(p, a, b, closed_interval)
        symbols = {s: g(int(str(s).split('_')[1])) for s in formula.free_symbols}
        return formula.subs(symbols)


    
if __name__ == '__main__':
    
    prev = 100
    current = 0
    tolerance = 0.000001

    for i in range(1, 10, 1):

        a, b = 0, 1
        prev = current
        current = newton_cotes(i, lambda x: (sin(2*x) + 4*x**2 + 3*x)**2, a, b, True)
        
        print('grau {} aberto = {}'.format(
            i, newton_cotes(i, lambda x: (sin(2*x) + 4*x**2 + 3*x)**2, a, b, True)
        ))
        print('grau {}  fechado  = {}'.format(
            i, newton_cotes(i, lambda x: (sin(2*x) + 4*x**2 + 3*x)**2, a, b, False)
        ))
        print('')
        
        print('erro absoluto: ',abs(prev-current))

        if(abs(prev-current) < tolerance):
            print('tolerancia atingida')
            print('iterações necessárias: ',i)
            break
