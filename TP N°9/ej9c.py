"""
Autor: GAÑAN, Tomas // CERIONI, Enrique 
Ejercicio 9c: Sexo (Gaussiano)
"""

# Importacion de librerias/modulos

import numpy as np
import random
import math
import statistics as stats

# Funcion Calculo Gauss

def calculoGauss(med,var,x):
    den = var * math.sqrt(2*math.pi)
    miem = pow(math.e,-0.5*pow((x-med)/var,2))
    gauss = (1/den)*miem
    
    return gauss

# Funcion Evaluacion

def evaluar(prob1,prob2):
    valueMax = max(prob1,prob2)
    if(valueMax == prob1):
        print("Se clasifica como: HOMBRE - El valor máximo es: ",valueMax)
    else:
        print("Se clasifica como: MUJER - El valor máximo es: ",valueMax)

# Desarrollo

D = [
    ['H',6,180,12],
    ['H',5.92,190,11],
    ['H',5.58,170,12],
    ['H',5.92,165,10],
    ['M',5,100,6],
    ['M',5.5,150,8],
    ['M',5.42,130,7],
    ['M',5.75,130,9]
    ]

h = 0
m = 0

for j in range(8):
    if(D[j][0] == 'H'):
        h += 1
    else:
        m += 1
        
# Probabilidades generales

probH = round(h/len(D),2)
probM = round(m/len(D),2)

# Contadores

dataEstH = []
dataEstM = []

dataPesoH = []
dataPesoM = []

dataPiesH = []
dataPiesM = []

for j in range(8):
    if(D[j][0] == 'H'):
        dataEstH.append(D[j][1])
        dataPesoH.append(D[j][2])
        dataPiesH.append(D[j][3])
    else:
        dataEstM.append(D[j][1])
        dataPesoM.append(D[j][2])
        dataPiesM.append(D[j][3])

# Media y varianza para la estatura

medEstH = np.mean(dataEstH)
medEstM = np.mean(dataEstM)
varEstH = np.var(dataEstH)
varEstM = np.var(dataEstM)

# Media y varianza para el peso

medPesoH = np.mean(dataPesoH)
medPesoM = np.mean(dataPesoM)
varPesoH = np.var(dataPesoH)
varPesoM = np.var(dataPesoM)

# Media y varianza para pies

medPiesH = np.mean(dataPiesH)
medPiesM = np.mean(dataPiesM)
varPiesH = np.var(dataPiesH)
varPiesM = np.var(dataPiesM)

"""
---> 5.67, 185, 9
---> 5.45, 190, 8
---> 5.34, 160, 6
"""

# Probabilidad a posteriori para cada clase

# Ejemplo 1

probTotH1 = probH * calculoGauss(medEstH,varEstH,5.67)* calculoGauss(medPesoH,varPesoH,185) * calculoGauss(medPiesH,varPiesH,9)
probTotM1 = probM * calculoGauss(medEstM,varEstM,5.67)* calculoGauss(medPesoM,varPesoM,185) * calculoGauss(medPiesM,varPiesM,9)

# Ejemplo 2

probTotH2 = probH * calculoGauss(medEstH,varEstH,5.45)* calculoGauss(medPesoH,varPesoH,190) * calculoGauss(medPiesH,varPiesH,8)
probTotM2 = probM * calculoGauss(medEstM,varEstM,5.45)* calculoGauss(medPesoM,varPesoM,190) * calculoGauss(medPiesM,varPiesM,8)

# Ejemplo 3

probTotH3 = probH * calculoGauss(medEstH,varEstH,5.34)* calculoGauss(medPesoH,varPesoH,160) * calculoGauss(medPiesH,varPiesH,6)
probTotM3 = probM * calculoGauss(medEstM,varEstM,5.34)* calculoGauss(medPesoM,varPesoM,160) * calculoGauss(medPiesM,varPiesM,6)

evaluar(probTotH1,probTotM1)
evaluar(probTotH2,probTotM2)
evaluar(probTotH3,probTotM3)