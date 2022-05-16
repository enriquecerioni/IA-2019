"""
Autor: GAÑAN, Tomas // CERIONI, Enrique 
Ejercicio 3: Torres de Hanoi
"""

# En el siguiente algoritmo se hace uso de la recursividad

def torresHanoi(n, torre1='1', torre2='2', torre3='3'): 
    if n > 0:
        torresHanoi(n-1, torre1,torre3,torre2)
        print('El disco:', n, 'se mueve de la torre:', torre1, 'a la torre:', torre3)
        torresHanoi(n-1, torre2,torre1,torre3)
 
discos = int(input('Por favor, ingrese el numero de discos: '))
torresHanoi(discos)

# n = 1 siempre va a ser el disco mas chico
