"""
HEAP SORT - Ordenamiento por Montículo (Heap)
==============================================
Utiliza una estructura de datos llamada heap (montículo).
Construye un max-heap y extrae elementos repetidamente del tope.

Complejidad: O(n log n) en todos los casos
Espacio: O(1)
Nota: Eficiente y con rendimiento predecible, aunque más lento que quick sort en práctica
"""

def heap_sort(lista):
    """
    Ordena una lista usando el método de montículo.
    
    Args:
        lista: Lista de números a ordenar
    
    Returns:
        La lista ordenada
    """
    n = len(lista)
    
    # Construimos el max-heap
    for i in range(n // 2 - 1, -1, -1):
        _hundir(lista, n, i)
    
    # Extraemos elementos del heap uno por uno
    for i in range(n - 1, 0, -1):
        # Movemos la raíz (máximo) al final
        lista[0], lista[i] = lista[i], lista[0]
        
        # Hundimos la nueva raíz
        _hundir(lista, i, 0)
    
    return lista


def _hundir(lista, n, i):
    """
    Hunde un nodo en el heap para mantener la propiedad de max-heap.
    
    Args:
        lista: Lista que representa el heap
        n: Tamaño del heap
        i: Índice del nodo a hundir
    """
    mayor = i
    izquierda = 2 * i + 1
    derecha = 2 * i + 2
    
    # Si el hijo izquierdo es mayor que la raíz
    if izquierda < n and lista[izquierda] > lista[mayor]:
        mayor = izquierda
    
    # Si el hijo derecho es mayor que el mayor hasta ahora
    if derecha < n and lista[derecha] > lista[mayor]:
        mayor = derecha
    
    # Si el mayor no es la raíz, intercambiamos y recursamos
    if mayor != i:
        lista[i], lista[mayor] = lista[mayor], lista[i]
        _hundir(lista, n, mayor)


def _flotar(lista, i):
    """
    Flota un nodo en el heap para mantener la propiedad de max-heap.
    
    Args:
        lista: Lista que representa el heap
        i: Índice del nodo a flotar
    """
    while i > 0:
        padre = (i - 1) // 2
        if lista[i] > lista[padre]:
            lista[i], lista[padre] = lista[padre], lista[i]
            i = padre
        else:
            break


# Ejemplo de uso
numeros = [64, 34, 25, 12, 22, 11, 90, 88]
print("Lista original:", numeros)

resultado = heap_sort(numeros.copy())
print("Lista ordenada:", resultado)

# Prueba con más ejemplos
print("\n--- Más ejemplos ---")
lista2 = [5, 2, 8, 1, 9, 3, 10, 4]
print(f"Original: {lista2}")
print(f"Ordenada: {heap_sort(lista2.copy())}")

lista3 = [100, 50, 25, 75, 1, 99, 30, 60, 40]
print(f"Original: {lista3}")
print(f"Ordenada: {heap_sort(lista3.copy())}")

lista4 = [19, 10, 14, 37, 13, 11, 15, 9, 8, 4]
print(f"Original: {lista4}")
print(f"Ordenada: {heap_sort(lista4.copy())}")
