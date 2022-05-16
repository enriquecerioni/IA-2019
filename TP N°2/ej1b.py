"""
Autor: GAÑAN, Tomas // CERIONI, Enrique 
Ejercicio 1b: 8 Reinas
"""

# Importacion de librerias/modulos

import numpy as np
import random

# El 1 representa a las reinas


matriz = np.zeros((8,8))

for i in range(8):
    
    #primera pasada
    num = random.randint(0,7)
    matriz[i][num] = 1
    print(matriz)
    print("-> Matriz <-\n",i+1)

    #a partir de la segunda pasada

    for i in range(8):
        for j in range(8):
            if matriz[i][j] == 1: # Compruebo Filas
                col=j
                fil=i

        for i in range(0,8):
            suma=0
            if (i!=fil):
                for j in range(0,8):
                    if (j!=col):
                        if(j!=col-i+fil):
                            if (j!=col+i-fil):
                                suma += 1
                                pass
                            elif matriz[i][j] != 1:
                                matriz[i][j]=2
                        elif matriz[i][j] != 1:
                            matriz[i][j]=2
                    elif matriz[i][j] != 1:
                        matriz[i][j]=2
            elif matriz[i][j] != 1:
                for j in range(0,8):
                    matriz[i][j]=2     

            matriz[fil][col]=1

    suma=0
    for i in range(0,8):
        for j in range(0,8):
            if (matriz[i][j]==0):
                suma +=1 #almacena cantidad de celdas vacias.

    print("CANTIDAD DE CELDAS VACIAS: ",suma)
    print("\n")