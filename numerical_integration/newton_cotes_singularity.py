#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from math import pi, tanh, cosh, sinh, inf, sqrt
import numpy as np

def singularity_newton_cotes_double(function, a, b):
    
    erro = np.Infinity
    r0 = 0
    c = 0
    error = 0.000001
    
    x = lambda s: ((a+b)/2) + ((b-a)/2)*tanh((pi/2)*(sinh(s)))
    dxs = lambda s: ((b-a)/2)*(pi/2)*((cosh(s))/(cosh((pi/2)*sinh(s)))**2)
    new_function = lambda s: function(x(s))*dxs(s)
                                   
    try:
        while(erro > error):

            c += 0.5

            r1 = newton_cotes_partition(3,new_function, -c, c, True)
            erro = abs((r1 - r0)/r1)
            r0 = r1

    except:
        return r0
    
    return r0



# In[1]:


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

singularity_newton_cotes_double(function,-2,0)


# In[100]:


print(pi/2) #o resultado era pra ter sido esse, acho que tem que 
            #mudar o valor de c ou o negócio é o newton-cotes, mas pelo menos tá perto do valor certo

