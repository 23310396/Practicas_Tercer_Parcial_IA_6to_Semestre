"""
BUBBLE SORT - Ordenamiento de Burbuja
======================================
El ordenamiento de burbuja es el algoritmo más simple.
Compara pares de elementos adyacentes y los intercambia si están en el orden incorrecto.
El proceso se repite hasta que la lista esté ordenada.

Complejidad: O(n²) en el peor caso, O(n) en el mejor caso
Espacio: O(1)
"""

def bubble_sort(lista):
    """
    Ordena una lista usando el método de burbuja.
    
    Args:
        lista: Lista de números a ordenar
    
    Returns:
        La lista ordenada
    """
    n = len(lista)
    
    # Recorremos la lista
    for i in range(n):
        # Flag para optimizar: si no hay intercambios, está ordenada
        intercambio = False
        
        # Comparamos elementos adyacentes
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # Intercambiamos si el elemento es mayor
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio = True
        
        # Si no hay intercambios, la lista está ordenada
        if not intercambio:
            break
    
    return lista


# Ejemplo de uso
numeros = [64, 34, 25, 12, 22, 11, 90, 88]
print("Lista original:", numeros)

resultado = bubble_sort(numeros.copy())
print("Lista ordenada:", resultado)

# Prueba con más ejemplos
print("\n--- Más ejemplos ---")
lista2 = [5, 2, 8, 1, 9, 3]
print(f"Original: {lista2}")
print(f"Ordenada: {bubble_sort(lista2.copy())}")

lista3 = [1, 2, 3, 4, 5]
print(f"Original: {lista3}")
print(f"Ordenada: {bubble_sort(lista3.copy())}")
