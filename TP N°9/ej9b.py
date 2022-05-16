"""
Autor: GAÑAN, Tomas // CERIONI, Enrique 
Ejercicio 9b: Flores (Gaussiano)
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

def evaluar(prob1,prob2,prob3):
    valueMax = max(prob1,prob2,prob3)
    if(valueMax == prob1):
        print("Se clasifica como: SETOSA - El valor máximo es: ",valueMax)
    elif(valueMax == prob2):
        print("Se clasifica como: VERSICOLOR - El valor máximo es: ",valueMax)
    else:
        print("Se clasifica como: VIRGINICA - El valor máximo es: ",valueMax)
    
# Desarrollo

fileName = open('iris.txt','r')

data = []

for i in fileName.readlines():          
    lista = i.split(',') 
    flores = []
    for item in lista:
        if not item.startswith('Iris'):
            item = float(item)
        else:
            item = item.rstrip('\n')
        flores.append(item)
    data.append(flores)	

irisSetosa = 0
irisVersi = 0
irisVergi = 0

for j in range(150):
    if(data[j][4] == 'Iris-setosa'):
        irisSetosa += 1
    elif(data[j][4] == 'Iris-versicolor'):
        irisVersi += 1
    else:
        irisVergi += 1
        
# Probabilidades generales

probSetosa = round(irisSetosa/len(data),2)
probVersi = round(irisVersi/len(data),2)
probVergi = round(irisVergi/len(data),2)

# Contadores

longitudCepalSetosa = []
anchoCepalSetosa = []
longitudPetaloSetosa = []
anchoPetaloSetosa = []

longitudCepalVersi = []
anchoCepalVersi = []
longitudPetaloVersi = []
anchoPetaloVersi = []

longitudCepalVergi = []
anchoCepalVergi = []
longitudPetaloVergi = []
anchoPetaloVergi = []

for j in range(150):
    if(data[j][4] == 'Iris-setosa'):
        longitudCepalSetosa.append(data[j][0])
        anchoCepalSetosa.append(data[j][1])
        longitudPetaloSetosa.append(data[j][2])
        anchoPetaloSetosa.append(data[j][3])
    elif(data[j][4] == 'Iris-versicolor'):
        longitudCepalVersi.append(data[j][0])
        anchoCepalVersi.append(data[j][1])
        longitudPetaloVersi.append(data[j][2])
        anchoPetaloVersi.append(data[j][3])
    elif(data[j][4] == 'Iris-virginica'):
        longitudCepalVergi.append(data[j][0])
        anchoCepalVergi.append(data[j][1])
        longitudPetaloVergi.append(data[j][2])
        anchoPetaloVergi.append(data[j][3])
   
# Media y varianza para la Longitud Cepal

medLongCepalSetosa = np.mean(longitudCepalSetosa)
medLongCepalVersi = np.mean(longitudCepalVersi)
medLongCepalVergi = np.mean(longitudCepalVergi)

varLongCepalSetosa = np.var(longitudCepalSetosa)
varLongCepalVersi = np.var(longitudCepalVersi)
varLongCepalVergi = np.var(longitudCepalVergi)

# Media y varianza para la Ancho Cepal

medAnchoCepalSetosa = np.mean(anchoCepalSetosa)
medAnchoCepalVersi = np.mean(anchoCepalVersi)
medAnchoCepalVergi = np.mean(anchoCepalVergi)

varAnchoCepalSetosa = np.var(anchoCepalSetosa)
varAnchoCepalVersi = np.var(anchoCepalVersi)
varAnchoCepalVergi = np.var(anchoCepalVergi)

# Media y varianza para la Longitud Petalo

medLongPetalSetosa = np.mean(longitudPetaloSetosa)
medLongPetalVersi = np.mean(longitudPetaloVersi)
medLongPetalVergi = np.mean(longitudPetaloVergi)

varLongPetalSetosa = np.var(longitudPetaloSetosa)
varLongPetalVersi = np.var(longitudPetaloVersi)
varLongPetalVergi = np.var(longitudPetaloVergi)

# Media y varianza para la Ancho Petalo

medAnchoPetalSetosa = np.mean(anchoPetaloSetosa)
medAnchoPetalVersi = np.mean(anchoPetaloVersi)
medAnchoPetalVergi = np.mean(anchoPetaloVergi)

varAnchoPetalSetosa = np.var(anchoPetaloSetosa)
varAnchoPetalVersi = np.var(anchoPetaloVersi)
varAnchoPetalVergi = np.var(anchoPetaloVergi)

"""
---> 5.3, 4.0, 1.6, 0.3
---> 5.0, 2.1, 4.6, 1.2
---> 6.9, 4.1, 2.6, 1.4
"""

# Probabilidad a posteriori para cada clase

# Ejemplo 1

probTotSetosa1 = probSetosa * calculoGauss(medLongCepalSetosa,varLongCepalSetosa,5.3) * calculoGauss(medAnchoCepalSetosa, varAnchoCepalSetosa,4.0) * calculoGauss(medLongPetalSetosa,varLongPetalSetosa,1.6) * calculoGauss(medAnchoPetalSetosa,varAnchoPetalSetosa,0.3)
probTotVersi1 = probVersi * calculoGauss(medLongCepalVersi,varLongCepalVersi,5.3) * calculoGauss(medAnchoCepalVersi,varAnchoCepalVersi,4.0) * calculoGauss(medLongPetalVersi,varLongPetalVersi,1.6) * calculoGauss(medAnchoPetalVersi,varAnchoPetalVersi,0.3)
probTotVergi1 = probVergi * calculoGauss(medLongCepalVergi,varLongCepalVergi,5.3) * calculoGauss(medAnchoCepalVergi,varAnchoCepalVergi,4.0) * calculoGauss(medLongPetalVergi,varLongPetalVergi,1.6) * calculoGauss(medAnchoPetalVergi, varAnchoPetalVergi,0.3)

# Ejemplo 2

probTotSetosa2 = probSetosa * calculoGauss(medLongCepalSetosa,varLongCepalSetosa,5.0) * calculoGauss(medAnchoCepalSetosa, varAnchoCepalSetosa,2.1) * calculoGauss(medLongPetalSetosa,varLongPetalSetosa,4.6) * calculoGauss(medAnchoPetalSetosa,varAnchoPetalSetosa,1.2)
probTotVersi2 = probVersi * calculoGauss(medLongCepalVersi,varLongCepalVersi,5.0) * calculoGauss(medAnchoCepalVersi,varAnchoCepalVersi,2.1) * calculoGauss(medLongPetalVersi,varLongPetalVersi,4.6) * calculoGauss(medAnchoPetalVersi,varAnchoPetalVersi,1.2)
probTotVergi2 = probVergi * calculoGauss(medLongCepalVergi,varLongCepalVergi,5.0) * calculoGauss(medAnchoCepalVergi,varAnchoCepalVergi,2.1) * calculoGauss(medLongPetalVergi,varLongPetalVergi,4.6) * calculoGauss(medAnchoPetalVergi, varAnchoPetalVergi,1.2)

# Ejemplo 3

probTotSetosa3 = probSetosa * calculoGauss(medLongCepalSetosa,varLongCepalSetosa,6.9) * calculoGauss(medAnchoCepalSetosa, varAnchoCepalSetosa,4.1) * calculoGauss(medLongPetalSetosa,varLongPetalSetosa,2.6) * calculoGauss(medAnchoPetalSetosa,varAnchoPetalSetosa,1.4)
probTotVersi3 = probVersi * calculoGauss(medLongCepalVersi,varLongCepalVersi,6.9) * calculoGauss(medAnchoCepalVersi,varAnchoCepalVersi,4.1) * calculoGauss(medLongPetalVersi,varLongPetalVersi,2.6) * calculoGauss(medAnchoPetalVersi,varAnchoPetalVersi,1.4)
probTotVergi3 = probVergi * calculoGauss(medLongCepalVergi,varLongCepalVergi,6.9) * calculoGauss(medAnchoCepalVergi,varAnchoCepalVergi,4.1) * calculoGauss(medLongPetalVergi,varLongPetalVergi,2.6) * calculoGauss(medAnchoPetalVergi, varAnchoPetalVergi,1.4)

evaluar(probTotSetosa1,probTotVersi1,probTotVergi1)
evaluar(probTotSetosa2,probTotVersi2,probTotVergi2)
evaluar(probTotSetosa3,probTotVersi3,probTotVergi3)