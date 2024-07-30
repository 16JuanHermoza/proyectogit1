import numpy as np
import random
filasa = 2
columnasa= 2
matriz_a = np.empty((filasa, columnasa), dtype=object)
for i in range (matriz_a.shape[0]):
    for j in range(matriz_a.shape[1]):
        matriz_a[i,j] = random.randint(-50,50)
filasb = 2
columnasb= 3
matriz_b = np.empty((filasb, columnasb), dtype=object)
for i in range (matriz_b.shape[0]):
    for j in range(matriz_b.shape[1]):
        matriz_b[i,j] = random.randint(-50,50)

matriz_r = np.zeros((filasa, columnasb), dtype=int)

print(f" A = \n{matriz_a}")
print(f" B = \n{matriz_b}")


if columnasa != filasb:
    print("Las matrices no se pueden multiplicar")
else:
    for i in range(filasa):
        for j in range(columnasb):
            for k in range(columnasa):
                matriz_r[i][j] += matriz_a[i][k] * matriz_b[k][j]
print(f"Resultado = \n{matriz_r}")


