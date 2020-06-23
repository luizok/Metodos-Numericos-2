import numpy as np

def autovalor(A, v):
    Av = A.dot(v)
    return v.dot(Av)

def metodo_potencia(A):
    n, d = A.shape

    auto_vetor = np.ones(d)/np.sqrt(d)

    auto_valor = autovalor(A, auto_vetor)

    while True:
        Av = A.dot(auto_vetor)
        novo_autovetor = Av / np.linalg.norm(Av)

        novo_autovalor = autovalor(A, novo_autovetor)
        if np.abs(auto_valor - novo_autovalor)/novo_autovalor < 0.000001:
            break

        auto_vetor = novo_autovetor
        auto_valor = novo_autovalor

    return novo_autovalor, novo_autovetor