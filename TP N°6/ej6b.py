"""
Autor: GAÑAN, Tomas // CERIONI, Enrique 
Ejercicio 6b: Hipotesis (Generar-Eliminar)
"""

# Importacion de librerias/modulos

import numpy as np
import random
import math
import cmath

G = ['?','?','?','?'] # Hipotesis general
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

cont = 0

for datos in D:
    for j in range(4):
        if(datos[True] and S[j] == '0'):
            S[j] = datos[j]
        if(datos[True] and datos[j] != S[j]):
            S[j] = '?'
            print(S)
        if(datos[True] and S == ['?', '?', '?', '?']):
            cont = 1
            break
    if cont == 1:
        break

G = [['sunny', 'overcast', 'rain'], ['hot', 'cool', 'mild'], ['high', 'normal'], ['weak', 'strong']]

for tables in D:
    if not tables[True]:
        for i in range(len(G)):
            for j in G[i]:
                if j == tables[i]:
                    G[i].remove(j)
            print(G)
for j in G:
    if len(j) == 0:
        j.append('?')
        
print("\n |--------------------------|")
print(" |   Hipotesis generales    | ")
print(" |--------------------------|")
print("\n",G)


print("\n |--------------------------|")
print(" |  Hipotesis Especificas   | ")
print(" |--------------------------|")

print("\n",S)