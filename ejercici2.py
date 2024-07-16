import numpy as np
filas = int(input("ingrese numeros de filas: ")) # número de filas
columnas = int(input("ingrese numeros de columnas: "))   # número de columnas
matriz1 = np.zeros((filas, columnas), dtype=object)
for i in range (matriz1.shape[0]):
    for j in range(matriz1.shape[1]):  
        if(i == 0):
            matriz1[i,j] = 1
        if(j == 0):
            matriz1[i,j] = 1
        if(i == matriz1.shape[0]-1):
            matriz1[i,j]=1
        if(j == matriz1.shape [1]-1):
            matriz1[i,j]=1
print(matriz1)