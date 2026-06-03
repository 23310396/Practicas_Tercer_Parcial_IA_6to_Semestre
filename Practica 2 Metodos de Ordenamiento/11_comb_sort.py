"""
COMB SORT - Ordenamiento de Peine
==================================
Mejora del Bubble Sort que utiliza un "peine" con espacios decrecientes
en lugar de comparar solo elementos adyacentes. Esto elimina "tortugas"
(valores pequeños al final que tardan en llegar al inicio).

Complejidad: O(n²) peor caso, O(n log n) en promedio
Espacio: O(1)
Nota: Mucho más rápido que Bubble Sort en práctica
"""

def comb_sort(lista):
    """
    Ordena una lista usando el método de peine.
    
    Args:
        lista: Lista de números a ordenar
    
    Returns:
        La lista ordenada
    """
    n = len(lista)
    gap = n
    intercambio = True
    
    while gap > 1 or intercambio:
        # Reducimos el gap
        gap = max(1, int(gap / 1.3))
        
        intercambio = False
        i = 0
        
        # Comparamos elementos separados por gap
        while i + gap < n:
            if lista[i] > lista[i + gap]:
                lista[i], lista[i + gap] = lista[i + gap], lista[i]
                intercambio = True
            i += 1
    
    return lista


# Ejemplo de uso
numeros = [64, 34, 25, 12, 22, 11, 90, 88]
print("Lista original:", numeros)

resultado = comb_sort(numeros.copy())
print("Lista ordenada:", resultado)

# Prueba con más ejemplos
print("\n--- Más ejemplos ---")
lista2 = [5, 2, 8, 1, 9, 3, 10, 4, 7, 6]
print(f"Original: {lista2}")
print(f"Ordenada: {comb_sort(lista2.copy())}")

lista3 = [100, 50, 25, 75, 1, 99, 30, 60, 40]
print(f"Original: {lista3}")
print(f"Ordenada: {comb_sort(lista3.copy())}")
