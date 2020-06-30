import numpy as np


def symmetric_matrix(n):
    # returns symmetric matrix of size nxn

    s = np.triu(np.arange(1, n**2+1).reshape(n, n))
    s = s + s.T - np.diag(s.diagonal())

    return s


def householder_on_ith_column(prev_ith_col, i, debug=False):

    n = len(prev_ith_col)
    w = np.zeros(n)
    w_line = np.zeros(n)
    w[i+1:] = prev_ith_col[i+1:]

    w_line[i+1] = np.linalg.norm(w)

    M = w - w_line
    m = (1./np.linalg.norm(M) * M).reshape(-1, 1)

    if debug: print('w = ', w)
    if debug: print('N = ', M)
    if debug: print('n = ', m.T)

    H = np.eye(n) - 2 * np.matmul(m, m.T)

    return H


def householder_method(A, debug=False):
    # Matri A must be symmetric
    n = len(A)
    H = np.eye(n)
    prev_A = A

    for i in range(n-2):
        H_i = householder_on_ith_column(prev_A[:, i], i, debug)
        if debug: print('\nH_{} = '.format(i))
        if debug: print(H_i)
        if debug: print('')
        curr_A = np.matmul(np.matmul(H_i.T, prev_A), H_i)
        prev_A = curr_A
        if debug: print('A_{} = '.format(i))
        if debug: print(str(prev_A))
        if debug: print('')
        H = np.matmul(H, H_i)
        # if debug: print(np.round(H, 4))
        if debug: print(len(str(prev_A).split('\n')[-1]) * '-')

    return prev_A, H


if __name__ == '__main__':

    np.set_printoptions(precision=3, suppress=True, linewidth=120)

    # a = symmetric_matrix(6)
    A = np.array([
        [40, 8, 4, 2, 1],
        [8, 30, 12, 6, 2],
        [4, 12, 20, 1, 2],
        [2, 6, 1, 25, 4],
        [1, 2, 2, 4, 5]
    ])

    A, H = householder_method(A)
    print('A = ')
    print(A)
    print('\nH = ')
    print(H)
