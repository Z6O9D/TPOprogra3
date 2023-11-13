# TPOprogra3

Estrategia:

El codigo utiliza un algoritmo de busqueda en amplitud (BFS) para encontrar el camino mas corto en un laberinto desde una entrada a una salida, teniendo en cuenta los portales que pueden transportarnos a diferentres partes del laberinto.

La estrategia fue la siguiente:
Se recorre cada celda del laberinto para encontrar la entrada, la salida y los portales. Si encuentra un portal lo agrega al diccionario de portales, con las coordenadas de su respectiva ubicacion usando la letra del portal como clave. 
Una vez encontrados la entrada, la salida y todos los portales, se inicia una busqueda en amplitud. Comienza en la entrada y explora todas las celdas adyacentes que no sean paredes (#) y que no hayan sido visitadas antes. Si la celda acual es un portal, se agregan todas las otras ubicaciones de ese portal al final de la cola. Esto nos permite saltar a traves de los portales. Si la celda actual es la salida, el codigo devuelve la cantidad de pasos que se dieron hasta llegar a ella. En cambio si el algoritmo recorre todo el laberinto y no encuentra una salida devuelve "-1", indicando que no se encontro un camino de la entrada a la salida.

Complejidad:

O( i * j + (n - m) ) 
Donde i y j son las dimensiones del laberinto y n son la cantidad de casillas posibles  y p son las paredes 