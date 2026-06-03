"""
RADIX SORT - Ordenamiento Radix
================================
Ordena números procesando dígitos individuales.
Utiliza counting sort como sub-rutina para cada dígito.
Muy eficiente para números con cantidad de dígitos limitada.

Complejidad: O(n * k) donde k es el número de dígitos
Espacio: O(n + d) donde d es la base (10 para decimales)
Nota: Excelente para números enteros o cadenas
"""

def radix_sort(lista):
    """
    Ordena una lista usando el método radix (por dígitos).
    
    Args:
        lista: Lista de números enteros no negativos a ordenar
    
    Returns:
        La lista ordenada
    """
    if not lista:
        return lista
    
    max_num = max(lista)
    exp = 1  # Exponente: 1, 10, 100, etc.
    
    # Procesamos cada dígito
    while max_num // exp > 0:
        lista = _counting_sort_por_digito(lista, exp)
        exp *= 10
    
    return lista


def _counting_sort_por_digito(lista, exp):
    """
    Ordena usando counting sort basado en un dígito específico.
    
    Args:
        lista: Lista a ordenar
        exp: Exponente del dígito a procesar (1, 10, 100, etc.)
    
    Returns:
        La lista parcialmente ordenada
    """
    n = len(lista)
    salida = [0] * n
    conteos = [0] * 10  # 10 dígitos posibles (0-9)
    
    # Contamos ocurrencias de cada dígito
    for i in range(n):
        digito = (lista[i] // exp) % 10
        conteos[digito] += 1
    
    # Convertimos a índices
    for i in range(1, 10):
        conteos[i] += conteos[i - 1]
    
    # Construimos la salida
    for i in range(n - 1, -1, -1):
        digito = (lista[i] // exp) % 10
        salida[conteos[digito] - 1] = lista[i]
        conteos[digito] -= 1
    
    return salida


# Ejemplo de uso
numeros = [64, 34, 25, 12, 22, 11, 90, 88]
print("Lista original:", numeros)

resultado = radix_sort(numeros.copy())
print("Lista ordenada:", resultado)

# Prueba con más ejemplos
print("\n--- Más ejemplos ---")
lista2 = [5, 2, 8, 1, 9, 3, 10, 4]
print(f"Original: {lista2}")
print(f"Ordenada: {radix_sort(lista2.copy())}")

lista3 = [100, 500, 250, 750, 10, 99, 300, 600, 400]
print(f"Original: {lista3}")
print(f"Ordenada: {radix_sort(lista3.copy())}")

lista4 = [329, 457, 657, 839, 436, 720, 355]
print(f"Original: {lista4}")
print(f"Ordenada: {radix_sort(lista4.copy())}")
