import math

def derivada_tg(alpha):
  return math.tan(alpha)

def limite(x, delta_x):
  lim = (f(x+delta_x) - f(x))/delta_x

def f(x):
  return 3*x*x
  
def foward_derivada_primeira(x, delta_x):
  derivada = (f(x + delta_x) - f(x))/delta_x
  return derivada


def backward_derivada_primeira(x, delta_x):
  derivada = (f(x) - f(x - delta_x))/delta_x
  return derivada


def central_derivada_primeira(x, delta_x):
  derivada = (f(x + delta_x) - f(x - delta_x))/2*delta_x
  return derivada


def foward_derivada_segunda(x, delta_x):
  derivada = (f(x + 2*delta_x) - 2*f(x + delta_x) + f(x))/(delta_x*delta_x)

def backward_derivada_segunda(x, delta_x):
  derivada = (f(x) - 2*f(x - delta_x) + f(x - 2*delta_x))/(delta_x*delta_x)
                                                           
def central_derivada_segunda(x, delta_x):
  derivada = (f(x + 2*delta_x) - 2*f(x) + f(x - 2*delta_x))/4*(delta_x*delta_x)
