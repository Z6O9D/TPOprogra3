def buscar(letra):
    fila=0
    for i in range(len(matriz)):
        if letra in matriz[i]:
            fila=i

    columna=matriz[fila].index(letra)
    return (fila,columna)




class solucion:
    inicio=None
    objetivo=None
    caminos=[]
    class Nodo:
        def __init__(self,x,y):
            self.posicion = (x,y)
            self.arriba = None
            self.abajo = None
            self.derecha = None
            self.izquierda = None
        def conectar(self,nodo,pos):
            if pos == "arriba":
                self.arriba = nodo
            if pos == "abajo":
                self.abajo = nodo
            if pos == "derecha":
                self.derecha = nodo
            if pos == "izquierda":
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


