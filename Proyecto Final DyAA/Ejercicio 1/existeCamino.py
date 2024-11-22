def existe_camino(n, m, x=0, y=0, visitados=None):
    if visitados is None:
        visitados = set()

    if x == n - 1 and y == m - 1:
        return True

    visitados.add((x, y))

    movimientos = [(x, y + 3), (x + 2, y)]

    for nx, ny in movimientos:
        if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visitados:
            if existe_camino(n, m, nx, ny, visitados):
                return True

    visitados.remove((x, y))
    return False



n, m = 5, 8
print("¿Existe un camino?", existe_camino(n, m))
