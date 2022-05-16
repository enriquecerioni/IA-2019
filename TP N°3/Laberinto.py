"""
Autor: GAÑAN, Tomas // CERIONI, Enrique 
Ejercicio 2: Laberinto
"""

# Importacion de librerias/modulos

import numpy as np
import random

# Laberinto

OPEN = []
CLOSE = []

# Distancias entre los nodos

S = ["S","A",6]

A1 = ["A","B",8]
A2 = ["A","DEAD-END",2]

B1 = ["B","G",2]
B2 = ["B","C",1]

C1 = ["C","D",1]
C2 = ["C","DEAD-END",3]

D1 = ["D","F",1]
D2 = ["D","E",2]

E1 = ["E","DEAD-END",1]
E2 = ["E","H",9]

F1 = ["F","DEAD-END",1]
F2 = ["F","G",3]

G1 = ["G","H",1]

H1 = ["H","DEAD-END",2]
H2 = ["H","I",3]

I1 = ["I","FIN",1]
I2 = ["I","DEAD-END",1]
I3 = ["I","DEAD-END",3]

# Inicio del programa

print("\n<< INICIO DEL LABERINTO >>\n")

# --------------------------- PRIMERA OPCION POR S->A1->B2->C1->D1->F2->G1->H2->I1

CLOSE.append(S[1])
OPEN.append(S[2])

#print("Partimos desde el nodo",S[0],"hasta el nodo",S[1],"con una distancia de",S[2],", por lo tanto agregamos:",S[1],"a la lista CLOSE:",CLOSE)
#print("Expandimos el nodo:",S[1])


# Primera elección

if(A1[2] < A2[2] and A1[1] != 'DEAD-END'):
    CLOSE.append(A1[1])
    OPEN.append(A1[2])
elif(A1[2] > A2[2] and A2[1] == 'DEAD-END'):
    CLOSE.append(A1[1])
    OPEN.append(A1[2])
else:
    CLOSE.append(A2[1])
    OPEN.append(A2[2])


# Segunda elección

if(B1[2] > B2[2] and B1[1] != 'DEAD-END'):
    CLOSE.append(B1[1])
    OPEN.append(B1[2])
elif(B1[2] < B2[2] and B2[1] == 'DEAD-END'):
    CLOSE.append(B1[1])
    OPEN.append(B1[2])
else:
    CLOSE.append(B2[1])
    OPEN.append(B2[2])


# Tercera elección

if(C1[2] < C2[2] and C1[1] != 'DEAD-END'):
    CLOSE.append(C1[1])
    OPEN.append(C1[2])
elif(C1[2] > C2[2] and C2[1] == 'DEAD-END'):
    CLOSE.append(C1[1])
    OPEN.append(C1[2])
else:
    CLOSE.append(C2[1])
    OPEN.append(C2[2])


# Cuarta elección

if(D1[2] < D2[2] and D1[1] != 'DEAD-END'):
    CLOSE.append(D1[1])
    OPEN.append(D1[2])
elif(D1[2] > D2[2] and D2[1] == 'DEAD-END'):
    CLOSE.append(D1[1])
    OPEN.append(D1[2])
else:
    CLOSE.append(D2[1])
    OPEN.append(D2[2])


# Quinta elección

if(F1[2] < F2[2] and F1[1] != 'DEAD-END'):
    CLOSE.append(F1[1])
    OPEN.append(F1[2])
elif(F1[2] > F2[2] and F2[1] == 'DEAD-END'):
    CLOSE.append(F1[1])
    OPEN.append(F1[2])
else:
    CLOSE.append(F2[1])
    OPEN.append(F2[2])


# Sexta elección

CLOSE.append(G1[1]) # UNICA OPCIÓN
OPEN.append(G1[2])

# Septima elección

if(H1[2] < H2[2] and H1[1] != 'DEAD-END'):
    CLOSE.append(H1[1])
    OPEN.append(H1[2])
elif(H1[2] > H2[2] and H2[1] == 'DEAD-END'):
    CLOSE.append(H1[1])
    OPEN.append(H1[2])
else:
    CLOSE.append(H2[1])
    OPEN.append(H2[2])


# Octava elección

if(I1[1] == 'FIN'):
    CLOSE.append(I1[1])
    OPEN.append(I1[2])
elif(I2[1] == 'FIN'):
    CLOSE.append(I2[1])
    OPEN.append(I2[2])
else:
     CLOSE.append(I3[1])
     OPEN.append(I3[2])

# --------------------------- SEGUNDA OPCIÓN OPCION POR S->A1->B1->G1->H2->I1 

OPEN2 = []
CLOSE2 = []

CLOSE2.append(S[1])
OPEN2.append(S[2])

# Primera elección

if(A1[2] < A2[2] and A1[1] != 'DEAD-END'):
    CLOSE2.append(A1[1])
    OPEN2.append(A1[2])
elif(A1[2] > A2[2] and A2[1] == 'DEAD-END'):
    CLOSE2.append(A1[1])
    OPEN2.append(A1[2])
else:
    CLOSE2.append(A2[1])
    OPEN2.append(A2[2])


# Segunda elección

if(B1[2] > B2[2] and B1[1] != 'DEAD-END'):
    CLOSE2.append(B1[1])
    OPEN2.append(B1[2])
elif(B1[2] < B2[2] and B2[1] == 'DEAD-END'):
    CLOSE2.append(B2[1])
    OPEN2.append(B2[2])
else:
    CLOSE2.append(B1[1])
    OPEN2.append(B1[2])


# Tercera elección

CLOSE2.append(G1[1]) # UNICA OPCIÓN
OPEN2.append(G1[2])

# Cuarta elección

if(H1[2] < H2[2] and H1[1] != 'DEAD-END'):
    CLOSE2.append(H1[1])
    OPEN2.append(H1[2])
elif(H1[2] > H2[2] and H2[1] == 'DEAD-END'):
    CLOSE2.append(H1[1])
    OPEN2.append(H1[2])
else:
    CLOSE2.append(H2[1])
    OPEN2.append(H2[2])


# Quinta elección

if(I1[1] == 'FIN'):
    CLOSE2.append(I1[1])
    OPEN2.append(I1[2])
elif(I2[1] == 'FIN'):
    CLOSE2.append(I2[1])
    OPEN2.append(I2[2])
else:
     CLOSE2.append(I3[1])
     OPEN2.append(I3[2])


# --------------------------- TERCERA OPCIÓN POR S->A1->B2->C1->D2->E2->H2->I1 

OPEN3 = []
CLOSE3 = []

CLOSE3.append(S[1])
OPEN3.append(S[2])

if(A1[2] < A2[2] and A1[1] != 'DEAD-END'):
    CLOSE3.append(A1[1])
    OPEN3.append(A1[2])
elif(A1[2] > A2[2] and A2[1] == 'DEAD-END'):
    CLOSE3.append(A1[1])
    OPEN3.append(A1[2])
else:
    CLOSE3.append(A2[1])
    OPEN3.append(A2[2])


# Segunda elección

if(B1[2] < B2[2] and B1[1] != 'DEAD-END'):
    CLOSE3.append(B1[1])
    OPEN3.append(B1[2])
elif(B1[2] > B2[2] and B2[1] == 'DEAD-END'):
    CLOSE3.append(B2[1])
    OPEN3.append(B2[2])
else:
    CLOSE3.append(B2[1])
    OPEN3.append(B2[2])


# Tercera elección

if(C1[2] < C2[2] and C1[1] != 'DEAD-END'):
    CLOSE3.append(C1[1])
    OPEN3.append(C1[2])
elif(C1[2] > C2[2] and C2[1] == 'DEAD-END'):
    CLOSE3.append(C1[1])
    OPEN3.append(C1[2])
else:
    CLOSE3.append(C2[1])
    OPEN3.append(C2[2])


# Cuarta elección

if(D1[2] < D2[2] and D2[1] != 'DEAD-END'):
    CLOSE3.append(D2[1])
    OPEN3.append(D2[2])
elif(D1[2] > D2[2] and D1[1] == 'DEAD-END'):
    CLOSE3.append(D1[1])
    OPEN3.append(D1[2])
else:
    CLOSE3.append(D2[1])
    OPEN3.append(D2[2])


# Quinta elección

if(E1[2] < E2[2] and E1[1] != 'DEAD-END'):
    CLOSE3.append(E1[1])
    OPEN3.append(E1[2])
elif(E1[2] > E2[2] and E2[1] == 'DEAD-END'):
    CLOSE3.append(E1[1])
    OPEN3.append(E1[2])
else:
    CLOSE3.append(E2[1])
    OPEN3.append(E2[2])


# Sexta elección

if(H1[2] < H2[2] and H1[1] != 'DEAD-END'):
    CLOSE3.append(H1[1])
    OPEN3.append(H1[2])
elif(H1[2] > H2[2] and H2[1] == 'DEAD-END'):
    CLOSE3.append(H1[1])
    OPEN3.append(H1[2])
else:
    CLOSE3.append(H2[1])
    OPEN3.append(H2[2])


# Septima elección

if(I1[1] == 'FIN'):
    CLOSE3.append(I1[1])
    OPEN3.append(I1[2])
elif(I2[1] == 'FIN'):
    CLOSE3.append(I2[1])
    OPEN3.append(I2[2])
else:
     CLOSE3.append(I3[1])
     OPEN3.append(I3[2])

# --------------------------------------------------------- RESULTADOS

costo1 = 0
costo2 = 0
costo3 = 0

# PRIMER CAMINO
print("el camino tomado por el nodo F es el siguiente: ")
print(CLOSE)
print(OPEN)
print("\n")

for i in range(len(CLOSE)): 
    costo1 = costo1 + OPEN[i]

# SEGUNDO CAMINO
print("el camino tomado por el nodo G es el siguiente: ")
print(CLOSE2)
print(OPEN2)
print("\n")

for i in range(len(CLOSE2)): 
    costo2 = costo2 + OPEN2[i]

# TERCER CAMINO CAMINO
print("el camino tomado por el nodo E es el siguiente: ")
print(CLOSE3)
print(OPEN3)
print("\n")

for i in range(len(CLOSE3)): 
    costo3 = costo3 + OPEN3[i]

# CALCULO DEL COSTO
if(costo1 < costo2 and costo1 < costo3):
    print("El camino de menor costo entre el origen",S[0],"y el destino",I1[0],"es por el nodo F con un costo de:",costo1)
    print("\n")
    for i in range(len(CLOSE)):
        n = len(CLOSE) 
        num = (n-1) - i
        print("",CLOSE[num])
        print(" ^ ")
        print(" | ")
elif(costo2 < costo1 and costo2 < costo3):
    print("El camino de menor costo entre el origen",S[0],"y el destino",I1[0],"es por el nodo G con un costo de:",costo2)
    print("\n")
    for i in range(len(CLOSE2)): 
        n = len(CLOSE2)
        num = (n-1) - i
        print("",CLOSE2[num])
        print(" ^ ")
        print(" | ")
else:
    print("El camino de menor costo entre el origen",S[0],"y el destino",I1[0],"es por el nodo E con un costo de:",costo3)
    print("\n")
    for i in range(len(CLOSE3)):
        n = len(CLOSE3) 
        num = (n-1) - i
        print("",CLOSE3[num])
        print(" ^ ")
        print(" | ")



