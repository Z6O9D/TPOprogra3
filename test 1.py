def buscar(letra):
    fila=0
    for i in range(len(matriz)):
        if letra in matriz[i]:
            fila=i

    columna=matriz[fila].index(letra)
    return (fila,columna)




class laberinto:
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
    def __init__(self,inicio):
        start = buscar(inicio)
        self.visitados = []
        self.inicio = self.Nodo(start[0],start[1])
        self.addvisitado(start)
        self.caminos=[]

    def addvisitado(self,tuple):
        self.visitados.append(tuple)
    def addcamino(self,tuple):
        self.visitados.append(tuple)
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
    def test(self,objetivo,matriz):
        pass



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


