#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from math import pi, tanh, cosh, sinh, sqrt
import numpy as np


def singularity_newton_cotes_single(function, a, b, c):

    
    x = lambda s: ((a+b)/2) + ((b-a)/2)*tanh(s)
    dxs = lambda s: ((b-a)/2)*(1./cosh(s)**2)
    new_function = lambda s: function(x(s))*dxs(s)

    return newton_cotes_partition(3,new_function, -c, c, True)


def singularity_newton_cotes_double(function, a, b, c):
    
    x = lambda s: ((a+b)/2) + ((b-a)/2)*tanh((pi/2)*(sinh(s)))
    dxs = lambda s: ((b-a)/2)*(pi/2)*((cosh(s))/(cosh((pi/2)*sinh(s)))**2)
    new_function = lambda s: function(x(s))*dxs(s)

    return newton_cotes_partition(3,new_function, -c, c, True)     



def newton_cotes_partition(p, func, a, b, closed_interval=True):
    '''
        Aproximate <func> using a polynomial of degree <p>
        to integrate [<a>, <b>] if <closed_interval> is true,
        else (<a>, <b>)
    '''
    h = (b - a) / (p + 2*int(not closed_interval))
    x = lambda k: a + h * (k + int(not closed_interval))
    g = lambda i: func(x(i))

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


# In[146]:


def function(x):
    
    return 1/(sqrt(4-x**2))


test_1 = lambda x: 1/x**(2/3)

print('TEST_1')
print('SIMPLES  = ' + str(singularity_newton_cotes_single(test_1,0,1, 5)))
print('DUPLA    = ' + str(singularity_newton_cotes_double(test_1,0,1, 2)))
print('ESPERADO = ' + str(3))
print('\n')

print('TEST_2')
print('SIMPLES  = ' + str(singularity_newton_cotes_single(function,-2,0, 3.5)))
print('DUPLA    = ' + str(singularity_newton_cotes_double(function,-2,0, 2.66)))
print('ESPERADO = ' + str(pi/2)) #o resultado era pra ter sido esse, acho que tem que
            #mudar o valor de c ou algo do tipo, mas pelo menos tá perto do valor certo

