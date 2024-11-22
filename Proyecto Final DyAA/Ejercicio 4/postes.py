from itertools import combinations

def leer_postes(archivo):
    with open(archivo, 'r') as f:
        postes = []
        for linea in f:
            x, y = map(int, linea.split())
            if x == -1 and y == -1:
                break
            postes.append((x, y))
    return postes

def area_triangulo(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2

def triangulo_mayor_area(postes):
    max_area = 0
    mejor_triangulo = None
    
    for p1, p2, p3 in combinations(postes, 3):
        area = area_triangulo(p1, p2, p3)
        if area > max_area:
            max_area = area
            mejor_triangulo = (p1, p2, p3)
    
    return mejor_triangulo

def escribir_resultado(archivo, triangulo):
    with open(archivo, 'w') as f:
        for p in triangulo:
            f.write(f"{p[0]} {p[1]}\n")

archivo_entrada = "campo.in"
archivo_salida = "campo.out"

postes = leer_postes(archivo_entrada)
mejor_triangulo = triangulo_mayor_area(postes)
escribir_resultado(archivo_salida, mejor_triangulo)
