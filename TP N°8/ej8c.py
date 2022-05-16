"""
Autor: GAÑAN, Tomas // CERIONI, Enrique 
Ejercicio 8a: Cartas
"""

# Importacion de librerias/modulos

import numpy as np
import random

# Funcion adaptación

def adaptacion(sum_valor,sum_peso,table):

    peso_mochila = (sum_peso/8) + sum_valor
    return peso_mochila

# Funcion Ruleta

def ruleta(poblacion, probabilidad, num):

    seleccionados = []
    
    while(len(seleccionados) < num):
        r = random.random()*0.1

        for (i,individuo) in enumerate(poblacion):            
            if (r <= probabilidad[i]):
                seleccionados.append(list(individuo))
                break
            
    return seleccionados

def cruzaUniforme(padre1,padre2):
    
    hijo1 = []
    hijo2 = []
    
    ran = random.randint(0,1)
    
    for i in range(2):
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
    
    ra1 = random.randint(0,1)
    ra2 = random.randint(0,1)
    
    while(ra1 == ra2):
        ra2 = random.randint(0,1)
    
    for i in range(50):

        a = pob[i][ra2]
        b = pob[i][ra1]

        pob[i][ra1] = a
        pob[i][ra2] = b
        
        mutacionPob.append(pob[i])
    
    return mutacionPob

# Desarrollo

table = [
        [1,15,1],
        [2,10,5],
        [3,9,3],
        [4,5,4],
        [5,2,1],
        [6,4,4],
        [7,5,5],
        ]

i = 0
nPoblacion = 100
total_ganancias = 0

individuo = []
poblacion = []
ganancias = []
probabilidad = []

for i in range(nPoblacion):

    sum_peso = 10

    while(sum_peso > 8):

        i = 0
        obj_sel = []
        individuo = []
        objetos = [1,2,3,4,5,6,7]

        while(i < 3):

            r = random.randint(0,6-i)
            obj_sel.append(objetos[r])
            objetos.remove(objetos[r])
            i += 1

        a = obj_sel[0]-1 # objeto 1
        b = obj_sel[1]-1 # objeto 2
        c = obj_sel[2]-1 # objeto 3

        individuo.append(b)
        individuo.append(c)

        # print("ingresaron los objetos a:",table[a][0],"b:",table[b][0],"y c:",table[c][0])

        sum_valor = table[a][1] + table[b][1] + table[c][1]
        sum_peso = table[a][2] + table[b][2] + table[c][2]

    gan_mochila = adaptacion(sum_valor,sum_peso,table)
    ganancias.append(gan_mochila)
    total_ganancias = total_ganancias + gan_mochila

    poblacion.append(individuo)

for i in range(nPoblacion):

    prob = ganancias[i]/total_ganancias
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


