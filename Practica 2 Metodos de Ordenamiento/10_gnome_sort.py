"""
GNOME SORT - Ordenamiento Gnomo
================================
Algoritmo simple que funciona como un gnomo ordenando fichas.
Compara un elemento con el anterior y lo intercambia si es necesario,
luego retrocede. Si es correcto, avanza.

Complejidad: O(n²) peor caso, O(n) mejor caso
Espacio: O(1)
Nota: Simple pero no muy eficiente, principalmente educativo
"""

def gnome_sort(lista):
    """
    Ordena una lista usando el método gnomo.
    
    Args:
        lista: Lista de números a ordenar
    
    Returns:
        La lista ordenada
    """
    n = len(lista)
    i = 0
    
    while i < n:
        # Si estamos al inicio o el elemento está en su lugar
        if i == 0 or lista[i] >= lista[i - 1]:
            i += 1
        else:
            # Intercambiamos y retrocedemos
            lista[i], lista[i - 1] = lista[i - 1], lista[i]
            i -= 1
    
    return lista


# Ejemplo de uso
numeros = [64, 34, 25, 12, 22, 11, 90, 88]
print("Lista original:", numeros)

resultado = gnome_sort(numeros.copy())
print("Lista ordenada:", resultado)

# Prueba con más ejemplos
print("\n--- Más ejemplos ---")
lista2 = [5, 2, 8, 1, 9, 3]
print(f"Original: {lista2}")
print(f"Ordenada: {gnome_sort(lista2.copy())}")

lista3 = [100, 50, 25, 75, 1, 99]
print(f"Original: {lista3}")
print(f"Ordenada: {gnome_sort(lista3.copy())}")
