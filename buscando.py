# Solucion planteada :

def solve(maze): # O( i * j + (n - m) ) donde i y j son las dimensiones del laberinto y n son la cantidad de casillas posibles  y p son las paredes 
    # Encuentra la entrada, la salida y los portales
    entrada = None
    salida = None
    portales = {}
    for i in range(len(maze)):  # O( i * j )
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
    queue = [(entrada, 0)]
    visited = {entrada}
    while queue: # Mientras la cola no este vacia           O( n - m )
        (x, y), steps = queue.pop(0)  # Usamos pop(0) para eliminar el primer elemento
        if (x, y) == salida:
            return steps  # Encontramos la salida
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # Movimientos posibles    
            nx, ny = x + dx, y + dy # Nueva posicion
            if (0 <= nx < len(maze)) and (0 <= ny < len(maze[0])) and (maze[nx][ny] != '#') and ((nx, ny) not in visited): # Si no es pared y no hemos visitado la posicion
                visited.add((nx, ny))
                queue.append(((nx, ny), steps + 1))
                if maze[nx][ny].islower():  # Si es un portal
                    for portal in portales[maze[nx][ny]]: # Buscamos el otro portal
                        if portal not in visited:  
                            visited.add(portal)
                            queue.append((portal, steps + 2)) # Sumamos 2 pasos por el portal
    return -1  # No hay camino a la salida


maze = [

    # Maze 1
    ['.', '.', '.', '.',],
    ['#', '#', '#', '.'],
    ['.', 'S', '.', '.',],
    ['.', '#', '#', '.'],
    ['.', '.', '.', 'E']

    # Maze 2
    # ['E', '.', '.'],
    # ['.', '.', '.'],
    # ['.', '.', 'S']

    # Maze 3
    # ['E', '#', '.'],
    # ['.', '#', '.'],
    # ['.', '#', 'S']
    

    # Maze 4
    # ['S', '.', 'b', '#', 'b'],
    # ['#', '#', '#', '#', 'a'],
    # ['.', '.', 'E', '#', '#'],
    # ['c', '#', '#', '.', 'c'],
    # ['#', 'a', '.', '.', '.']
]


print("Se necesitan ",solve(maze), " pasos para llegar a la salida")