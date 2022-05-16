"""
Autor: GAÑAN, Tomas // CERIONI, Enrique 
Ejercicio 8b: Aeronave
"""

# Importacion de librerias/modulos

import numpy as np
import random
import math

# Funcion

def ruleta(poblacion, probabilidad, num):

    seleccionados = []
    
    while(len(seleccionados) < num):
        r = random.random()*0.1
        
        for (i,individuo) in enumerate(poblacion):            
            if (r <= probabilidad[i]):
                seleccionados.append(list(individuo))
                break
            
    #print("Seleccionados: ", seleccionados)
    return seleccionados

def cruzaUniforme(padre1,padre2):
    
    hijo1 = []
    hijo2 = []
    
    ran = random.randint(0,1)
    
    for i in range(4):
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
    
    ra1 = random.randint(0,3)
    ra2 = random.randint(0,3)
    
    while(ra1 == ra2):
        ra2 = random.randint(0,3)
    
    for i in range(50):
        a = pob[i][ra2]
        b = pob[i][ra1]

        pob[i][ra1] = a
        pob[i][ra2] = b
        
        mutacionPob.append(pob[i])
    
    return mutacionPob
        
# Desarrollo

nPoblacion = 100
elv = 0
i = 0
cont = 0

poblacion = []
elevaciones = []
probabilidad = []

while(cont < 10):

    for i in range(nPoblacion):

        individuo = []
        
        individuo.append(random.randint(0,63))
        individuo.append(random.randint(0,63))
        individuo.append(random.randint(0,63))
        individuo.append(random.randint(0,63))
        
        poblacion.append(individuo)
        
        elevacion = math.pow((individuo[0]-individuo[1]),2) + math.pow((individuo[2]-individuo[3]),2) - math.pow((individuo[0]-30),3) - math.pow((individuo[2]-40),3)
        elevaciones.append(elevacion)
        elv = elv + elevacion

    for i in range(nPoblacion):

        prob = elevaciones[i]/elv

        probabilidad.append(prob)
            
    num = 20
    selec = ruleta(poblacion,probabilidad,num)
    hijosA = []
    hijosB = []
    newPoblacion = []

    # Cruza

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
    
    print("Iteración N°",cont+1,":",elv)

    cont+=1