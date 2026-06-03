# Métodos de Ordenamiento en Python

Este directorio contiene implementaciones de 14 métodos de ordenamiento en Python, con código sencillo y bien explicado.

## 📁 Archivos

### 1_bubble_sort.py
**Ordenamiento de Burbuja**
- Compara pares adyacentes e intercambia si están en orden incorrecto
- Complejidad: O(n²)
- Mejor para: Listas pequeñas

### 2_selection_sort.py
**Ordenamiento por Selección**
- Encuentra el elemento mínimo y lo coloca en su posición
- Complejidad: O(n²)
- Mejor para: Casos donde el espacio es crítico

### 3_insertion_sort.py
**Ordenamiento por Inserción**
- Inserta elementos en su posición correcta
- Complejidad: O(n²) peor caso, O(n) mejor caso
- Mejor para: Listas pequeñas o casi ordenadas

### 4_merge_sort.py
**Ordenamiento por Mezcla**
- Divide la lista recursivamente y mezcla las mitades ordenadas
- Complejidad: O(n log n)
- Mejor para: Listas grandes, necesita espacio extra

### 5_quick_sort.py
**Ordenamiento Rápido**
- Selecciona un pivote y particiona la lista
- Complejidad: O(n log n) promedio, O(n²) peor caso
- Mejor para: Listas grandes, muy rápido en práctica

### 6_shell_sort.py
**Ordenamiento de Shell**
- Generalización de inserción con espacios decrecientes
- Complejidad: O(n log n) o O(n^1.25)
- Mejor para: Listas medianas

### 7_counting_sort.py
**Ordenamiento por Conteo**
- Cuenta ocurrencias de cada número
- Complejidad: O(n + k)
- Mejor para: Números enteros en rango conocido

### 8_radix_sort.py
**Ordenamiento Radix**
- Ordena por dígitos individuales
- Complejidad: O(n·k)
- Mejor para: Números enteros positivos

### 9_heap_sort.py
**Ordenamiento por Montículo**
- Utiliza una estructura de heap
- Complejidad: O(n log n)
- Mejor para: Rendimiento predecible

### 10_gnome_sort.py
**Ordenamiento Gnomo**
- Algoritmo simple que compara y retrocede
- Complejidad: O(n²)
- Mejor para: Educativo, listas pequeñas

### 11_comb_sort.py
**Ordenamiento de Peine**
- Mejora de Bubble Sort con espacios decrecientes
- Complejidad: O(n²) peor caso, O(n log n) promedio
- Mejor para: Datos con valores dispersos

### 12_bucket_sort.py
**Ordenamiento por Cubetas**
- Distribuye elementos en cubetas y ordena cada una
- Complejidad: O(n + k) promedio
- Mejor para: Números en un rango específico

### 13_cocktail_shaker_sort.py
**Ordenamiento Coctelera**
- Variación de Bubble Sort que ordena en ambas direcciones
- Complejidad: O(n²)
- Mejor para: Datos con valores pequeños dispersos

### 14_pancake_sort.py
**Ordenamiento de Panqueques**
- Ordena invirtiendo prefijos de la lista
- Complejidad: O(n²)
- Mejor para: Problema teórico, demostración educativa

### 0_main.py
Archivo principal que:
- Demuestra el uso de cada método
- Compara el rendimiento de todos los métodos
- Muestra el análisis de complejidad

## 📊 Comparación Rápida

| Método | Mejor Caso | Promedio | Peor Caso | Espacio | Estable |
|--------|-----------|----------|-----------|---------|---------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | ✓ |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | ✗ |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | ✓ |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | ✓ |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | ✗ |
| Shell Sort | O(n) | O(n log n) | O(n²) | O(1) | ✗ |
| Counting Sort | O(n+k) | O(n+k) | O(n+k) | O(n+k) | ✓ |
| Radix Sort | O(n·k) | O(n·k) | O(n·k) | O(n+k) | ✓ |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | ✗ |
| Gnome Sort | O(n) | O(n²) | O(n²) | O(1) | ✓ |
| Comb Sort | O(n log n) | O(n log n) | O(n²) | O(1) | ✗ |
| Bucket Sort | O(n+k) | O(n+k) | O(n²) | O(n+k) | ✓ |
| Cocktail Sort | O(n) | O(n²) | O(n²) | O(1) | ✓ |
| Pancake Sort | O(n) | O(n²) | O(n²) | O(1) | ✗ |

## 🚀 Cómo Usar

### Ejecutar un método específico:
```bash
python 1_bubble_sort.py
```

Cada archivo se ejecuta directamente sin necesidad de bloque `if __name__ == "__main__":`

### Comparar todos los métodos:
```bash
python 0_main.py
```

## 💡 Tips

- **Listas pequeñas (< 50 elementos)**: Insertion Sort, Gnome Sort
- **Listas medianas**: Shell Sort, Comb Sort, Quick Sort
- **Listas grandes**: Merge Sort, Quick Sort, Heap Sort, Radix Sort
- **Números enteros con rango limitado**: Counting Sort, Bucket Sort, Radix Sort
- **Se requiere estabilidad**: Merge Sort, Insertion Sort, Counting Sort, Bucket Sort
- **Mejor rendimiento práctico**: Quick Sort, Merge Sort
- **Rendimiento predecible**: Heap Sort, Merge Sort
- **Educativo**: Gnome Sort, Pancake Sort

## 📝 Ejemplo de Uso

```python
from bubble_sort import bubble_sort

lista = [64, 34, 25, 12, 22, 11, 90, 88]
resultado = bubble_sort(lista)
print(resultado)  # [11, 12, 22, 25, 34, 64, 88, 90]
```

## 🎯 Conceptos Clave

### Complejidad de Tiempo
- **O(1)**: Constante
- **O(log n)**: Logarítmica
- **O(n)**: Lineal
- **O(n log n)**: Lineal-logarítmica
- **O(n²)**: Cuadrática
- **O(2^n)**: Exponencial

### Estabilidad
Un algoritmo es estable si mantiene el orden relativo de elementos iguales.

### Espacio Auxiliar
La cantidad de memoria adicional que requiere el algoritmo.

## 📚 Referencias

- Algoritmos de ordenamiento clásicos
- Análisis de complejidad computacional
- Implementaciones optimizadas
- Métodos teóricos y educativos

