"""
Autor: GAÑAN, Tomas // CERIONI, Enrique 
Ejercicio 9a: Tenis (Multimodal)
"""

# Importacion de librerias/modulos

import numpy as np
import random

# Desarrollo

def evaluar(prob1,prob2):
    valueMax = max(prob1,prob2)
    if(valueMax == prob1):
        print("Se clasifica como: SI - El valor máximo es: ",valueMax)
    else:
        print("Se clasifica como: NO")

# Tabla de referencia

ref = [
      ['sunny', 'overcast', 'rain'],
      ['hot', 'cool', 'mild'],
      ['high', 'normal'],
      ['weak', 'strong']
      ]

# Tabla general

D = [
    ['sunny','hot','high','weak',False],
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

# Declaración de variables

yes = 0
no = 0

sunnyYes = 0
sunnyNo = 0
overcastYes = 0
overcastNo = 0
rainYes = 0
rainNo = 0

hotYes = 0
hotNo = 0
mildYes = 0
mildNo = 0
coolYes = 0
coolNo = 0

highYes = 0
highNo = 0
normalYes = 0
normalNo = 0

weakYes = 0
weakNo = 0
strongYes = 0
strongNo = 0

# Calculo Yes/No

for j in range(14):
    if(D[j][4] == True):
        yes += 1
    else:
        no += 1

# Calculo de Outlook    
        
    if(D[j][4] == True and D[j][0] == ref[0][0]):
        sunnyYes += 1
    elif(D[j][4] == False and D[j][0] == ref[0][0]):
        sunnyNo += 1
    elif(D[j][4] == True and D[j][0] == ref[0][1]):
        overcastYes += 1
    elif(D[j][4] == False and D[j][0] == ref[0][1]):
        overcastNo += 1
    elif(D[j][4] == True and D[j][0] == ref[0][2]):
        rainYes += 1
    elif(D[j][4] == False and D[j][0] == ref[0][2]):
        rainNo += 1
        
# Calculo de Temperature

    if(D[j][4] == True and D[j][1] == ref[1][0]):
        hotYes += 1
    elif(D[j][4] == False and D[j][1] == ref[1][0]):
        hotNo += 1
    elif(D[j][4] == True and D[j][1] == ref[1][2]):
        mildYes += 1
    elif(D[j][4] == False and D[j][1] == ref[1][2]):
        mildNo += 1
    elif(D[j][4] == True and D[j][1] == ref[1][1]):
        coolYes += 1
    elif(D[j][4] == False and D[j][1] == ref[1][1]):
        coolNo += 1

# Calculo de Humidity

    if(D[j][4] == True and D[j][2] == ref[2][0]):
        highYes += 1
    elif(D[j][4] == False and D[j][2] == ref[2][0]):
        highNo += 1
    elif(D[j][4] == True and D[j][2] == ref[2][1]):
        normalYes += 1
    elif(D[j][4] == False and D[j][2] == ref[2][1]):
        normalNo += 1

# Calculo de Wind    
    
    if(D[j][4] == True and D[j][3] == ref[3][0]):
        weakYes += 1
    elif(D[j][4] == False and D[j][3] == ref[3][0]):
        weakNo += 1
    elif(D[j][4] == True and D[j][3] == ref[3][1]):
        strongYes += 1
    elif(D[j][4] == False and D[j][3] == ref[3][1]):
        strongNo += 1
        
# Probabilidades generales

probYes = round(yes/len(D),2)
probNo = round(no/len(D),2)

# Probabilidades Outlook

probSunnyYes = round(sunnyYes/yes,2)
probSunnyNo = round(sunnyNo/no,2)

probOvercastYes = round(overcastYes/yes,2)
probOvercastNo = round(overcastNo/no,2)

probRainYes = round(rainYes/yes,2)
probRainNo = round(rainNo/no,2)

# Probabilidades Temperature

probHotYes = round(hotYes/yes,2)
probHotNo = round(hotNo/no,2)

probCoolYes = round(coolYes/yes,2)
probCoolNo = round(coolNo/no,2)

probMildYes = round(mildYes/yes,2)
probMildNo = round(mildNo/no,2)

# Probabilidades Humidity

probHighYes = round(highYes/yes,2)
probHighNo = round(highNo/no,2)

probNormalYes = round(normalYes/yes,2)
probNormalNo = round(normalNo/no,2)

# Probabilidades wind

probWeakYes = round(weakYes/yes,2)
probWeakNo = round(weakNo/no,2)

probStrongYes = round(strongYes/yes,2)
probStrongNo = round(strongNo/no,2)

"""
---> Rain, Mild, Hight, Weak
---> Overcast, Cool, Normal, Strong
---> Sunny, Cool, Normal, Weak
"""

# Probabilidad a posteriori para cada clase

probTotYes1 = probYes * probRainYes * probMildYes * probHighYes * probWeakYes
probTotNo1 = probNo * probRainNo * probMildNo * probHighNo * probWeakNo

probTotYes2 = probYes * probOvercastYes * probCoolYes * probNormalYes * probStrongYes
probTotNo2 = probNo * probOvercastNo * probCoolNo * probNormalNo * probStrongNo

probTotYes3 = probYes * probSunnyYes * probCoolYes * probNormalYes * probWeakYes
probTotNo3 = probNo * probSunnyNo * probCoolNo * probNormalNo * probWeakNo

# Evaluación

evaluar(probTotYes1,probTotNo1)
evaluar(probTotYes2,probTotNo2)
evaluar(probTotYes3,probTotNo3)