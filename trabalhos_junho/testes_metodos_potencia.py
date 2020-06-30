import numpy as np
from metodo_potencia import metodo_potencia
from metodo_potencia_inversa import metodo_inverso
from metodo_potencia_deslocamento import metodo_potencia_deslocamento

A1 = np.array([
		[5, 2, 1],
		[2, 3, 1],
		[1, 1, 2]
	])
    
A2 = np.array([
		[-14, 1, -2],
		[1, -1, 1],
		[-2, 1, -11]
	])
    

A3 = np.array([
        [40, 8, 4, 2, 1],
        [8, 30, 12, 6, 2],
        [4, 12, 20, 1, 2],
        [2, 6, 1, 25, 4],
        [1, 2, 2, 4, 5]
    ])

v1 = np.ones(A1.shape[0])
v2 = np.ones(A2.shape[0])
v3 = np.ones(A3.shape[0])

epsilon = 0.000001

A1_1 = metodo_potencia(A1, v1, epsilon)
A1_2 = metodo_inverso(A1, v1, epsilon)
A1_3 = metodo_potencia_deslocamento(A1, 0, v1, epsilon)

A2_1 = metodo_potencia(A2, v2, epsilon)
A2_2 = metodo_inverso(A2, v2, epsilon)
A2_3 = metodo_potencia_deslocamento(A2, 0, v2, epsilon)

A3_1 = metodo_potencia(A3, v3, epsilon)
A3_2 = metodo_inverso(A3, v3, epsilon)
A3_3 = metodo_potencia_deslocamento(A3, 0, v3, epsilon)


print('----------------------------------------------------------------------')
print('O formato da saída é: (autovalor, autovetor correspondente)-----------')
print('----------------------------------------------------------------------')
print('-----------------------MATRIZ A1--------------------------------------')
print('--------------------MÉTODO DA POTÊNCIA--------------------------------')
print(A1_1)
print('-----------------MÉTODO DA POTÊNCIA INVERSA---------------------------')
print(A1_2)
print('------------MÉTODO DA POTÊNCIA COM DESLOCAMENTO-----------------------')
print(A1_3)
print('----------------------------------------------------------------------')
print('-----------------------MATRIZ A2--------------------------------------')
print('--------------------MÉTODO DA POTÊNCIA--------------------------------')
print(A2_1)
print('-----------------MÉTODO DA POTÊNCIA INVERSA---------------------------')
print(A2_2)
print('------------MÉTODO DA POTÊNCIA COM DESLOCAMENTO-----------------------')
print(A2_3)
print('----------------------------------------------------------------------')
print('-----------------------MATRIZ A3--------------------------------------')
print('--------------------MÉTODO DA POTÊNCIA--------------------------------')
print(A3_1)
print('-----------------MÉTODO DA POTÊNCIA INVERSA---------------------------')
print(A3_2)
print('------------MÉTODO DA POTÊNCIA COM DESLOCAMENTO-----------------------')
print(A3_3)
print('----------------------------------------------------------------------')
