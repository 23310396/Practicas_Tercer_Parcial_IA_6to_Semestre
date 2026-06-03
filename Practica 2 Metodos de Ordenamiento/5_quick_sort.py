"""
QUICK SORT - Ordenamiento Rápido
=================================
Algoritmo de "divide y conquista". Selecciona un elemento pivote,
particiona la lista en elementos menores y mayores que el pivote,
y luego ordena recursivamente cada partición.

Complejidad: O(n log n) en promedio, O(n²) en el peor caso
Espacio: O(log n)
Nota: Muy eficiente en la práctica, especialmente para datos aleatorios
"""

def quick_sort(lista):
    """
    Ordena una lista usando el método rápido (quick sort).
    
    Args:
        lista: Lista de números a ordenar
    
    Returns:
        La lista ordenada
    """
    if len(lista) <= 1:
        return lista
    
    # Seleccionamos el pivote (el elemento central)
    pivote = lista[len(lista) // 2]
    
    # Particionamos la lista
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]
    
    # Ordenamos recursivamente y combinamos
    return quick_sort(menores) + iguales + quick_sort(mayores)


def quick_sort_inplace(lista, inicio=0, fin=None):
    """
    Ordena una lista usando quick sort en el lugar (sin usar espacio extra).
    
    Args:
        lista: Lista de números a ordenar
        inicio: Índice inicial
        fin: Índice final
    
    Returns:
        La lista ordenada
    """
    if fin is None:
        fin = len(lista) - 1
    
    if inicio < fin:
        # Particionamos y obtenemos el índice del pivote
        pivot_idx = _particionar(lista, inicio, fin)
        
        # Ordenamos recursivamente las particiones
        quick_sort_inplace(lista, inicio, pivot_idx - 1)
        quick_sort_inplace(lista, pivot_idx + 1, fin)
    
    return lista


def _particionar(lista, inicio, fin):
    """
    Particiona la lista alrededor de un pivote.
    
    Args:
        lista: Lista de números
        inicio: Índice inicial
        fin: Índice final
    
    Returns:
        Índice del pivote en su posición final
    """
    pivote = lista[fin]
    i = inicio - 1
    
    for j in range(inicio, fin):
        if lista[j] < pivote:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    
    lista[i + 1], lista[fin] = lista[fin], lista[i + 1]
    return i + 1


# Ejemplo de uso
numeros = [64, 34, 25, 12, 22, 11, 90, 88]
print("Lista original:", numeros)

# Versión simple
resultado = quick_sort(numeros)
print("Lista ordenada (versión simple):", resultado)

# Versión in-place
numeros2 = [64, 34, 25, 12, 22, 11, 90, 88]
quick_sort_inplace(numeros2)
print("Lista ordenada (versión in-place):", numeros2)

# Prueba con más ejemplos
print("\n--- Más ejemplos ---")
lista2 = [5, 2, 8, 1, 9, 3, 10, 4]
print(f"Original: {lista2}")
print(f"Ordenada: {quick_sort(lista2)}")

lista3 = [100, 50, 25, 75, 1, 99, 30]
print(f"Original: {lista3}")
print(f"Ordenada: {quick_sort(lista3)}")
