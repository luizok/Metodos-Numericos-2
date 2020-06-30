import numpy as np
from metodo_potencia import metodo_potencia
from metodo_potencia_inversa import metodo_inverso
from metodo_potencia_deslocamento import metodo_potencia_deslocamento

A = np.array([[5, 2, 1], [2, 3, 1], [1, 1, 2]])
v0 = np.array([1, 1, 1])
epsilon = 0.000001

resp1 = metodo_potencia(A, v0, epsilon)
resp2 = metodo_inverso(A, v0, epsilon)
resp3 = metodo_potencia_deslocamento(A, 0, v0, epsilon)


print('-----------------------------------------------------------')
print('O formato da saída é: (autovalor, autovetor correspondente)')
print('-----------------------------------------------------------')
print('--------------------MÉTODO DA POTÊNCIA---------------------')
print(resp1)
print('-----------------MÉTODO DA POTÊNCIA INVERSA----------------')
print(resp2)
print('------------MÉTODO DA POTÊNCIA COM DESLOCAMENTO------------')
print(resp3)
