"""
Autor: GAÑAN, Tomas // CERIONI, Enrique 
Ejercicio 6a: Hipotesis (Encontrar-E)
"""

# Importacion de librerias/modulos

import numpy as np
import random

S = ['0','0','0','0'] # Hipotesis especifica

D = [
    ['sunny','hot','high','weak',False],
    ['sunny','hot','high','strong',False],
    ['ovecast','hot','high','weak',True],
    ['rain','mild','high','weak',True],
    ['rain','cool','normal','weak',True],
    ['rain','cool','normal','strong',False],
    ['ovecast','cool','normal','strong',True],
    ['sunny','mild','high','weak',False],
    ['sunny','cool','normal','weak',True],
    ['rain','mild','normal','weak',True],
    ['sunny','mild','normal','strong',True],
    ['ovecast','mild','high','strong',True],
    ['ovecast','hot','normal','weak',True],
    ['rain','mild','high','strong',False]
    ]

# Desarrollo

for j in range(13):
    for i in range(4):
        if(D[j][4] == True):
            if(S[i] == '0'):
                S[i] = D[j][i]
            if(D[j][i] != S[i]):
                S[i]='?'
                print(S)