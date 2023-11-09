def search(pos_inicial,find):
    direccion=[]
    if pos_inicial[0] - find[0]<0:
        direccion.append(1)
    elif pos_inicial[0] - find[0]>0:
        direccion.append(-1)
    else:
        direccion.append(0)
    if pos_inicial[1] - find[1]<0:
        direccion.append(1)
    elif pos_inicial[1] - find[1]>0:
        direccion.append(-1)
    else:
        direccion.append(0)
    return direccion

def mostrar_conexiones(objeto):
    for key in objeto.portales.values():
        print(key[0].sig)


class Nodo:
    def __init__(self, letra,pos, cambio):
        self.letra = letra
        self.pos = pos
        self.sig = []
        self.sig_peso = {}
        self.cambio = cambio
    def add_next(self, nodo_siguiente, peso_arista):
        self.sig.append(nodo_siguiente)
        self.sig_peso[nodo_siguiente.letra] = peso_arista
class laberinto:
    def __init__(self,matriz):
        self.portal_list = []
        self.matriz = matriz
        self.matriz_peso = []
        self.caminos_posibles = {}
        self.portales = {}
        self.inicio = None
        self.salida = None
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                casilla = matriz[i][j]
                if casilla not in [".", "#"]:
                    if casilla == "E":
                        self.inicio = Nodo(casilla,[i,j],None)
                    elif casilla == "S":
                        self.salida = Nodo(casilla,[i,j],None)
                    elif casilla not in self.portal_list:
                        self.portal_list.append(casilla)
                        pos = [i,j]
                        self.portales[casilla] = []
                        cambiar=self.buscar_cambio(casilla, pos)
                        self.portales[casilla].append(Nodo(casilla,[i,j],cambiar))
                    else:
                        cambiar=self.buscar_cambio(casilla, pos)
                        self.portales[casilla].append(Nodo(casilla,[i,j],cambiar))

    def buscar_cambio(self,letra,pos):
        for i in range(len(self.matriz)):
            if letra in self.matriz[i]:
                if i!=pos[0] and self.matriz[i].index(letra)!=pos[1]:
                    return (i,self.matriz[i].index(letra))
        return False


    def caminos(self,nodo_fin,nodo_inicio,info,mov): #caminos mas cortos de una posicion X a la posicion Y
        i=nodo_inicio.pos
        j=nodo_inicio.pos
        info[i].append([i,j])
        tablero = self.matriz
        mov+=" "+str(i)+","+str(j)
        buscar=search(nodo_inicio,nodo_fin)

        if tablero[i][j] != info[0] and (i>0 or i<len(tablero)) and (j>0 or j<len(tablero)) and tablero[i][j] != "#":
        
            if buscar[0]!=0 and i+buscar[0] < len(tablero) and [i+buscar[0],j] not in info[1]:
                self.caminos(nodo_fin,[i+buscar[0],j],info,mov)
            if buscar[1]!=0 and j+buscar[1] < len(tablero) and [i,j+buscar[1]] not in info[1]:
                self.caminos(nodo_fin,[i,j+buscar[1]],info,mov)

        if tablero[i][j]==info[0] and (info[0] not in info[-1].sig or len(mov.split(" ")-1)<info[-1].sig_peso[info[0]]):
            a=mov.split(" ")
            print("entro")
            info[-1].add_next(info[0],len(a)-1)

    def caminos_cortos(self,pos):
        visitar = []
        for key in self.portales:
            a = self.portales[key][0].pos[0]-pos[0]
            b = self.portales[key][0].pos[1]-pos[1]
            c = (a**2)**0.5+(b**2)**0.5
            a = self.portales[key][1].pos[0]-pos[0]
            b = self.portales[key][1].pos[1]-pos[1]
            d = (a**2)**0.5+(b**2)**0.5
            if c<d:
                visitar.append(self.portales[key][0])
            else:
                visitar.append(self.portales[key][1])
        return visitar

    def buscar_conexiones(self):
        for portal in self.portal_list:
            self.caminos(self.portales[portal][0],self.inicio,["S",[],test.inicio],"")
            self.caminos(self.portales[portal][1],self.inicio,["S",[],test.inicio],"")
        for key in self.portal_list:
            for portal in self.portal_list[key]:
                for portal_buscado in self.portal_list:
                    if key!=portal_buscado and (self.portales[portal][0] not in portal.sig or self.portales[portal][1] not in portal.sig):
                        self.caminos(portal_buscado[0],portal,["S",[],test.inicio],"")
                        self.caminos(portal_buscado[1],portal,["S",[],test.inicio],"")
        for portal in self.portal_list:
            self.caminos(self.salida, self.portales[portal][0],["S",[],test.inicio],"")
            self.caminos(self.salida, self.portales[portal][1],["S",[],test.inicio],"")

    def buscar_salida(self):
        pass



filas=open("laberinto.txt", "r")
target = []
for linea in filas.readlines():
    linea = linea.replace(".\n",".")
    target.append(str(linea).split(" "))
filas.close


test = laberinto(target)
test.buscar_conexiones

print(test.inicio.sig)
print(test.inicio.sig_peso)
print(test.portales["a"][0].sig)
