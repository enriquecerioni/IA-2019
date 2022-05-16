"""
Autor: GAÑAN, Tomas // CERIONI, Enrique 
Ejercicio 2: Moneda Falsa
"""

# Importacion de librerias/modulos

import numpy as np
import random

# Eligir una moneda aleatoriamente /  identificar cuál es la falsa

moneda = [0,0,0,0,0,0,0,0,0,0,0,0]
num = random.randint(0,11)
moneda[num]=1

true_coin = [0,0,0]

print("\nLAS 12 MONEDAS = ")
print(moneda)

brazo_der = [moneda[0], moneda[1], moneda[2], moneda[3]]
brazo_izq = [moneda[4], moneda[5], moneda[6], moneda[7]]
mesa = [moneda[8], moneda[9], moneda[10], moneda[11]]

print("\nBRAZO DERECHO = ")
print(brazo_der)

print("\nBRAZO IZQUIERDO =")
print(brazo_izq)

print("\nMESA = ")
print(mesa)

# PRIMER PESADA

if brazo_der == brazo_izq:
    print("\nBALANZA EQUILIBRADA.")
else:
        print("\nLA MONEDA SE ENCUENTRA EN UNO DE LOS BRAZOS.")

brazo_der2 = [moneda[0], moneda[9], moneda[10], moneda[11]]
brazo_izq2 = [moneda[4],moneda[1], moneda[2], moneda[3]]
mesa2 = [moneda[8], moneda[5], moneda[6], moneda[7]]

print("\nBRAZO DERECHO = ")
print(brazo_der)

print("\nBRAZO IZQUIERDO =")
print(brazo_izq)

print("\nMESA = ")
print(mesa)

# SEGUNDA PESADA

if brazo_der2 == brazo_izq2:
    print("\nBALANZA EQUILIBRADA.")
else:
        print("\nLA MONEDA SE ENCUENTRA EN UNO DE LOS BRAZOS.")

# ÚLTIMAS 3 MONEDAS DE CADA GRUPO

brazo_der3 = [moneda[9], moneda[10], moneda[11]]
brazo_izq3 = [moneda[1], moneda[2], moneda[3]]
mesa3 = [moneda[5], moneda[6], moneda[7]]

if brazo_der3 == brazo_izq3 and brazo_der3 == mesa3:
    print("\nLA MONEDA SE ENCUENTRA EN UNA DE LAS 3 QUE NO CAMBIAMOS (INICIALES)")
    # TERCER PESADA
    if moneda[0] == moneda[4]:
        print("LA MONEDA -> 9 ES FALSA")
    elif moneda[0] == 1:
        print("LA MONEDA -> 1 ES FALSA")
    else:
        print("LA MONEDA -> 5 ES FALSA")
else:
    if brazo_der3 == true_coin and brazo_izq3 == true_coin:
        print("\nLA MONEDA SE ENCUENTRA EN EL BRAZO IZQUIERDO.")
        # TERCER PESADA
        if moneda[5] == moneda[6]:
            print("LA MONEDA -> 8 ES FALSA")
        elif moneda[5] == 1:
            print("LA MONEDA -> 6 ES FALSA")
        else:
            print("LA MONEDA -> 7 ES FALSA")
        
    elif brazo_der3 == true_coin and mesa3 == true_coin:
        print("\nLA MONEDA SE ENCUENTRA EN EL BRAZO DERECHO.")
        # TERCER PESADA
        if moneda[1] == moneda[2]:
            print("LA MONEDA -> 4 ES FALSA")
        elif moneda[1] == 1:
            print("LA MONEDA -> 2 ES FALSA")
        else:
            print("LA MONEDA -> 3 ES FALSA")

    else:
        print("\nLA MONEDA SE ENCUENTRA EN EL BRAZO DERECHO.")
        # TERCER PESADA
        if moneda[9] == moneda[10]:
            print("LA MONEDA -> 12 ES FALSA")
        elif moneda[9] == 1:
            print("LA MONEDA -> 10 ES FALSA")
        else:
            print("LA MONEDA -> 11 ES FALSA")