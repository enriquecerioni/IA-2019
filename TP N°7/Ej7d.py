"""
Autor: GAÑAN, Tomas // CERIONI, Enrique 
Ejercicio 7d: Backpropagation
"""

# Importacion de librerias/modulos

import numpy as np
import random
from math import exp

# Desarrollo

ej = []

fileName = open('seeds_dataset.txt','r')

for i in fileName.readlines():          
	lista = i.split() 
	semilla = []
	for item in lista:
		item = float(item)
		semilla.append(item)
	ej.append(semilla)	

# 1) Inicializar 

def iniciarRed(nEntradas, nOculta, nSalidas):
	red = list()
	capaOculta = [{'pesos':[random() for i in range(nEntradas + 1)]} for i in range(capaOculta)]
	red.append(capaOculta)
	capaSalida = [{'pesos':[random() for i in range(nOculta + 1)]} for i in range(nSalidas)]
	red.append(capaSalida)
	return red
 
# Activar
def activar(pesos, entradas):
	activacion = pesos[-1]
	for i in range(len(pesos)-1):
		activacion += pesos[i] * entradas[i]
	return activacion
# Transferir
def transferir(activacion):
	return 1.0 / (1.0 + exp(-activacion))

# 2) Propagacion hacia adelante

def propagacionAdelante(red, fila):
	salidas = fila
	for capa in red:
		nuevasEntradas = []
		for neurona in capa:
			activacion = activar(neurona['pesos'], salidas)
			neurona['salidas'] = transferir(activacion)
			nuevasEntradas.append(neurona['salidas'])
		salidas = nuevasEntradas
	return salidas

# 3) Propagacion hacia atras

def propagacionAtras(red, valorEsperado):
	for i in reversed(range(len(red))):
		capa = red[i]
		errores = list()
		if i != len(red)-1:
			for j in range(len(capa)):
				error = 0.0
				for neurona in red[i + 1]:
					error += (neurona['pesos'][j] * neurona['delta'])
				errores.append(error)
		else:
			for j in range(len(capa)):
				neurona = capa[j]
				errores.append(valorEsperado[j] - neurona['salidas'])
		for j in range(len(capa)):
			neurona = capa[j]
			neurona['delta'] = errores[j]

# 4) Actualizar pesos

def actualizarPesos(red,fila,tipo):
    for i in range(len(red)):
        salidas = fila[:-1]
        if(i != 0):
            salidas = [neurona['salidas'] for neurona in red[i-1]]
        for neurona in red[i]:
            for j in range(len(salidas)):
                neurona['pesos'][j] += tipo * neurona['delta'] * salidas[j]
            neurona['pesos'][-1] += tipo * neurona['delta']

# 5) Entrenamiento

def entrenamientoRed(red,entrenar,tipo,nFecha,nSalidas):
    for fecha in range(nFecha):
        sumaError = 0
        for fila in entrenar:
            salidas = propagacionAdelante(red,fila)
            valorEsperado = [0 for i in range(nSalidas)]
            valorEsperado[fila[-1]] = 1
            sumaError += sum[(valorEsperado[i] - salidas[i]) ** 2 for i in range(len(valorEsperado))]
            propagacionAtras(red,valorEsperado)
            actualizarPesos(red,fila,tipo)
        print("nFecha: ",fecha,"Tipo: ",tipo,"Suma error: ",sumaError)

# 6) Predicción

def predecir(red, fila):
    salidas = propagacionAdelante(red,fila)
    return salidas.index(max(salidas))