"""
Autor: GAÑAN, Tomas // CERIONI, Enrique 
Ejercicio 3: Programar el caso para un agente reactivo basado en objetivos
"""

# Importacion de librerias/modulos

import time

piso = [1,1,0,1] # 1 = sucio / 0 = limpio
backup = [0,0,0,0]

i = 2
direccion = 1

# Definicion de la funcion movimiento

def mov(i,direccion):
    i = i + direccion
    print("MOVIMIENTO A: ", i)
    return i

while piso != [0,0,0,0]:

    if backup[i] == 1:
        print("Ya pase por aca... \n")
        i = mov(i,direccion)
        time.sleep(1)
    else:

        if piso[i] == 1:
            print("LIMPIANDO... \n")
            piso[i] = 0
            time.sleep(1)
        else:
            if i == 3:
                direccion = -1

            elif i == 0:
                direccion = 1

            backup[i] = 1
            i = mov(i,direccion)
            time.sleep(1)




