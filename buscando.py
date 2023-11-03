# """Intente buscar errores en el codigo para mejorarlo"""

# def direccion(pos,find):
#     direccion=[]
#     if pos[0] - find[0]<0:
#         direccion.append(1)
#     elif pos[0] - find[0]>0:
#         direccion.append(-1)
#     else:
#         direccion.append(0)
#     if pos[1] - find[1]<0:
#         direccion.append(1)
#     elif pos[1] - find[1]>0:
#         direccion.append(-1)
#     else:
#         direccion.append(0)
#     return direccion
# def caminos(tablero,adress,index,cont,mov,letra):
#     i=index[0]
#     j=index[1]
#     cont+=1
#     mov+=","+str(index[0])+"/"+str(index[1])
#     buscar=direccion(index,adress)

#     if tablero[index[0]][index[1]] != letra and (i>0 or i<len(tablero)) and (j>0 or j<len(tablero)) and cont<10 and tablero[index[0]][index[1]] != "#":
#         print(mov,"tablero",i,j,tablero[i][j],letra)
#         if buscar[0]!=0:
#             caminos(tablero,adress,[index[0]+buscar[0],index[1]],cont,mov,letra)
#         if buscar[1]!=0:
#             caminos(tablero,adress,[index[0],index[1]+buscar[1]],cont,mov,letra)

#     if tablero[i][j]==letra:
#         print("entro")
#         print(mov,tablero[index[0]][index[1]])
#         resultado.append(mov)


# resultado=[]
# table='''. . . A . . . . . . . . . . .
# . . . . . . . . . . . . . . .
# . . . . . B . . . . . . . . .
# . . . . . . . . . . . . . . .
# . . . . . . . . . C . . . . .
# . . . . . . . D . . . . . . E
# . . . . . . . . . . . . . . .
# . . . . F . . . . . G . . . .
# . . . . . . . . . . . . . . .
# . . . . . . . . . . . . . . .
# . H . . . . . X . . . . . I .
# . . . . . . . . . . . . . . .
# . . . . . . . . . . . . . . .
# . . . . J . . . . . K . . . .
# . . . . . . . . . . . . . . .
# L . . . . . . M . . . . . . .
# . . . . . N . . . . . . . . .
# . . . . . . . . . . O . . . .
# . . . . . . . . . . . . . . .
# . . . . . . . . . . . . . . .
# . . . . . . . . . . . P . . .'''
# tab=""". . . .
# . A # .
# . . . .
# . . C .
# . . . ."""
# sec=tab.split('\n')
# matriz = []
# for i in range(len(sec)):
#     matriz.append(sec[i].split(" "))
# caminos(matriz,[1,1],[3,2],0,"","A")
# print("resultado:\n",resultado)
# print(matriz)

# """
# . . . .
# . A # .
# . . . .
# . . C .
# . . . .
# """


# Solucion planteada :

from collections import deque

def solve(maze):
    # Encuentra la entrada, la salida y los portales
    entrada = None
    salida = None
    portales = {}
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'E':
                entrada = (i, j)
            elif maze[i][j] == 'S':
                salida = (i, j)
            elif maze[i][j].islower():
                if maze[i][j] not in portales:
                    portales[maze[i][j]] = []
                portales[maze[i][j]].append((i, j))


    # BFS ( Busqueda en amplitud ) desde la entrada
    queue = deque([(entrada, 0)])
    visited = {entrada}
    while queue:
        (x, y), steps = queue.popleft()
        if (x, y) == salida:
            return steps  # Encontramos la salida
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(maze)) and (0 <= ny < len(maze[0])) and (maze[nx][ny] != '#') and ((nx, ny) not in visited):
                visited.add((nx, ny))
                queue.append(((nx, ny), steps + 1))
                if maze[nx][ny].islower():  # Si es un portal
                    for portal in portales[maze[nx][ny]]:
                        if portal not in visited:
                            visited.add(portal)
                            queue.append((portal, steps + 1))
    return -1  # No hay camino a la salida


maze = [

    # Maze 1
    # ['S', '.', '.', '.',],
    # ['#', '#', '#', '.'],
    # ['.', '.', '.', '.',],
    # ['.', '#', '#', '#'],
    # ['.', '.', '.', 'E']

    # Maze 2
    # ['E', '.', '.'],
    # ['.', '.', '.'],
    # ['.', '.', 'S']

    # Maze 3
    ['E', '#', '.'],
    ['.', '#', '.'],
    ['.', '#', 'S']
    
    

    # Maze 4
    # ['S', '.', 'b', '#', 'b'],
    # ['#', '#', '#', '#', 'a'],
    # ['.', '.', 'E', '#', '#'],
    # ['c', '#', '#', '.', 'c'],
    # ['#', 'a', '.', '.', '.']
]


print(solve(maze))