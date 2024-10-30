laberinto = [
    ['P', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['p', 'p', 'c', 'c', 'c', 'c', 'c', 'p'],
    ['p', 'p', 'c', 'p', 'p', 'p', 'c', 'p'],
    ['p', 'p', 'c', 'c', 'c', 'p', 'c', 'p'],
    ['p', 'p', 'p', 'p', 'c', 'p', 'c', 'S'],
    ['p', 'p', 'X', 'p', 'c', 'p', 'p', 'p'],
    ['p', 'X', 'c', 'c', 'c', 'c', 'p', 'p'],
    ['p', 'p', 'c', 'p', 'p', 'p', 'p', 'p'],
    ['p', 'p', 'E', 'p', 'p', 'p', 'p', 'p']
]

# Definimos las coordenadas de la entrada y la salida
entrada = (13, 2)  # posición de 'E'
salida = (9, 7)    # posición de 'S'

# Pila para almacenar el camino
pila = []
pila.append(entrada)

# Movimientos posibles: izquierda, arriba, derecha, abajo
movimientos = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def resolver_laberinto(laberinto, entrada, salida):
    while pila:
        x, y = pila[-1]
        
        # Marcamos el camino como visitado
        laberinto[x][y] = 'X'
        
        # Revisamos si hemos llegado a la salida
        if (x, y) == salida:
            return pila  # Retorna el camino completo
        
        # Intentamos con cada dirección
        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            
            # Verificamos si la posición es válida
            if 0 <= nx < len(laberinto) and 0 <= ny < len(laberinto[0]) and laberinto[nx][ny] == 'c':
                pila.append((nx, ny))
                break
        else:
            # Si no encontramos un camino, hacemos pop (backtracking)
            pila.pop()
    
    return None

# Ejecutamos la función y mostramos el camino si existe
camino = resolver_laberinto
if camino:
    print("Camino encontrado:", camino)
else:
    print("No hay solución para el laberinto.")
