def buscar(letra):
    fila=0
    for i in range(len(matriz)):
        if letra in matriz[i]:
            fila=i

    columna=matriz[fila].index(letra)
    return (fila,columna)




class grafo:
    inicio=None
    objetivo=None
    caminos=[]
    class Nodo:
        def __init__(self,x,y):
            self.x = x
            self.y = y
            self.arriba = None
            self.abajo = None
            self.derecha = None
            self.izquierda = None
        def conectar(self,nodo,i,j):
            if self.y > i: 
                self.arriba = nodo
            if self.y < i:
                self.abajo = nodo
            if self.x < j:
                self.derecha = nodo
            if self.x > j:
                self.izquierda = nodo

    def __init__(self,Nodo):
        self.inicio = Nodo
    
    def arriba(nodo):
        return nodo.arriba
    def abajo(nodo):
        return nodo.abajo
    def derecha(nodo):
        return nodo.derecha
    def izquierda(nodo):
        return nodo.izquierda
    def posibles(self):
        return self.caminos



def arriba(x,y):
    return (x-1,y)
def abajo(x,y):
    return (x+1,y)
def derecha(x,y):
    return (x,y+1)
def izquierda(x,y):
    return (x,y-1)

def llegar(inicio,fin,actual):
    recorrido=[]
    if inicio == fin:
        caminos.append(recorrido)



matriz='''. . . A . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . B . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . C . . . . .
. . . . . . . D . . . . . . E
. . . . . . . . . . . . . . .
. . . . F . . . . . G . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. H . . . . . X . . . . . I .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . J . . . . . K . . . .
. . . . . . . . . . . . . . .
L . . . . . . M . . . . . . .
. . . . . N . . . . . . . . .
. . . . . . . . . . O . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . P . . .'''


