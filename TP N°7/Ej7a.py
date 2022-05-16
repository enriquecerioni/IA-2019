"""
Autor: GAÑAN, Tomas // CERIONI, Enrique 
Ejercicio 7a: Patrón AND
"""

# Importacion de librerias/modulos

import numpy as np
import random

# Funciones

def printTable(x0,x1,x2,z,w0,w1,w2,s,n,errorE,corrD,w0b,w1b,w2b):

    print("|",x0," | ",x1,"| ",x2," |",z,"| ",w0," |",w1," |",w2," |",s," |   ",n,"  |   ",errorE,"   |   ",corrD," |",w0b,"|",w1b,"|",w2b,"|")
    print("-----------------------------------------------------------------------------------------------------")

# Desarrollo

table = [
        [0,0,0],
        [0,1,0],
        [1,0,0],
        [1,1,1],
        ]

# Pesos de las entradas
w0 = -1
w1 = round(random.uniform(0,1),2)
w2 = round(random.uniform(0,1),2)

r = 0.2 # tasa de aprendizaje
cont = 0
validate = 0

while(validate != 4):
    errors = []
    print("-----------------------------------------------------------------------------------------------------")
    print("|        Entrada    |          Pesos      |     Salida     | Error E | Corr  D |     Nuevos Pesos   |")
    print("| x0 | x1 | x2  | z |   w0  |  w1  |  w2  |   s   |    n   |         |         |  w0  |  w1  |  w2  |")

    for i in range(len(table)):
        for j in range(2):

            # Valores de entrada
            x0 = 1
            x1 = table[i][0]
            x2 = table[i][1]
            z = table[i][2]
            
        s = w0*x0 + w1*x1 + w2*x2
        s = round(s,2) # redondear valor de s

        if(s >= 0):
            n=1
        else:
            n=0
                
        errorE = z - n
        corrD = r*errorE

        # Nuevos pesos de las entradas
        w0b = w0 + x0*corrD
        w1b = w1 + x1*corrD
        w1b = round(w1,2)
        w2b = w2 + x2*corrD    
        w2b = round(w2,2)

        printTable(x0,x1,x2,z,w0,w1,w2,s,n,errorE,corrD,w0b,w1b,w2b)
        errors.append(errorE)

        w0 = w0b
        w1 = w1b
        w2 = w2b

    validate = 0
    for i in range(4):
        if(errors[i] == 0):
            validate += 1