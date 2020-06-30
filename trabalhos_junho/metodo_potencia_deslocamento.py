import scipy
import numpy as np
import scipy.linalg as splalg

from metodo_potencia_inversa import metodo_inverso

def metodo_potencia_deslocamento(A, u, x, epsilon):
  
    Au = A
    
    for i in range (0,len(A)):
        Au[i][i] = A[i][i] - u
        
        
    inverse = metodo_inverso(Au, x, epsilon) 
    ans1 = inverse[0] + u
    ans2 = inverse[1]

    return ans1, ans2
