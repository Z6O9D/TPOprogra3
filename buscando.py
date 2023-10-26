

def direccion(pos,find):
    direccion=[]
    if pos[0] - find[0]<0:
        direccion.append(1)
    elif pos[0] - find[0]>0:
        direccion.append(-1)
    else:
        direccion.append(0)
    if pos[1] - find[1]<0:
        direccion.append(1)
    elif pos[1] - find[1]>0:
        direccion.append(-1)
    else:
        direccion.append(0)
    return direccion
def caminos(tablero,adress,index,cont,mov,letra):
    i=index[0]
    j=index[1]
    cont+=1
    mov+=","+str(index[0])+"/"+str(index[1])
    buscar=direccion(index,adress)

    if tablero[index[0]][index[1]] != letra and (i>0 or i<len(tablero)) and (j>0 or j<len(tablero)) and cont<10 and tablero[index[0]][index[1]] != "#":
        print(mov,"tablero",i,j,tablero[i][j],letra)
        if buscar[0]!=0:
            caminos(tablero,adress,[index[0]+buscar[0],index[1]],cont,mov,letra)
        if buscar[1]!=0:
            caminos(tablero,adress,[index[0],index[1]+buscar[1]],cont,mov,letra)

    if tablero[i][j]==letra:
        print("entro")
        print(mov,tablero[index[0]][index[1]])
        resultado.append(mov)


resultado=[]
table='''. . . A . . . . . . . . . . .
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
tab=""". . . .
. A # .
. . . .
. . C .
. . . ."""
sec=tab.split('\n')
matriz = []
for i in range(len(sec)):
    matriz.append(sec[i].split(" "))
caminos(matriz,[1,1],[3,2],0,"","A")
print("resultado:\n",resultado)
print(matriz)

"""
. . . .
. A # .
. . . .
. . C .
. . . .
"""