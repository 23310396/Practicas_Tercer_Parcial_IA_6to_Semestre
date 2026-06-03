"""
INSERTION SORT - Ordenamiento por Inserción
=============================================
Este algoritmo construye la lista ordenada de uno en uno.
Toma un elemento de la parte desordenada e lo inserta en la posición correcta
dentro de la parte ordenada.

Complejidad: O(n²) en el peor caso, O(n) en el mejor caso
Espacio: O(1)
Nota: Es eficiente para listas pequeñas o casi ordenadas
"""

def insertion_sort(lista):
    """
    Ordena una lista usando el método de inserción.
    
    Args:
        lista: Lista de números a ordenar
    
    Returns:
        La lista ordenada
    """
    # Empezamos desde el segundo elemento (índice 1)
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        
        # Movemos elementos mayores que la clave una posición hacia la derecha
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        
        # Insertamos la clave en su posición correcta
        lista[j + 1] = clave
    
    return lista


# Ejemplo de uso
numeros = [64, 34, 25, 12, 22, 11, 90, 88]
print("Lista original:", numeros)

resultado = insertion_sort(numeros.copy())
print("Lista ordenada:", resultado)

# Prueba con más ejemplos
print("\n--- Más ejemplos ---")
lista2 = [5, 2, 8, 1, 9, 3]
print(f"Original: {lista2}")
print(f"Ordenada: {insertion_sort(lista2.copy())}")

lista3 = [1, 4, 0, 5, 23, 14, 12, 67, 38]
print(f"Original: {lista3}")
print(f"Ordenada: {insertion_sort(lista3.copy())}")
