from math import sin, sqrt


def gauss_legendre(p, func, a, b, tol=10e-6):
    '''
        Aproximate <func> using a polynomial of degree <p>
        to integrate [<a>, <b>] until reaches the absolute error < <tol>
    '''
    curr_value = float('inf')
    prev_value = 0
    n = 0

    while(abs(curr_value - prev_value) > tol):
        iters = 0
        total_sum = 0
        dx = (b - a) / 2**n

        for i in range(2**n):
            total_sum += gauss_legendre_partition(p, func,
                            a + i*dx, a + (i + 1)*dx)

        prev_value = curr_value
        curr_value = total_sum

        n += 1

    return n, total_sum

def gauss_legendre_partition(p, func, a, b):
    '''
        Aproximate <func> using a polynomial of degree <p>
        to integrate [<a>, <b>]
    '''
    x = lambda alpha: 1/2.*(a + b - (b - a)*alpha)
    fx = lambda alpha: func(x(alpha))

    if p == 2:
        return (b - a) / 2 * (1*fx(-sqrt(1/3)) + 1*fx(sqrt(1/3)))
    elif p == 3:
        return (b - a) / 2 * (5/9*fx(-sqrt(3/5)) + + 8/9*fx(0) + 5/9*fx(sqrt(3/5)))
    elif p == 4:
        return (b - a) / 2 * (
            0.652145*fx(-sqrt(3/7-2*sqrt(6/5)/7)) +
            0.652145*fx(sqrt(3/7-2*sqrt(6/5)/7)) +
            0.347855*fx(-sqrt(3/7+2*sqrt(6/5)/7)) +
            0.347855*fx(sqrt(3/7+2*sqrt(6/5)/7))
        )


if __name__ == '__main__':

    for i in range(2, 5, 1):
        a, b = 0, 1
        
        print(30 * '-')
        print('POLINOMIO GRAU ' + str(i))
        print('iteracoes = {}, valor aprox. = {}'.format(
            *gauss_legendre(i, lambda x: (sin(2*x) + 4*x**2 + 3*x)**2, a, b)
        ))
        print('')