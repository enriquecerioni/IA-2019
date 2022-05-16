"""
Autor: GAÑAN, Tomas // CERIONI, Enrique 
Ejercicio 1: Programar el caso para un agente reactivo simple
"""

# Importacion de librerias/modulos

import time

piso = [1,1,0,1] # 1 = sucio / 0 = limpio
i = 0
direccion = 1

while True:

    if piso[i] == 1:
        print("LIMPIANDO... \n")
        piso[i] = 0
        time.sleep(1)
    else:
        if i == 3:
            direccion = -1

        elif i == 0:
            direccion = 1

        i = i + direccion
        print("MOVIMIENTO A: ", i)
        time.sleep(1)

