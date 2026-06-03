"""
COUNTING SORT - Ordenamiento por Conteo
========================================
Algoritmo que funciona contando cuántas veces aparece cada número.
No compara elementos, sino que cuenta ocurrencias.
Muy eficiente para rangos limitados de números enteros.

Complejidad: O(n + k) donde k es el rango de números
Espacio: O(n + k)
Nota: Ideal para números enteros en un rango conocido
"""

def counting_sort(lista):
    """
    Ordena una lista usando el método de conteo.
    
    Args:
        lista: Lista de números enteros no negativos a ordenar
    
    Returns:
        La lista ordenada
    """
    if not lista:
        return lista
    
    # Encontramos el valor máximo y mínimo
    min_val = min(lista)
    max_val = max(lista)
    
    # Creamos un array de conteos
    rango = max_val - min_val + 1
    conteos = [0] * rango
    
    # Contamos ocurrencias de cada número
    for num in lista:
        conteos[num - min_val] += 1
    
    # Convertimos conteos en índices
    for i in range(1, len(conteos)):
        conteos[i] += conteos[i - 1]
    
    # Construimos la lista ordenada
    resultado = [0] * len(lista)
    
    # Iteramos de atrás hacia adelante para mantener estabilidad
    for num in reversed(lista):
        idx = conteos[num - min_val] - 1
        resultado[idx] = num
        conteos[num - min_val] -= 1
    
    return resultado


def counting_sort_simple(lista):
    """
    Versión simple del ordenamiento por conteo (asume números positivos).
    
    Args:
        lista: Lista de números enteros positivos a ordenar
    
    Returns:
        La lista ordenada
    """
    if not lista:
        return lista
    
    max_val = max(lista)
    conteos = [0] * (max_val + 1)
    
    # Contamos ocurrencias
    for num in lista:
        conteos[num] += 1
    
    # Reconstruimos la lista
    resultado = []
    for i in range(len(conteos)):
        resultado.extend([i] * conteos[i])
    
    return resultado


# Ejemplo de uso
numeros = [64, 34, 25, 12, 22, 11, 90, 88]
print("Lista original:", numeros)

resultado = counting_sort(numeros)
print("Lista ordenada:", resultado)

# Versión simple
resultado_simple = counting_sort_simple(numeros)
print("Lista ordenada (versión simple):", resultado_simple)

# Prueba con más ejemplos
print("\n--- Más ejemplos ---")
lista2 = [5, 2, 8, 1, 9, 3, 10, 4]
print(f"Original: {lista2}")
print(f"Ordenada: {counting_sort_simple(lista2)}")

lista3 = [100, 50, 25, 75, 1, 99, 30, 60, 40]
print(f"Original: {lista3}")
print(f"Ordenada: {counting_sort(lista3)}")
