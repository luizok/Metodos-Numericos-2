from math import sin, sqrt, pi


def gauss_hermite(n, func):
    '''
        Aproximate <func> using a polynomial of degree <p>
        to integrate [<a>, <b>]
    '''
    x = []
    w = []
    if n == 2:
        x = [-1/sqrt(2), 1/sqrt(2)]
        w = [0.886226925453, 0.886226925453]
    elif n == 3:
        x = [-sqrt(3/2), 0 , sqrt(3/2)]
        w = [0.295408975151, 1.1816359006, 0.295408975151]
    elif n == 4:
        x = [-sqrt(3/2+sqrt(3/2)), -sqrt(3/2-sqrt(3/2)), sqrt(3/2-sqrt(3/2)), sqrt(3/2+sqrt(3/2))]
        w = [0.0813128354472, 0.804914090006, 0.804914090006, 0.0813128354472]

    return sum(func(x[i]) * w[i] for i in range(n))


if __name__ == '__main__':

    print(60 * '#')
    print('GAUSS-HERMITE \int_{-oo}^{+oo} e^{-x^{2}}f(x)dx, f(x) = 1')
    print('valor esperado: 1.7724538509055')
    for i in range(2, 5, 1):
        print('')
        print('n = ' + str(i))
        print('valor aprox. = {}'.format(gauss_hermite(i, lambda x: 1)))