"""
Autor: GAÑAN, Tomas // CERIONI, Enrique 
Ejercicio 6c: Arbol de decisión
"""

# Importacion de librerias/modulos

import numpy as np
import random
import math
import cmath

G = ['?','?','?','?'] # Hipotesis general -> POSITIVO
S = ['0','0','0','0'] # Hipotesis especifica -> NEGATIVO

D = [
    ['sunny','hot','high','weak',False],  # Cambiar por todo lo contrario: rain, cool, mild, normal // overcast, cool, mild, normal
    ['sunny','hot','high','strong',False],
    ['overcast','hot','high','weak',True],
    ['rain','mild','high','weak',True],
    ['rain','cool','normal','weak',True],
    ['rain','cool','normal','strong',False],
    ['overcast','cool','normal','strong',True],
    ['sunny','mild','high','weak',False],
    ['sunny','cool','normal','weak',True],
    ['rain','mild','normal','weak',True],
    ['sunny','mild','normal','strong',True],
    ['overcast','mild','high','strong',True],
    ['overcast','hot','normal','weak',True],
    ['rain','mild','high','strong',False]
    ]

true = 0; false = 0
sunny = 0

# Funciones

def resetVariables():
    global sunnyTrue; global sunnyFalse
    sunnyTrue = 0; sunnyFalse = 0
    global overcast; global overcastTrue; global overcastFalse
    overcast = 0; overcastTrue = 0; overcastFalse = 0
    global rain; global rainTrue; global rainFalse
    rain = 0; rainTrue = 0; rainFalse = 0
    global hot; global hotTrue; global hotFalse
    hot = 0; hotTrue = 0; hotFalse = 0
    global mild; global mildTrue; global mildFalse
    mild = 0; mildTrue = 0; mildFalse = 0
    global cool; global coolTrue; global coolFalse
    cool = 0; coolTrue = 0; coolFalse = 0
    global high; global highTrue; global highFalse
    high = 0; highTrue = 0; highFalse = 0
    global normal; global normalTrue; global normalFalse
    normal = 0; normalTrue = 0; normalFalse = 0
    global weak; global weakTrue; global weakFalse
    weak = 0; weakTrue = 0; weakFalse = 0
    global strong; global strongTrue; global strongFalse
    strong = 0; strongTrue = 0; strongFalse = 0

def calculoEntropia(val0,val1,tot):
    if(val0 != 0 and val1 != 0):
        entropia = -val0/tot * math.log(val0/tot) - val1/tot * math.log(val1/tot)
    else:
        entropia = 0

    return entropia

# Desarrollo

# Contador de True & False

for j in range(14):
    if(D[j][4] == True):
        true = true + 1
    else:
        false = false + 1

# Entropia inicial (Sistema)

totSys = true + false
entIni = calculoEntropia(true,false,totSys)

resetVariables()

# Contador de Sunny

for j in range(14):
    if(D[j][0] == 'sunny'):
        sunny = sunny + 1
    if(D[j][0] == 'sunny' and D[j][4] == True):
        sunnyTrue = sunnyTrue + 1
    elif(D[j][0] == 'sunny' and D[j][4] == False):
        sunnyFalse = sunnyFalse + 1

# Contador de Overcast

for j in range(14):
    if(D[j][0] == 'overcast'):
        overcast = overcast + 1
    if(D[j][0] == 'overcast' and D[j][4] == True):
        overcastTrue = overcastTrue + 1
    elif(D[j][0] == 'overcast' and D[j][4] == False):
        overcastFalse = overcastFalse + 1

# Contador de Rain

for j in range(14):
    if(D[j][0] == 'rain'):
        rain = rain + 1
    if(D[j][0] == 'rain' and D[j][4] == True):
        rainTrue = rainTrue + 1
    elif(D[j][0] == 'rain' and D[j][4] == False):
        rainFalse = rainFalse + 1
  
# Calculo de ganancia Outlook

ganOutlook = entIni - ((sunny/totSys) * calculoEntropia(sunnyTrue,sunnyFalse,totSys) + (overcast/totSys) * calculoEntropia(overcastTrue,overcastFalse,totSys) +(rain/totSys) * calculoEntropia(rainTrue,rainFalse,totSys))

# Contador de Hot

for j in range(14):
    if(D[j][1] == 'hot'):
        hot = hot + 1
    if(D[j][1] == 'hot' and D[j][4] == True):
        hotTrue = hotTrue + 1
    elif(D[j][1] == 'hot' and D[j][4] == False):
        hotFalse = hotFalse + 1

# Contador de Mild

for j in range(14):
    if(D[j][1] == 'mild'):
        mild = mild + 1
    if(D[j][1] == 'mild' and D[j][4] == True):
        mildTrue = mildTrue + 1
    elif(D[j][1] == 'mild' and D[j][4] == False):
        mildFalse = mildFalse + 1

# Contador de Cool

for j in range(14):
    if(D[j][1] == 'cool'):
        cool = cool + 1
    if(D[j][1] == 'cool' and D[j][4] == True):
        coolTrue = coolTrue + 1
    elif(D[j][1] == 'cool' and D[j][4] == False):
        coolFalse = coolFalse + 1
  
# Calculo de ganancia Temperature

ganTemp = entIni - ((hot/totSys) * calculoEntropia(hotTrue,hotFalse,totSys) + (mild/totSys) * calculoEntropia(mildTrue,mildFalse,totSys) + (cool/totSys) * calculoEntropia(coolTrue,coolFalse,totSys))

# Contador de High

for j in range(14):
    if(D[j][2] == 'high'):
        high = high + 1
    if(D[j][2] == 'high' and D[j][4] == True):
        highTrue = highTrue + 1
    elif(D[j][2] == 'high' and D[j][4] == False):
        highFalse = highFalse + 1

# Contador de Normal

for j in range(14):
    if(D[j][2] == 'normal'):
        normal = normal + 1
    if(D[j][2] == 'normal' and D[j][4] == True):
        normalTrue = normalTrue + 1
    elif(D[j][2] == 'normal' and D[j][4] == False):
        normalFalse = normalFalse + 1
  
# Calculo de ganancia Humidity

ganHum = entIni - ((high/totSys) * calculoEntropia(highTrue,highFalse,totSys) + (normal/totSys) * calculoEntropia(normalTrue,normalFalse,totSys))

# Contador de Weak

for j in range(14):
    if(D[j][3] == 'weak'):
        weak = weak + 1
    if(D[j][3] == 'weak' and D[j][4] == True):
        weakTrue = weakTrue + 1
    elif(D[j][3] == 'weak' and D[j][4] == False):
        weakFalse = weakFalse + 1

# Contador de Strong

for j in range(14):
    if(D[j][3] == 'strong'):
        strong = strong + 1
    if(D[j][3] == 'strong' and D[j][4] == True):
        strongTrue = strongTrue + 1
    elif(D[j][3] == 'strong' and D[j][4] == False):
        strongFalse = strongFalse + 1
  
# Calculo de ganancia Wind

ganWind = entIni - ((weak/totSys) * calculoEntropia(weakTrue,weakFalse,totSys) + (strong/totSys) * calculoEntropia(strongTrue,strongFalse,totSys))

# Maximo de ganancia del sistema
print("\nLa ganancia de Outlook es:",ganOutlook,"\nLa ganancia de Temperatura es:",ganTemp,"\nLa ganancia de Humedad es:",ganHum,"\nLa ganancia de Viento es:",ganWind)
maxGan = max(ganOutlook,ganTemp,ganHum,ganWind) # Devuelve el subsistema
print("\nLa mayor ganancia es la de Outlook:",maxGan)
############################

#CALCULAMOS ENTROPIAS DE LA COLUMNA OUTLOOK
entSunny = calculoEntropia(sunnyTrue,sunnyFalse,sunny)
entOver = calculoEntropia(overcastTrue,overcastFalse,overcast)
entRain = calculoEntropia(rainTrue,rainFalse,rain)

#-----------------------------------------------SUNNY-----------------------------------------------------------------#

resetVariables() # resetamos variables a 0

for j in range(14):
    if(D[j][0] == 'sunny'):
        if(D[j][1] == 'hot'):
            hot = hot + 1
        if(D[j][1] == 'hot' and D[j][4] == True):
            hotTrue = hotTrue + 1
        elif(D[j][1] == 'hot' and D[j][4] == False):
            hotFalse = hotFalse + 1

for j in range(14):
    if(D[j][0] == 'sunny'):
        if(D[j][1] == 'mild'):
            mild = mild + 1
        if(D[j][1] == 'mild' and D[j][4] == True):
            mildTrue = mildTrue + 1
        elif(D[j][1] == 'mild' and D[j][4] == False):
            mildFalse = mildFalse + 1

for j in range(14):
    if(D[j][0] == 'sunny'):
        if(D[j][1] == 'cool'):
            cool = cool + 1
        if(D[j][1] == 'cool' and D[j][4] == True):
            coolTrue = coolTrue + 1
        elif(D[j][1] == 'cool' and D[j][4] == False):
            coolFalse = coolFalse + 1
        
ganSunnyTem = entSunny - ((hot/sunny) * calculoEntropia(hotTrue,hotFalse,sunny) + (mild/sunny) * calculoEntropia(mildTrue,mildFalse,sunny) + (cool/sunny) * calculoEntropia(coolTrue,coolFalse,sunny))

#-------------------#

resetVariables() # resetamos variables a 0

for j in range(14):
    if(D[j][0] == 'sunny'):
        if(D[j][2] == 'high'):
            high = high + 1
        if(D[j][2] == 'high' and D[j][4] == True):
            highTrue = highTrue + 1
        elif(D[j][2] == 'high' and D[j][4] == False):
            highFalse = highFalse + 1

for j in range(14):
    if(D[j][0] == 'sunny'):
        if(D[j][2] == 'normal'):
            normal = normal + 1
        if(D[j][2] == 'normal' and D[j][4] == True):
            normalTrue = normalTrue + 1
        elif(D[j][2] == 'normal' and D[j][4] == False):
            normalFalse = normalFalse + 1

ganSunnyHum = entSunny - ((high/sunny) * calculoEntropia(highTrue,highFalse,sunny) + (normal/sunny) * calculoEntropia(normalTrue,normalFalse,sunny))

resetVariables() # resetamos variables a 0

for j in range(14):
    if(D[j][0] == 'sunny'):
        if(D[j][3] == 'weak'):
            weak = weak + 1
        if(D[j][3] == 'weak' and D[j][4] == True):
            weakTrue = weakTrue + 1
        elif(D[j][3] == 'weak' and D[j][4] == False):
            weakFalse = weakFalse + 1

for j in range(14):
    if(D[j][0] == 'sunny'):
        if(D[j][3] == 'strong'):
            strong = strong + 1
        if(D[j][3] == 'strong' and D[j][4] == True):
            strongTrue = strongTrue + 1
        elif(D[j][3] == 'strong' and D[j][4] == False):
            strongFalse = strongFalse + 1


ganSunnyWind = entSunny - ((weak/sunny) * calculoEntropia(weakTrue,weakFalse,sunny) + (strong/sunny) * calculoEntropia(strongTrue,strongFalse,sunny))
print("\n//////////// ---- SUNNY ---- ////////////")
print("\nGanancia de Sunny respecto a Temperatura:",ganSunnyTem,"\nGanancia de Sunny respecto a Humedad:",ganSunnyHum,"\nGanancia de Sunny respecto a Viento:",ganSunnyWind)
maxGanSunny = max(ganSunnyTem,ganSunnyHum,ganSunnyWind)

print("\nLa columna que tiene mayor ganancia es la de Humedad",maxGanSunny)

entSunnyHigh = calculoEntropia(highTrue,highFalse,sunny)
entSunnyNormal = calculoEntropia(normalTrue,normalFalse,sunny)

if(entSunnyHigh == 0 and entSunnyNormal == 0):
    print("La entropía para High en las filas de sunny es:",entSunnyHigh,"\nLa entropía para Normal en las filas de sunny es:",entSunnyNormal,"\nPor lo tanto no hay desorden en los datos.\nEl arbol finaliza la rama.")


#-----------------------------------------------RAIN-----------------------------------------------------------------#

resetVariables() # resetamos variables a 0

for j in range(14):
    if(D[j][0] == 'rain'):
        rain +=1

for j in range(14):
    if(D[j][0] == 'rain'):
        if(D[j][1] == 'hot'):
            hot = hot + 1
        if(D[j][1] == 'hot' and D[j][4] == True):
            hotTrue = hotTrue + 1
        elif(D[j][1] == 'hot' and D[j][4] == False):
            hotFalse = hotFalse + 1

for j in range(14):
    if(D[j][0] == 'rain'):
        if(D[j][1] == 'mild'):
            mild = mild + 1
        if(D[j][1] == 'mild' and D[j][4] == True):
            mildTrue = mildTrue + 1
        elif(D[j][1] == 'mild' and D[j][4] == False):
            mildFalse = mildFalse + 1

for j in range(14):
    if(D[j][0] == 'rain'):
        if(D[j][1] == 'cool'):
            cool = cool + 1
        if(D[j][1] == 'cool' and D[j][4] == True):
            coolTrue = coolTrue + 1
        elif(D[j][1] == 'cool' and D[j][4] == False):
            coolFalse = coolFalse + 1

ganrainTem = entRain - ((hot/rain) * calculoEntropia(hotTrue,hotFalse,rain) + (mild/rain) * calculoEntropia(mildTrue,mildFalse,rain) + (cool/rain) * calculoEntropia(coolTrue,coolFalse,rain))

#-------------------#

resetVariables() # resetamos variables a 0

for j in range(14):
    if(D[j][0] == 'rain'):
        rain +=1

for j in range(14):
    if(D[j][0] == 'rain'):
        if(D[j][2] == 'high'):
            high = high + 1
        if(D[j][2] == 'high' and D[j][4] == True):
            highTrue = highTrue + 1
        elif(D[j][2] == 'high' and D[j][4] == False):
            highFalse = highFalse + 1

for j in range(14):
    if(D[j][0] == 'rain'):
        if(D[j][2] == 'normal'):
            normal = normal + 1
        if(D[j][2] == 'normal' and D[j][4] == True):
            normalTrue = normalTrue + 1
        elif(D[j][2] == 'normal' and D[j][4] == False):
            normalFalse = normalFalse + 1

ganrainHum = entRain - ((high/rain) * calculoEntropia(highTrue,highFalse,rain) + (normal/rain) * calculoEntropia(normalTrue,normalFalse,rain))

resetVariables() # resetamos variables a 0
for j in range(14):
    if(D[j][0] == 'rain'):
        rain +=1

for j in range(14):
    if(D[j][0] == 'rain'):
        if(D[j][3] == 'weak'):
            weak = weak + 1
        if(D[j][3] == 'weak' and D[j][4] == True):
            weakTrue = weakTrue + 1
        elif(D[j][3] == 'weak' and D[j][4] == False):
            weakFalse = weakFalse + 1

for j in range(14):
    if(D[j][0] == 'rain'):
        if(D[j][3] == 'strong'):
            strong = strong + 1
        if(D[j][3] == 'strong' and D[j][4] == True):
            strongTrue = strongTrue + 1
        elif(D[j][3] == 'strong' and D[j][4] == False):
            strongFalse = strongFalse + 1


ganrainWind = entRain - ((weak/rain) * calculoEntropia(weakTrue,weakFalse,rain) + (strong/rain) * calculoEntropia(strongTrue,strongFalse,rain))

print("\n//////////// ---- RAIN ---- ////////////")
print("\nGanancia de rain respecto a Temperatura:",ganrainTem,"\nGanancia de rain respecto a Humedad:",ganrainHum,"\nGanancia de rain respecto a Viento:",ganrainWind)
maxGanrain = max(ganrainTem,ganrainHum,ganrainWind)

print("\nLa columna que tiene mayor ganancia es la de Viento",maxGanrain)

entrainHigh = calculoEntropia(highTrue,highFalse,rain)
entrainNormal = calculoEntropia(normalTrue,normalFalse,rain)

if(entrainHigh == 0 and entrainNormal == 0):
    print("La entropía para High en las filas de rain es:",entrainHigh,"\nLa entropía para Normal en las filas de rain es:",entrainNormal,"\nPor lo tanto no hay desorden en los datos.\nEl arbol finaliza la rama.\n")