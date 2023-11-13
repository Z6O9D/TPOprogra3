def search(pos_inicial,find): #complejidad O(1)
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


class Nodo:
    def __init__(self, letra,pos):
        self.letra = letra
        self.pos = pos
        self.sig = []
        self.sig_peso = {}
        self.sig_camino = {}
        self.cambio = None
    def add_next(self, nodo_siguiente, peso_arista):
        self.sig.append(nodo_siguiente)
        self.sig_peso[nodo_siguiente.letra] = peso_arista
class laberinto:
    def __init__(self,matriz): #complejidad O(rango de la matriz^2)
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
                        self.inicio = Nodo(casilla,[i,j])
                    elif casilla == "S":
                        self.salida = Nodo(casilla,[i,j])
                    elif casilla not in self.portal_list:
                        self.portal_list.append(casilla)
                        pos = [i,j]
                        self.portales[casilla] = []
                        self.portales[casilla].append(Nodo(casilla,[i,j]))
                    else:
                        self.portales[casilla].append(Nodo(casilla,[i,j]))
        for key in self.portales:
            self.portales[key][0].cambio=self.portales[key][1]
            self.portales[key][1].cambio=self.portales[key][0]


    def caminos(self,nodo_fin,nodo_inicio_pos,info,portal,mov, revisar,minimo=999999): #complejidad O(n-m) n=cantidad de casillas de la matriz, m= muros(#)
        if not revisar and minimo<=len(mov.split(" "))-2:
            return
        i=nodo_inicio_pos[0]
        j=nodo_inicio_pos[1]
        info.append([i,j])
        tablero = self.matriz
        mov+=" "+str(i)+","+str(j)
        buscar=search(nodo_inicio_pos,nodo_fin.pos)
        if tablero[i][j] != info:
        
            if i+buscar[0]>=0 and i+buscar[0] < len(tablero) and [i+buscar[0],j] not in info and tablero[i+buscar[0]][j] != "#": #greedy
                self.caminos(nodo_fin,[i+buscar[0],j],info,portal,mov,revisar)
            if j+buscar[1]>=0 and j+buscar[1] < len(tablero) and [i,j+buscar[1]] not in info and tablero[i][j+buscar[1]] != "#": #greedy
                self.caminos(nodo_fin,[i,j+buscar[1]],info,portal,mov,revisar)

            if 0 <= i-1 and [i-1,j] not in info and tablero[i-1][j] != "#":
                revisar = True
                self.caminos(nodo_fin,[i-1,j],info,portal,mov,revisar,minimo)
            if i+1 <len(tablero) and [i+1,j] not in info and tablero[i+1][j] != "#":
                revisar = True
                self.caminos(nodo_fin,[i+1,j],info,portal,mov,revisar,minimo)
            if j+1 <len(tablero) and [i,j+1] not in info and tablero[i][1+j] != "#":
                revisar = True
                self.caminos(nodo_fin,[i,j+1],info,portal,mov,revisar,minimo)
            if 0 <=j-1 and [i,j-1] not in info and tablero[i][1-j] != "#":
                revisar = True
                self.caminos(nodo_fin,[i,j-1],info,portal,mov,revisar,minimo)

        if tablero[i][j]==nodo_fin.letra:
            if nodo_fin.letra not in portal.sig_peso:
                a=mov.split(" ")
                portal.add_next(nodo_fin,len(a)-2)
                minimo=len(a)-2
                portal.sig_camino[nodo_fin.letra] = mov[1:].split(" ")
            else:
                if len(mov[1:].split(" "))<portal.sig_peso[nodo_fin.letra]:
                    a=mov.split(" ")
                    portal.add_next(nodo_fin,len(a)-2)
                    minimo=len(a)-2



    def buscar_conexiones(self): #  complejidad O(2*n+n^2) n=cantidad de nodos
        self.caminos(self.salida,self.inicio.pos,[],self.inicio,"",False)
        for key in self.portales:
            for portal in self.portales[key]:
                self.caminos(portal,self.inicio.pos,[],self.inicio,"",False)

        conti=0
        for i in range(conti,len(self.portal_list)):
            for j in range(i+1,len(self.portal_list)):
                for portal_buscado in self.portales[self.portal_list[j]]:
                    for portal in self.portales[self.portal_list[i]]:
                        self.caminos(portal_buscado,portal.pos,[],portal,"",False)
                    if portal_buscado.letra in portal.sig_peso:
                        portal_buscado.add_next(portal,portal.sig_peso[portal_buscado.letra])
            conti+=1
        for key in self.portal_list:
            for portal in self.portales[key]:
                self.caminos(self.salida,portal.pos,[],portal,"",False)
    def buscar_salida(self):
        if len(self.inicio.sig)>0:
            if "S" in self.inicio.sig_peso:
                minimo=[self.inicio.sig_peso["S"]]
            else:
                minimo=[len(self.matriz)**4]
            cont=0
            for key in self.inicio.sig:
                if key.letra!="S":
                    self.evaluar(key.cambio,"",self.inicio.sig_peso[key.letra]+1,minimo)
            if min(minimo)<len(self.matriz)**3:
                return min(minimo)
            else:
                return -1
        else:
            return -1
    def evaluar(self,nodo,lista,cont,results):
        for key in nodo.sig:
            if key.letra not in lista and key.letra!="S":
                contar=nodo.sig_peso[key.letra]+cont
                lista+=key.letra
                self.evaluar(key.cambio,lista,contar+1,results)
            if key.letra=="S":
                contar=nodo.sig_peso[key.letra]+cont
                results.append(contar)

filas=open("laberinto.txt", "r")
target = []
for linea in filas.readlines(): # complejidad O(n) n=rango de la matriz
    linea = linea.replace("\n","")
    target.append(str(linea).split(" "))
filas.close


test = laberinto(target)

test.buscar_conexiones()



print(test.buscar_salida())