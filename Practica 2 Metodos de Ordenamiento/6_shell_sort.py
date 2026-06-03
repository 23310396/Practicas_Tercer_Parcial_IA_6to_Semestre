"""
SHELL SORT - Ordenamiento de Shell
===================================
Generalización del ordenamiento por inserción que permite el intercambio
de elementos lejanos. Utiliza una secuencia de espacios decrecientes.

Complejidad: Depende de la secuencia de espacios, típicamente O(n log n) o O(n^1.25)
Espacio: O(1)
Nota: Más eficiente que inserción para listas medianas
"""

def shell_sort(lista):
    """
    Ordena una lista usando el método de Shell.
    
    Args:
        lista: Lista de números a ordenar
    
    Returns:
        La lista ordenada
    """
    n = len(lista)
    
    # Iniciamos el espacio (gap) como la mitad de la longitud
    espacio = n // 2
    
    # Reducimos el espacio hasta 1
    while espacio > 0:
        # Hacemos un ordenamiento por inserción con el espacio actual
        for i in range(espacio, n):
            temp = lista[i]
            j = i
            
            # Comparamos elementos separados por el espacio
            while j >= espacio and lista[j - espacio] > temp:
                lista[j] = lista[j - espacio]
                j -= espacio
            
            lista[j] = temp
        
        # Reducimos el espacio
        espacio //= 2
    
    return lista


# Ejemplo de uso
numeros = [64, 34, 25, 12, 22, 11, 90, 88]
print("Lista original:", numeros)

resultado = shell_sort(numeros.copy())
print("Lista ordenada:", resultado)

# Prueba con más ejemplos
print("\n--- Más ejemplos ---")
lista2 = [5, 2, 8, 1, 9, 3, 10, 4, 7, 6]
print(f"Original: {lista2}")
print(f"Ordenada: {shell_sort(lista2.copy())}")

lista3 = [100, 50, 25, 75, 1, 99, 30, 60, 40]
print(f"Original: {lista3}")
print(f"Ordenada: {shell_sort(lista3.copy())}")
