import numpy as np
import random 
 
filas = int(input("ingrese numeros de filas: ")) # número de filas
columnas = int(input("ingrese numeros de columnas: "))   # número de columnas
matriz_vacia = np.empty((filas, columnas), dtype=object)
for i in range (matriz_vacia.shape[0]):
    for j in range(matriz_vacia.shape[1]):
        matriz_vacia[i,j] = random.randint(0,100)
print(matriz_vacia)
diagonal = np.diag(matriz_vacia)
print(f"la diagonal es: {diagonal}") 
