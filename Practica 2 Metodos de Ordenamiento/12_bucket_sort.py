"""
BUCKET SORT - Ordenamiento por Cubetas (Buckets)
=================================================
Algoritmo que distribuye elementos en "cubetas" y luego ordena cada cubeta.
Funciona bien para datos distribuidos uniformemente en un rango conocido.

Complejidad: O(n + k) en promedio, O(n²) peor caso
Espacio: O(n + k) donde k es el número de cubetas
Nota: Excelente para números en un rango específico
"""

def bucket_sort(lista, num_buckets=10):
    """
    Ordena una lista usando el método de cubetas.
    
    Args:
        lista: Lista de números a ordenar (entre 0 y 1, o escalable)
        num_buckets: Número de cubetas a utilizar
    
    Returns:
        La lista ordenada
    """
    if len(lista) == 0:
        return lista
    
    # Encontramos los valores mínimo y máximo
    min_val = min(lista)
    max_val = max(lista)
    
    # Evitamos división por cero
    if min_val == max_val:
        return sorted(lista)
    
    # Creamos las cubetas
    rango = max_val - min_val
    cubetas = [[] for _ in range(num_buckets)]
    
    # Distribuimos elementos en las cubetas
    for num in lista:
        # Calculamos el índice de la cubeta
        if num == max_val:
            idx = num_buckets - 1
        else:
            idx = int((num - min_val) / rango * (num_buckets - 1))
        cubetas[idx].append(num)
    
    # Ordenamos cada cubeta y combinamos
    resultado = []
    for cubeta in cubetas:
        # Usamos insertion sort para cada cubeta (rápido para pocos elementos)
        cubeta.sort()
        resultado.extend(cubeta)
    
    return resultado


# Ejemplo de uso
numeros = [64, 34, 25, 12, 22, 11, 90, 88]
print("Lista original:", numeros)

resultado = bucket_sort(numeros, num_buckets=5)
print("Lista ordenada:", resultado)

# Prueba con más ejemplos
print("\n--- Más ejemplos ---")
lista2 = [5, 2, 8, 1, 9, 3, 10, 4]
print(f"Original: {lista2}")
print(f"Ordenada: {bucket_sort(lista2, num_buckets=4)}")

lista3 = [100, 50, 25, 75, 1, 99, 30, 60, 40]
print(f"Original: {lista3}")
print(f"Ordenada: {bucket_sort(lista3, num_buckets=5)}")
