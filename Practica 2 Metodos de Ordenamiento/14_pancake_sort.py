"""
PANCAKE SORT - Ordenamiento de Panqueques
===========================================
Algoritmo que únicamente puede invertir ("voltear") prefijos de la lista.
Se utiliza para demostrar problemas teóricos. Invierte secuencias para llevar
elementos mayores al final.

Complejidad: O(n²) en general
Espacio: O(1)
Nota: Algoritmo principalmente teórico, no práctico para uso real
"""

def pancake_sort(lista):
    """
    Ordena una lista usando el método de panqueques.
    
    Args:
        lista: Lista de números a ordenar
    
    Returns:
        La lista ordenada
    """
    n = len(lista)
    
    # Iteramos desde el final hacia el inicio
    for i in range(n, 1, -1):
        # Encontramos el índice del máximo elemento
        max_idx = _encontrar_max(lista, i)
        
        # Si el máximo no está al final del segmento, lo movemos
        if max_idx != i - 1:
            # Invertimos del inicio hasta el máximo
            _invertir(lista, 0, max_idx)
            # Invertimos del inicio hasta el final del segmento
            _invertir(lista, 0, i - 1)
    
    return lista


def _encontrar_max(lista, n):
    """
    Encuentra el índice del máximo elemento en los primeros n elementos.
    
    Args:
        lista: Lista de números
        n: Número de elementos a considerar
    
    Returns:
        Índice del elemento máximo
    """
    max_idx = 0
    for i in range(1, n):
        if lista[i] > lista[max_idx]:
            max_idx = i
    return max_idx


def _invertir(lista, inicio, fin):
    """
    Invierte los elementos entre inicio y fin (inclusivo).
    
    Args:
        lista: Lista a invertir
        inicio: Índice de inicio
        fin: Índice de fin
    """
    while inicio < fin:
        lista[inicio], lista[fin] = lista[fin], lista[inicio]
        inicio += 1
        fin -= 1


# Ejemplo de uso
numeros = [64, 34, 25, 12, 22, 11, 90, 88]
print("Lista original:", numeros)

resultado = pancake_sort(numeros.copy())
print("Lista ordenada:", resultado)

# Prueba con más ejemplos
print("\n--- Más ejemplos ---")
lista2 = [5, 2, 8, 1, 9, 3]
print(f"Original: {lista2}")
print(f"Ordenada: {pancake_sort(lista2.copy())}")

lista3 = [100, 50, 25, 75, 1, 99]
print(f"Original: {lista3}")
print(f"Ordenada: {pancake_sort(lista3.copy())}")
