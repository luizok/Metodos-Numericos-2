import numpy as np
import scipy.linalg as splalg

def metodo_inverso(A, x, epsilon):
    
    LUP = splalg.lu_factor(A, overwrite_a = True)
    n = A.shape[0]
    splalg.lu_solve(LUP, x, overwrite_b=True )
    l_old = 0
    lmin = 1./np.linalg.norm(x)
    x = x * lmin
    
    while(abs(lmin-l_old) > epsilon*lmin):
        l_old = lmin
        splalg.lu_solve(LUP, x, overwrite_b=True )
        lmin = 1./np.linalg.norm(x)
        x *= lmin
        
    return lmin, x
