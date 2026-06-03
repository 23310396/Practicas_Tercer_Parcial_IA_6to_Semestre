"""
SELECTION SORT - Ordenamiento por Selección
=============================================
Este algoritmo divide la lista en dos partes: ordenada y desordenada.
En cada iteración, encuentra el elemento mínimo de la parte desordenada
y lo coloca al final de la parte ordenada.

Complejidad: O(n²) en todos los casos
Espacio: O(1)
"""

def selection_sort(lista):
    """
    Ordena una lista usando el método de selección.
    
    Args:
        lista: Lista de números a ordenar
    
    Returns:
        La lista ordenada
    """
    n = len(lista)
    
    # Recorremos la lista
    for i in range(n):
        # Asumimos que el elemento actual es el mínimo
        minimo_idx = i
        
        # Buscamos el elemento mínimo en el resto de la lista
        for j in range(i + 1, n):
            if lista[j] < lista[minimo_idx]:
                minimo_idx = j
        
        # Intercambiamos el elemento mínimo encontrado con el actual
        lista[i], lista[minimo_idx] = lista[minimo_idx], lista[i]
    
    return lista


# Ejemplo de uso
numeros = [64, 34, 25, 12, 22, 11, 90, 88]
print("Lista original:", numeros)

resultado = selection_sort(numeros.copy())
print("Lista ordenada:", resultado)

# Prueba con más ejemplos
print("\n--- Más ejemplos ---")
lista2 = [5, 2, 8, 1, 9, 3]
print(f"Original: {lista2}")
print(f"Ordenada: {selection_sort(lista2.copy())}")

lista3 = [29, 10, 14, 37, 13]
print(f"Original: {lista3}")
print(f"Ordenada: {selection_sort(lista3.copy())}")
