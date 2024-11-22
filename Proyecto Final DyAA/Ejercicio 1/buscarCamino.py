def buscar_todos_caminos(n, m, x=0, y=0, camino=None, soluciones=None):
    if camino is None:
        camino = []
    if soluciones is None:
        soluciones = []

    camino.append((x, y))

    if x == n - 1 and y == m - 1:
        soluciones.append(list(camino))
    else:
        movimientos = [(x, y + 3), (x + 2, y)]

        for nx, ny in movimientos:
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in camino:
                buscar_todos_caminos(n, m, nx, ny, camino, soluciones)

    camino.pop()

    return soluciones


n, m = 5, 8 
soluciones = buscar_todos_caminos(n, m)
print(f"Se encontraron {len(soluciones)} caminos:")
for camino in soluciones:
    print(camino)
