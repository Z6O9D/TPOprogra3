

class laberinto:
    class Nodo:
        def __init__(self,x,y,info):
            self.info = info
            self.x = x
            self.y = y
            self.arriba = None
            self.abajo = None
            self.derecha = None
            self.izquierda = None
        def conectar(self,nodo,i,j):
            if self.y == i + 1: 
                self.arriba = nodo
            if self.y + 1 == i:
                self.abajo = nodo
            if self.x + 1 == j:
                self.derecha = nodo
            if self.x == j+1:
                self.izquierda = nodo
            else:
                print("El nodo no es adyacente")
    def __init__(self,matriz):
        self.matriz=matriz
        self.caminos=[]
        self.info = {}
        self.inicio = None
        self.fin = None
    def buscar(self):◘
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                casilla = self.matriz[i][j]
                if casilla == ".":
                    self.info[str(i)+","+str(j)] = self.Nodo(i,j,casilla)
                elif casilla == "#":
                    pass
                elif casilla == ".":
                    self.info[casilla] = self.Nodo(i,j,casilla)
                else:
                    if casilla in self.info["portal"]:
                        self.info["portal"][casilla] = self.Nodo(i,j,casilla)
                    else:
                        self.info["portal"][casilla] = [self.Nodo(i,j,casilla)]

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
    def test_sinportal(self,matriz):
        pass
    def test_gota(self,matriz):
        evaluar=[self.inicio]
        evaluados=[]
        for i in range(len(tablero)):
            for j in range(len(tablero)):
                if tablero[i][j] == 0 and (i>0 or i<len(tablero)) and (j>0 or j<len(tablero)):
                    for k in range(-1,2):
                        for l in range(-1,2):
                            try:
                                if tablero[i+k][j+l] == "." and (i+k > -1 and j+l > -1):
                                    tablero[i+k][j+l] = minefield[i+k][j+l]
                                    band=True
                            except IndexError:
                                pass
            if band:
                cero(tablero,minefield)







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


