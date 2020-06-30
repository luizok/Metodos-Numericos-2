import numpy as np

from householder import householder_method
from metodo_potencia import metodo_potencia
from metodo_potencia_inversa import metodo_inverso


if __name__ == '__main__':

    np.set_printoptions(precision=3, suppress=True, linewidth=120)

    A = np.array([
        [40, 8, 4, 2, 1],
        [8, 30, 12, 6, 2],
        [4, 12, 20, 1, 2],
        [2, 6, 1, 25, 4],
        [1, 2, 2, 4, 5]
    ])
    v = np.ones(A.shape[0])

    print('A = ')
    print(A)

    A_eigval, A_eigvec = metodo_potencia(A, v, 10e-7)
    A_eigval_inv, A_eigvec_inv = metodo_inverso(A, v, 10e-7)
    print('\nA (eigval, eigvec) = ')
    print(A_eigval, A_eigvec)
    print('\nA (eigval, eigvec) inv = ')
    print(A_eigval_inv, A_eigvec_inv)

    # 1, # 2
    A_bar, H = householder_method(A)
    print('\nA_bar =')
    print(A_bar)
    print('\nH = ')
    print(H)

    # 3
    A_bar_eigval, A_bar_eigvec = metodo_potencia(A_bar, v, 10e-7)
    A_bar_eigval_inv, A_bar_eigvec_inv = metodo_inverso(A_bar, v, 10e-7)
    print('\nA_bar (eigval, eigvec) = ')
    print(A_bar_eigval, A_bar_eigvec)
    print('\nA_bar (eigval, eigvec) inv = ')
    print(A_bar_eigval_inv, A_bar_eigvec_inv)

    # 4
    print('\nA_eigvec = H * A_bar_eigvec')
    print(np.matmul(H, A_bar_eigvec))
    print('\nA_eigvec = H * A_bar_eigvec_inv')
    print(np.matmul(H, A_bar_eigvec_inv))
    # 5
    # Os autovalores de A_bar são autovalores de A (?)
