from itertools import combinations

def leer_postes(archivo):
    """Leer coordenadas de los postes desde el archivo."""
    with open(archivo, 'r') as f:
        postes = []
        for linea in f:
            x, y = map(int, linea.split())
            if x == -1 and y == -1:
                break
            postes.append((x, y))
    return postes

def area_triangulo(p1, p2, p3):
    """Calcular el área de un triángulo dado por tres puntos."""
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2

def rama_poda(postes):
    """Encontrar el triángulo de mayor área usando Ramificación y Poda."""
    max_area = 0
    mejor_triangulo = None
    postes.sort()  

    def backtrack(combinacion, inicio):
        nonlocal max_area, mejor_triangulo
        if len(combinacion) == 3:  
            area = area_triangulo(*combinacion)
            if area > max_area:
                max_area = area
                mejor_triangulo = list(combinacion)
            return
        
        for i in range(inicio, len(postes)):
            combinacion.append(postes[i])
            if len(combinacion) < 3 or estimacion_area(combinacion) > max_area:
                backtrack(combinacion, i + 1)
            combinacion.pop()

    def estimacion_area(combinacion):
        """Estimar el área máxima posible con los puntos actuales."""
        if len(combinacion) < 2:
            return float('inf')
        
        xs = [p[0] for p in combinacion]
        ys = [p[1] for p in combinacion]
        return max(xs) * max(ys) / 2

    backtrack([], 0)
    return mejor_triangulo

archivo_entrada = "campo.in"
archivo_salida = "campo.out"

postes = leer_postes(archivo_entrada)
mejor_triangulo = rama_poda(postes)
with open(archivo_salida, 'w') as f:
    for p in mejor_triangulo:
        f.write(f"{p[0]} {p[1]}\n")
