import copy

class Nodo():
    nombre=""
    #padre = Nodo("",,None)
    matriz = []
    #hijo=[]

    def __init__(self, nombre, matriz, padre,fila,end):
        self.nombre=nombre
        self.matriz=matriz
        self.padre=padre
        self.hijo=[]
        self.fila=fila
        self.end=end

    def agregarHijo(self, hijo):
        self.hijo.append(hijo)


    def cambiarAHijo(self,posicion):
        return self.hijo[posicion]

    def volverPadre(self):
        return self.padre

    def borrarHijo(self,hijo):
        self.hijo.remove(hijo)

    def calcularHijos(self, nodoActual, open):
        nMatriz=copy.deepcopy(self.matriz)
        nMatriz=llenarCeldaOcupadas(nMatriz)
        n=0
        for i in range(0,8):
            
            end=0
            if (self.fila==6):
                end=1

            if(nMatriz[self.fila+1][i]==0):
                nMatriz[self.fila+1][i]=1
                if (cantCeldasVaciaProcimaFila(llenarCeldaOcupadas(nMatriz))==0):
                    #print("end")
                    end=1
                nombre= str(self.fila+1) + str(i)
                self.hijo.append(Nodo(nombre,copy.deepcopy(nMatriz),nodoActual,self.fila+1,end))
                open.append(nodoActual.cambiarAHijo(n))
                n = n+1

            nMatriz=copy.deepcopy(self.matriz)
            nMatriz=llenarCeldaOcupadas(nMatriz)

    def __str__(self):
        string= "Nombre: " + self.nombre + " END: " + str(self.end)+" Fila: "+str(self.fila)+" Hijos: "
        for a in self.hijo:
            string += a.nombre+ " "
        print(string)
        mostrarMatriz(self.matriz)
        return ""

def llenarCeldaOcupadas(matriz):# Para llenar en que lugares no se puede colocar reinas
    suma=0
    fil=0
    col=0
    for i in range(8):
        for j in range(8):
            if matriz[i][j] == 1: # Compruebo Filas
                col=j
                fil=i
    
    for i in range(0,8):
        if (i!=fil):
            for j in range(0,8):
                if (j!=col):
                    if(j!=col-i+fil):
                        if (j!=col+i-fil):
                            suma += 1
                        else:
                            matriz[i][j]=2
                    else:
                        matriz[i][j]=2
                else:
                    matriz[i][j]=2
        else:
            for j in range(0,8):
                matriz[i][j]=2     

        matriz[fil][col]=1             

    return matriz

def validMatriz(matriz): # Verifica si la matris es valida
    count = 0
    limite = 7
    for i in range(8):
        aux = 0
        aux2 = 0
        aux3 = 0
        aux4 = 0
        aux5 = 0
        aux6 = 0
        for j in range(8):
            if matriz[i][j] == 1: # Compruebo Filas
                aux += 1

            if matriz[j][i] == 1: # Compruebo Columnas
                aux2 += 1

            if(j <= limite):
                if(matriz[j][j+count] == 1): # Diagonales superiores principales
                    aux3 += 1

                if(matriz[j+count][j] == 1): # Diagonales inferiores principales
                    aux4 += 1

            if(i >= j):
                if(matriz[j][i - j] == 1): # Diagonales superiores secundarias
                    aux5 += 1

            if(i+j <= 7):
                if(matriz[(7-j)][i + j] == 1): # Diagonales inferiores secundarias
                    aux6 += 1

        limite -= 1
        count += 1

        if(aux > 1) or (aux2 > 1) or (aux3 > 1) or (aux4 > 1) or (aux5 > 1) or (aux6 > 1):
            return False

    return True
    
def limpiarMatriz(matriz):
    for i in range(0,8):
        for j in range(0,8):
            matriz[i][j]=0

def mostrarMatriz(matriz): # muestra la matriz de forma ordenada
    string=''
    for i in range(8):
        string= string + '\n'
        for j in range(8):
            string=string + str(matriz[i][j]) + ' '
        
    print(string)

def cantCeldasVaciaProcimaFila(matriz):
    suma=0
    fila=1
    for i in range(0,7):
        for j in range(0,8):
            if (matriz[i][j]==1):
                fila=i+1

    for a in range(0,8):

        if (matriz[fila][a]==0):
            suma +=1
    return suma
    
def mostraListaNodos(list):
    strr=""
    for a in list:
        strr = strr + a.nombre + " "
    print(strr)


def insertarRecursivo(inicial,matriz,padre):
    #print("Incertando Hijo")
    nuevo=Nodo("a",matriz,padre,0,0)
    if (inicial==padre):
        #print("\nInicial==padre")
        inicial.agregarHijo(nuevo)
    else:
        for hijo in inicial.hijo:
            if (hijo==padre):
                #print("\nHijo==padre")
                hijo.agregarHijo(nuevo)
            else:
                #print("recursando")
                insertarRecursivo(hijo,matriz,padre)

def crearRecursivo(nodo,matriz,abierto,cerrado):
    if (nodo.padre):
        print("Creando Hijos")
        nodo.calcularHijos(nodoActual,abierto)
        for hijo in nodo.hijo:
            abierto.append(hijo)
            if(hijo.fila==7):
                if(validMatriz(hijo.matriz)):
                    print("Matriz Valida")
                    print(hijo)
                    print("saliendo")
                    exit()
                break
            crearRecursivo(hijo,hijo.matriz,abierto,cerrado)
            abierto.remove(hijo)
            cerrado.append(hijo)
    else:
        print ("nodo inicial")
        for j in range(0,8):
            matriz[0][j]=1
            insertarRecursivo(nodo,copy.deepcopy(matriz),nodo)
            abierto.append(nodoActual.cambiarAHijo(j))
            limpiarMatriz(matriz)
        for hijo in nodo.hijo:
            print("Creando Hijos")
            crearRecursivo(hijo,hijo.matriz,abierto,cerrado)
            abierto.remove(hijo)
            cerrado.append(hijo)
        
def mostrarRecursivo(nodo):
    for hijo in nodo.hijo:
        print(hijo)
        mostrarRecursivo(hijo)


abierto=[]
cerrado=[]

matriz = []# creo la matriz y defino el tamaño
for i in range(8):
    matriz.append([])
    for j in range(8):
        matriz[i].append(None)

limpiarMatriz(matriz)

inicial = Nodo("inicial",matriz,None,0,0)
abierto.append(inicial)

nodoActual=inicial

crearRecursivo(inicial,matriz,abierto,cerrado)

print("mostarndo arbol")
mostrarRecursivo(inicial)
print("fin")

