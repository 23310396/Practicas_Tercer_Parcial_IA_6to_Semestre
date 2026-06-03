"""
MERGE SORT - Ordenamiento por Mezcla
=====================================
Algoritmo de "divide y conquista". Divide la lista en mitades recursivamente,
luego mezcla las mitades ordenadas para producir listas ordenadas.

Complejidad: O(n log n) en todos los casos
Espacio: O(n)
Nota: Muy eficiente, especialmente para listas grandes
"""

def merge_sort(lista):
    """
    Ordena una lista usando el método de mezcla (merge sort).
    
    Args:
        lista: Lista de números a ordenar
    
    Returns:
        La lista ordenada
    """
    if len(lista) <= 1:
        return lista
    
    # Dividimos la lista en dos mitades
    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]
    
    # Ordenamos recursivamente cada mitad
    izquierda = merge_sort(izquierda)
    derecha = merge_sort(derecha)
    
    # Combinamos las mitades ordenadas
    return _mezclar(izquierda, derecha)


def _mezclar(izquierda, derecha):
    """
    Mezcla dos listas ordenadas en una sola lista ordenada.
    
    Args:
        izquierda: Primera lista ordenada
        derecha: Segunda lista ordenada
    
    Returns:
        Una lista ordenada con todos los elementos
    """
    resultado = []
    i = j = 0
    
    # Comparamos elementos de ambas listas
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    
    # Añadimos los elementos restantes
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    
    return resultado


# Ejemplo de uso
numeros = [64, 34, 25, 12, 22, 11, 90, 88]
print("Lista original:", numeros)

resultado = merge_sort(numeros)
print("Lista ordenada:", resultado)

# Prueba con más ejemplos
print("\n--- Más ejemplos ---")
lista2 = [5, 2, 8, 1, 9, 3, 10, 4]
print(f"Original: {lista2}")
print(f"Ordenada: {merge_sort(lista2)}")

lista3 = [100, 50, 25, 75, 1, 99]
print(f"Original: {lista3}")
print(f"Ordenada: {merge_sort(lista3)}")
