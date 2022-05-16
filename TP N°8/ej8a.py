"""
Autor: GAÑAN, Tomas // CERIONI, Enrique 
Ejercicio 8a: Cartas
"""

# Importacion de librerias/modulos

import numpy as np
import random

# Funcion Ruleta

def ruleta(poblacion, probabilidad, num):

    seleccionados = []
    
    while(len(seleccionados) < num):
        r = random.random()*0.1

        for (i,individuo) in enumerate(poblacion):            
            if (r <= probabilidad[i]):
                seleccionados.append(list(individuo))
                break
            
    # print("Seleccionados: ", seleccionados)
    return seleccionados

# Funcion Adaptación

def adaptacion(p1,p2):

    fun_adap = round((p1/36) + (p2/360),2)
    if(fun_adap >= 1.5 and fun_adap <= 2.5):
        valor = 6
    elif(fun_adap < 1.5 and fun_adap >= 0.5):
        valor = 5
    elif(fun_adap < 0.5):
        valor = 4
    elif(fun_adap > 2.5 and fun_adap <= 3.5):
        valor = 4
    elif(fun_adap > 3.5 and fun_adap <= 4.5):
        valor = 3
    elif(fun_adap > 4.5 and fun_adap <= 5.5):
        valor = 2
    else:
        valor = 1
    return valor

# Función Cruza

def cruzaUniforme(padre1,padre2):
    
    hijo1 = []
    hijo2 = []
    
    ran = random.randint(0,1)
    
    for i in range(10):
        if(ran == 1):
            hijo1.append(padre1[i])
            hijo2.append(padre2[i])
        else:
            hijo1.append(padre2[i])
            hijo2.append(padre1[i])
    
    for i in range(5):
        newPoblacion.append(hijo1)
        newPoblacion.append(hijo2)
        
    return newPoblacion

def mutacionPermu(pob):
    
    ra1 = random.randint(0,9)
    ra2 = random.randint(0,9)
    
    while(ra1 == ra2):
        ra2 = random.randint(0,9)
    
    for i in range(50):

        a = pob[i][ra2]
        b = pob[i][ra1]

        pob[i][ra1] = a
        pob[i][ra2] = b
        
        mutacionPob.append(pob[i])
    
    return mutacionPob

# Desarrollo

cont = 0
nPoblacion = 100
resultado = 0
total_cercanos = 0
j = 0

probabilidad = []
individuo = []
poblacion = []
cercanos = []

while(cont < 10):

    for k in range(nPoblacion):
        individuo = []
        i = 0
        p1 = 0
        p2 = 0
        randomValue = [1,2,3,4,5,6,7,8,9,10]
        pila1 = []
        pila2 = []

        while(i <= 9):
            
            r = random.randint(0,9-i)
            pila1.append(randomValue[r])
            randomValue.remove(randomValue[r])
            
            i += 1
            
            r = random.randint(0,9-i)
            pila2.append(randomValue[r])
            randomValue.remove(randomValue[r])

            i += 1

        # print("P1 =",pila1,"| P2 =",pila2)

        # Almacenamos los individuos en una pila temporal
        for j in range(len(pila1)):
            p1 = pila1[j] + p1
            individuo.append(pila1[j])

        for j in range(len(pila2)):
            if(j == 0):
                p2 = pila2[j]
                individuo.append(pila2[j])
            else:
                p2 = pila2[j]*p2
                individuo.append(pila2[j])
        
        # print("suma P1 =",p1,"| mult P2 =",p2)

        valor = adaptacion(p1,p2)
        cercanos.append(valor)
        total_cercanos = total_cercanos + valor

        # Almacenamos los individuos (10 valores) en una lista poblacion
        poblacion.append(individuo)
    
    for i in range(nPoblacion):

        prob = cercanos[i]/total_cercanos
        probabilidad.append(prob)

    num = 20
    selec = ruleta(poblacion,probabilidad,num)

    # Cruza

    newPoblacion = []

    for i in range(10):

        randomPadre1 = random.randint(0,len(selec)-1) 
        randomPadre2 = random.randint(0,len(selec)-1) 

        while(randomPadre1 == randomPadre2):
            randomPadre2 = random.randint(0,len(selec)-1) 
        
        cruzaUniforme(selec[randomPadre1],selec[randomPadre2]) # Ejecuto la cruza 
        
        if(randomPadre1 >= randomPadre2):
            selec.remove(selec[randomPadre1])
            selec.remove(selec[randomPadre2])
        else:
            selec.remove(selec[randomPadre2])
            selec.remove(selec[randomPadre1])

    # Mutacion

    mutacionPob = []
    mutacionPermu(newPoblacion)

    print("Iteración N°",cont+1,":",total_cercanos)
    cont+=1

