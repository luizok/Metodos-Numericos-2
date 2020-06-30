import numpy as np

def autovalor(A, v):
    Av = A.dot(v)
    return v.dot(Av)

def metodo_potencia(A, v, epsilon):
    n, d = A.shape


    ev = autovalor(A, v)
    # print(v)

    while True:
        Av = A.dot(v)
        v_new = Av / np.linalg.norm(Av)

        ev_new = autovalor(A, v_new)
        if np.abs(ev - ev_new) < epsilon:
            break

        v = v_new
        ev = ev_new

    return ev_new, v_new
