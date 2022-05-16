"""
Autor: GAÑAN, Tomas // CERIONI, Enrique 
Ejercicio 1a: 8 Reinas
"""

# Importacion de librerias/modulos

import numpy as np
import random

# Funcion para validar
f = 0
def validMatriz(matriz):
    count = 0
    limite = 7
    for i in range(8):
        aux = 0
        aux2 = 0
        aux3 = 0
        aux4 = 0
        aux5 = 0
        aux6 = 0
        for j in range(8):
            if matriz[i][j] == 1: # Compruebo Filas
                aux += 1

            if matriz[j][i] == 1: # Compruebo Columnas
                aux2 += 1

            if(j <= limite):
                if(matriz[j][j+count] == 1): # Diagonales superiores principales
                    aux3 += 1

                if(matriz[j+count][j] == 1): # Diagonales inferiores principales
                    aux4 += 1

            if(i >= j):
                if(matriz[j][i - j] == 1): # Diagonales superiores secundarias
                    aux5 += 1

            if(i+j <= 7):
                if(matriz[(7-j)][i + j] == 1): # Diagonales inferiores secundarias
                    aux6 += 1

        limite -= 1
        count += 1

        if(aux > 1) or (aux2 > 1) or (aux3 > 1) or (aux4 > 1) or (aux5 > 1) or (aux6 > 1):
            print('Falso')
            return False

    print('Verdadero')
    f = 1
    return True

# El 1 representa a las reinas

while f == 0:

    matriz = np.zeros((8,8))

    for i in range(8):
        num = random.randint(0,7)
        matriz[i][num] = 1

    print(matriz)
    validMatriz(matriz)


