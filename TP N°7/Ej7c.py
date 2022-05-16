"""
Autor: GAÑAN, Tomas // CERIONI, Enrique 
Ejercicio 7c: Reconocer ejemplos
"""

# Importacion de librerias/modulos

import numpy as np
import random

# Funciones

def printTable(x0,x1,x2,x3,x4,x5,z,w0,w1,w2,w3,w4,w5,s,n,errorE,corrD,w0b,w1b,w2b,w3b,w4b,w5b):

    print("|",x0," | ",x1,"| ",x2," | ",x3," | ",x4," | ",x5," |",z,"| ",w0," |",w1," |",w2," | ",w3," | ",w4," | ",w5," |",s," |   ",n,"  |   ",errorE,"   |   ",corrD," |",w0b,"|",w1b,"|",w2b," | ",w3b," | ",w4b," | ",w5b,"|")
    print("---------------------------------------------------------------------------------------------------------------------------")

# Desarrollo

table = [
        [4.2,-1,-1,-1,-1,-1],
        [9.7,-1,-1,-1,-1,1],
        [5.4,1,1,1,1,1],
        [5.3,1,1,-1,-1,-1],
        ]

# Pesos de las entradas
w0 = -1
w1 = round(random.uniform(0,1),2)
w2 = round(random.uniform(0,1),2)
w3 = round(random.uniform(0,1),2)
w4 = round(random.uniform(0,1),2)
w5 = round(random.uniform(0,1),2)

r = 0.2 # tasa de aprendizaje
cont = 0
num = []

while(num != [-1,1,1,-1]):
    num = []
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("|               Entrada              |                   Pesos                  |     Salida     | Error E | Corr  D |                  Nuevos Pesos           |")
    print("| x0 | x1 | x2  | x3  | x4 | x5 | z  |   w0  |  w1  |  w2  |  w3  |  w4  |  w5  |   s   |    n   |         |         |  w0  |  w1  |  w2  |  w3  |  w4  |  w5  |")

    for i in range(len(table)):
        for j in range(5):

            # Valores de entrada
            x0 = 1
            x1 = table[i][0]
            x2 = table[i][1]
            x3 = table[i][2]
            x4 = table[i][3]
            x5 = table[i][4]
            z = table[i][5]
            
        s = w0*x0 + w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5
        s = round(s,2) # redondear valor de s

        if(s >= 0):
            n=-1
            num.append(n)
        else:
            n=-1
            num.append(n)
                
        errorE = z - n
        corrD = r*errorE

        # Nuevos pesos de las entradas
        w0b = w0 + x0*corrD
        w1b = w1 + x1*corrD
        w1b = round(w1,2)
        w2b = w2 + x2*corrD    
        w2b = round(w2,2)
        w3b = w3 + x3*corrD    
        w3b = round(w3,2)
        w4b = w4 + x4*corrD    
        w4b = round(w4,2)
        w5b = w5 + x5*corrD    
        w5b = round(w5,2)

        printTable(x0,x1,x2,x3,x4,x5,z,w0,w1,w2,w3,w4,w5,s,n,errorE,corrD,w0b,w1b,w2b,w3b,w4b,w5b)

        w0 = w0b
        w1 = w1b
        w2 = w2b
        w3 = w3b
        w4 = w4b
        w5 = w5b