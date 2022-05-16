"""
Autor: GAÑAN, Tomas // CERIONI, Enrique 
Ejercicio 2: Programar el caso para un agente reactivo basado en modelo
"""

# Importacion de librerias/modulos

import time

piso = [1,1,0,1] # 1 = sucio / 0 = limpio
backup = [0,0,0,0]

i = 0
direccion = 1

while True:

    if backup[i] == 1:
        print("Ya pase por aca... \n")
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
            i = i + direccion
            print("MOVIMIENTO A: ", i)
            time.sleep(1)


