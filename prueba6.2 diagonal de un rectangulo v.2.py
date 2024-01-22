import math

def diagonal_rectangulo (ancho, alto):
    cuadrados = (ancho**2) + (alto**2)
    diagonal = math.sqrt (cuadrados)
    return diagonal
