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

def gauss_laguerre(n, func):
    '''
        Aproximate <func> using a polynomial of degree <p>
        to integrate [<a>, <b>]
    '''
    x = []
    w = []
    if n == 2:
        x = [2 - sqrt(2), 2 + sqrt(2)]
        w = [0.25*(2 - sqrt(2)), 0.25*(2 + sqrt(2))]
    elif n == 3:
        x = [0.4157745568, 2.2942803603, 6.2899450829]
        w = [0.7110930099, 0.2785177336, 0.0103892565]
    elif n == 4:
        x = [0.32255, 1.7458, 4.4366, 9.3951]
        w = [0.60318, 0.3574, 0.0389, 0.000539]

    return sum(func(x[i]) * w[i] for i in range(n))


def gauss_chebyshev(n, func):
    '''
        Aproximate <func> using a polynomial of degree <p>
        to integrate [<a>, <b>]
    '''
    x = []
    w = []
    if n == 2:
        x = [-1/sqrt(2), 1/sqrt(2)]
        w = [pi/2, pi/2]
    elif n == 3:
        x = [-sqrt(3)/2, 0 , sqrt(3)/2]
        w = [pi/3, pi/3, pi/3]
    elif n == 4:
        x = [-sqrt(2 - sqrt(2))/2, sqrt(2 - sqrt(2))/2, -sqrt(2 + sqrt(2))/2, sqrt(2 + sqrt(2))/2] 
        w = [pi/4, pi/4, pi/4, pi/4]

    return sum(func(x[i]) * w[i] for i in range(n))

if __name__ == '__main__':

    print(60 * '#')
    print('GAUSS-HERMITE \int_{-oo}^{+oo} e^{-x^{2}}f(x)dx, f(x) = 1')
    print('valor esperado: 1.7724538509055')
    print(60 * '#')
    print('GAUSS-LAGUERRE \int_{0}^{+oo} e^{-x}f(x)dx, f(x) = 1')
    print('valor esperado: 1.0')
    print(60 * '#')
    print('GAUSS-CHEBYSHEV \int_{-1}^{+1} 1/sqrt{1-x^{2}}f(x)dx, f(x) = 1')
    print('valor esperado: pi')
    print(60 * '#')

    for i in range(2, 5, 1):
        print('')
        print('n = ' + str(i))
        print('valor aprox. = {}'.format(gauss_chebyshev(i, lambda x: 1)))
