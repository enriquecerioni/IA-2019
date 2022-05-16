"""
Autor: GAÑAN, Tomas // CERIONI, Enrique 
Ejercicio 5: Bicicleta
"""

# Importacion de librerias/modulos

import numpy as np
import random

print("Ingrese velocidad")
vel = int(input())
print("Ingrese distancia")
dis = int(input())

# Funcion distancia

def calculo(x1,x2,x3,x4,y1,y2,y3,y4):
    yp = ((x1*y2 - y1*x2)*(y3 - y4) - (y1 - y2)*(x3*y4 - y3*x4)) / ((x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4))
    #print(yp)
    return yp

# Condiciones de velocidad

if(vel >=0 and vel <=10):
    print("Lento 1 (0-10)")
    x1 = 0
    y1 = 0
    x2 = 10
    y2 = 1

    x3 = vel
    y3 = 0
    x4 = vel
    y4 = 1
    
    mhu = calculo(x1,x2,x3,x4,y1,y2,y3,y4)
    print(mhu)

    velocidad = 0

if(vel >=10 and vel <=20):
    print("Lento 2 (10-20)")
    x1 = 10
    y1 = 1
    x2 = 20
    y2 = 0

    x3 = vel
    y3 = 0
    x4 = vel
    y4 = 1

    mhu = calculo(x1,x2,x3,x4,y1,y2,y3,y4)
    print(mhu)

    velocidad = 1

if(vel >=10 and vel <=30):
    print("Bastante rapido 1 (10-30)")
    x1 = 10
    y1 = 0
    x2 = 30
    y2 = 1

    x3 = vel
    y3 = 0
    x4 = vel
    y4 = 1

    mhu = calculo(x1,x2,x3,x4,y1,y2,y3,y4)
    print(mhu)

    velocidad = 2

if(vel >=30 and vel <=50):
    print("Bastante rapido 2 (30-50)")
    x1 = 30
    y1 = 0
    x2 = 50
    y2 = 1

    x3 = vel
    y3 = 0
    x4 = vel
    y4 = 1

    mhu = calculo(x1,x2,x3,x4,y1,y2,y3,y4)
    print(mhu)

    velocidad = 3

if(vel >=30 and vel <=50):
    print("Bastante rapido 3 (30-50)")
    x1 = 30
    y1 = 1
    x2 = 50
    y2 = 0

    x3 = vel
    y3 = 0
    x4 = vel
    y4 = 1

    mhu = calculo(x1,x2,x3,x4,y1,y2,y3,y4)
    print(mhu)

    velocidad = 4

if(vel >=50):
    print("Rapido (50 o mas)")
    x1 = 50
    y1 = 1
    x2 = 1000
    y2 = 1

    x3 = vel
    y3 = 0
    x4 = vel
    y4 = 1

    mhu = calculo(x1,x2,x3,x4,y1,y2,y3,y4)
    print(mhu)

    velocidad = 5

# Condiciones de distancia

if(dis >=0 and dis <=5):
    print("Muy cerca 1 (0-5)")
    x1 = 0
    y1 = 0
    x2 = 5
    y2 = 1

    x3 = dis
    y3 = 0
    x4 = dis
    y4 = 1

    mhu2 = calculo(x1,x2,x3,x4,y1,y2,y3,y4)
    print(mhu2)

    distancia = 0

if(dis >=5 and dis <=15):
    print("Cerca (5-15)")
    x1 = 5
    y1 = 0
    x2 = 15
    y2 = 1

    x3 = dis
    y3 = 0
    x4 = dis
    y4 = 1

    mhu2 = calculo(x1,x2,x3,x4,y1,y2,y3,y4)
    print(mhu2)

    distancia = 1

if(dis >=15 and dis <=25):
    print("Cerca 2 (15-25)")
    x1 = 15
    y1 = 1
    x2 = 25
    y2 = 0

    x3 = dis
    y3 = 0
    x4 = dis
    y4 = 1

    mhu2 = calculo(x1,x2,x3,x4,y1,y2,y3,y4)
    print(mhu2)

    distancia = 2

if(dis >=20 and dis <=30):
    print("Bastante lejos 1 (20-30)")
    x1 = 20
    y1 = 0
    x2 = 30
    y2 = 1

    x3 = dis
    y3 = 0
    x4 = dis
    y4 = 1

    mhu2 = calculo(x1,x2,x3,x4,y1,y2,y3,y4)
    print(mhu2)

    distancia = 3

if(dis >=30 and dis <=40):
    print("Bastante lejos 2 (30-40)")
    x1 = 30
    y1 = 1
    x2 = 40
    y2 = 1

    x3 = dis
    y3 = 0
    x4 = dis
    y4 = 1

    mhu2 = calculo(x1,x2,x3,x4,y1,y2,y3,y4)
    print(mhu2)

    distancia = 4

if(dis >=35 and dis <=50):
    print("Lejos (35-50)")
    x1 = 35
    y1 = 0
    x2 = 50
    y2 = 1

    x3 = dis
    y3 = 0
    x4 = dis
    y4 = 1

    mhu2 = calculo(x1,x2,x3,x4,y1,y2,y3,y4)
    print(mhu2)

    distancia = 5

if(dis >=50):
    print("Lejos 2 (50 o mas)")
    x1 = 50
    y1 = 1
    x2 = 1000
    y2 = 1

    x3 = vel
    y3 = 0
    x4 = vel
    y4 = 1

    mhu2 = calculo(x1,x2,x3,x4,y1,y2,y3,y4)
    print(mhu2)

    distancia = 6

# CALCULO MÍNIMO

minimo = min(mhu,mhu2)
print("El mínimo es: " , minimo)

# Condiciones de presion

# 0 = Nada //  1 = Poca presion // 2 = Media presion // 3 = Alta presion
table =[[1,3,3],
        [1,3,3],
        [0,2,2],
        [0,1,1]]

#----------poca presion----------#

# Lento 1 = 0 y Muy Cerca = 0 
# Lento 2 = 1 y Muy Cerca = 0

# Lento 1 = 0 y Cerca 1 = 1 
# Lento 1 = 0 y Cerca 2 = 2 
# Lento 2 = 1 y Cerca 1 = 1 
# Lento 2 = 1 y Cerca 2 = 2

# Bastante Rápido 1 = 2 y Lejos 1 = 5
# Bastante Rápido 1 = 2 y Lejos 2 = 6
# Bastante Rápido 2 = 3 y Lejos 1 = 5
# Bastante Rápido 2 = 3 y Lejos 2 = 6
# Bastante Rápido 3 = 4 y Lejos 1 = 5
# Bastante Rápido 3 = 4 y Lejos 2 = 6

# Rápido = 5 y Lejos 1 = 5
# Rápido = 5 y Lejos 2 = 6

#----------media presion----------#

# Bastante Rápido 1 = 2 y Bastante Lejos 1 = 3
# Bastante Rápido 1 = 2 y Bastante Lejos 2 = 4
# Bastante Rápido 2 = 3 y Bastante Lejos 1 = 3
# Bastante Rápido 2 = 3 y Bastante Lejos 2 = 4
# Bastante Rápido 3 = 4 y Bastante Lejos 1 = 3
# Bastante Rápido 3 = 4 y Bastante Lejos 2 = 4

# Rápido = 5 y Bastante Lejos 1 = 3
# Rápido = 5 y Bastante Lejos 2 = 4

#----------alta presion----------#

# Bastante Rápido 1 = 2 y Muy Cerca = 0
# Bastante Rápido 2 = 3 y Muy Cerca = 0
# Bastante Rápido 3 = 4 y Muy Cerca = 0

# Bastante Rápido 1 = 2 y Cerca 1 = 1
# Bastante Rápido 1 = 2 y Cerca 2 = 2
# Bastante Rápido 2 = 3 y Cerca 1 = 1
# Bastante Rápido 2 = 3 y Cerca 2 = 2
# Bastante Rápido 3 = 4 y Cerca 1 = 1
# Bastante Rápido 3 = 4 y Cerca 2 = 2


# Rápido = 5 y Muy Cerca = 0

# Rápido = 5 y Cerca 1 = 1
# Rápido = 5 y Cerca 2 = 2

#-------------------------------------#

if(velocidad == 0 and distancia == 0 or velocidad == 1 and distancia == 0 or velocidad == 0 and distancia == 1 or velocidad == 0 and distancia == 2 or velocidad == 1 and distancia == 1 or velocidad == 1 and distancia == 2 or velocidad == 2 and distancia == 5 or velocidad == 2 and distancia == 6 or velocidad == 3 and distancia == 5 or velocidad == 3 and distancia == 6 or velocidad == 4 and distancia == 5 or velocidad == 4 and distancia == 6 or velocidad == 5 and distancia == 5 or velocidad == 5 and distancia == 6):
    presion = 1
    print("La posicion en la tabla es:" , presion)
    print("\n BAJA PRESIÓN !!")

if(velocidad == 2 and distancia == 3 or velocidad == 2 and distancia == 4 or velocidad == 3 and distancia == 3 or velocidad == 3 and distancia == 4 or velocidad == 4 and distancia == 3 or velocidad == 4 and distancia == 4 or velocidad == 5 and distancia == 3 or velocidad == 5 and distancia == 4):
    presion = 2
    print("La posicion en la tabla es:" , presion)
    print("\n MEDIA PRESIÓN !!")

if(velocidad == 2 and distancia == 0 or velocidad == 3 and distancia == 0 or velocidad == 4 and distancia == 0 or velocidad == 2 and distancia == 1 or velocidad == 2 and distancia == 2 or velocidad == 3 and distancia == 1 or velocidad == 3 and distancia == 2 or velocidad == 4 and distancia == 1 or velocidad == 4 and distancia == 2 or velocidad == 5 and distancia == 0 or velocidad == 5 and distancia == 1 or velocidad == 5 and distancia == 2):
    presion = 3
    print("La posicion en la tabla es:" , presion)
    print("\n ALTA PRESIÓN !!")


# Condiciones de presion

if(presion == 1):
    print("Presion Baja (15-30)")
    
    x1 = 1
    y1 = 15
    x2 = 0
    y2 = 30

    x3 = minimo
    y3 = 0
    x4 = minimo
    y4 = 30

    pf = calculo(x1,x2,x3,x4,y1,y2,y3,y4)
    print("la presion final es: ",pf,"%")

if(presion == 2):
    print("Presion Media (50-80)")

    x1 = 1
    y1 = 50
    x2 = 0
    y2 = 80

    x3 = minimo
    y3 = 0
    x4 = minimo
    y4 = 80

    pf = calculo(x1,x2,x3,x4,y1,y2,y3,y4)
    print("la presion final es: ",pf,"%")

if(presion == 3):
    print("Presion Alta (50-80)")

    x1 = 0
    y1 = 50
    x2 = 1
    y2 = 80

    x3 = minimo
    y3 = 0
    x4 = minimo
    y4 = 100

    pf = calculo(x1,x2,x3,x4,y1,y2,y3,y4)
    print("la presion final es: ",pf,"%")   

