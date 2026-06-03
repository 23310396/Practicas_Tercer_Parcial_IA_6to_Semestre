"""
COCKTAIL SHAKER SORT - Ordenamiento Coctelera
===============================================
Variación de Bubble Sort que ordena en ambas direcciones (de adelante hacia atrás
y de atrás hacia adelante). Es más eficiente que Bubble Sort en ciertos casos.

Complejidad: O(n²) en general, O(n) en el mejor caso
Espacio: O(1)
Nota: Mejor rendimiento que Bubble Sort para datos con valores pequeños dispersos
"""

def cocktail_shaker_sort(lista):
    """
    Ordena una lista usando el método coctelera.
    
    Args:
        lista: Lista de números a ordenar
    
    Returns:
        La lista ordenada
    """
    n = len(lista)
    inicio = 0
    fin = n - 1
    
    while inicio < fin:
        # Fase de adelante hacia atrás
        for i in range(inicio, fin):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
        
        # El elemento más grande está en su lugar
        fin -= 1
        
        # Fase de atrás hacia adelante
        for i in range(fin, inicio, -1):
            if lista[i] < lista[i - 1]:
                lista[i], lista[i - 1] = lista[i - 1], lista[i]
        
        # El elemento más pequeño está en su lugar
        inicio += 1
    
    return lista


# Ejemplo de uso
numeros = [64, 34, 25, 12, 22, 11, 90, 88]
print("Lista original:", numeros)

resultado = cocktail_shaker_sort(numeros.copy())
print("Lista ordenada:", resultado)

# Prueba con más ejemplos
print("\n--- Más ejemplos ---")
lista2 = [5, 2, 8, 1, 9, 3]
print(f"Original: {lista2}")
print(f"Ordenada: {cocktail_shaker_sort(lista2.copy())}")

lista3 = [100, 50, 25, 75, 1, 99, 30]
print(f"Original: {lista3}")
print(f"Ordenada: {cocktail_shaker_sort(lista3.copy())}")
