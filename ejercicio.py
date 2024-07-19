import numpy as np
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))
matriz = []

for i in range(filas):
    fila = []
    for j in range(columnas):
        if i == 0 or i == filas - 1 or j == 0 or j == columnas - 1:
            fila.append(0)
        else:
            fila.append(5) 
    matriz.append(fila)


# Imprimir la matriz resultante
print("Matriz con ceros en los bordes:")
for fila in matriz:
    print(fila)