# Simulador del Algoritmo de Dijkstra

## Descripción corta

Esta práctica consiste en realizar un simulador del algoritmo de Dijkstra usando Python. El programa permite calcular la ruta más corta dentro de un grafo precargado, mostrando el procedimiento paso a paso en consola. Además, incluye una visualización gráfica sencilla donde se muestran los nodos, las conexiones, los pesos y la ruta más corta encontrada.

## ¿Qué es el algoritmo de Dijkstra?

El algoritmo de Dijkstra es un método utilizado para encontrar la ruta más corta desde un nodo inicial hacia los demás nodos de un grafo.

Un grafo está formado por nodos y aristas. Los nodos representan puntos, lugares o elementos, mientras que las aristas representan las conexiones entre ellos. Cada arista puede tener un peso, que normalmente representa distancia, tiempo, costo o dificultad.

El algoritmo trabaja revisando las distancias acumuladas desde el nodo inicial y eligiendo siempre el nodo no visitado que tenga la menor distancia conocida. Después revisa sus vecinos y actualiza las distancias si encuentra un camino más corto.

## ¿Para qué sirve?

El algoritmo de Dijkstra sirve para resolver problemas donde se necesita encontrar el camino más corto o más eficiente entre diferentes puntos.

Algunas aplicaciones comunes son:

- Encontrar rutas más cortas en mapas.
- Calcular caminos óptimos entre ciudades.
- Optimizar rutas de transporte.
- Mejorar sistemas de entrega de paquetes.
- Buscar caminos eficientes en redes de computadoras.
- Planear rutas para robots móviles o vehículos autónomos.
- Optimizar trayectorias dentro de almacenes o líneas de producción.

## ¿Cómo funciona?

El funcionamiento general del algoritmo es el siguiente:

1. Se selecciona un nodo inicial.
2. La distancia del nodo inicial se coloca en 0.
3. Las distancias hacia los demás nodos se colocan como infinito.
4. Se selecciona el nodo no visitado con la menor distancia acumulada.
5. Se revisan sus vecinos.
6. Si se encuentra una distancia menor hacia un vecino, se actualiza.
7. El nodo actual se marca como visitado.
8. El proceso se repite hasta visitar todos los nodos.

Una condición importante es que el algoritmo de Dijkstra no debe usarse con pesos negativos, porque su lógica supone que una vez encontrada la menor distancia hacia un nodo, esa distancia ya no se reducirá después.

## ¿Cómo se implementa en el mundo?

En el mundo real, Dijkstra se puede implementar en sistemas donde existen varias rutas posibles y se necesita elegir la mejor.

Por ejemplo, en aplicaciones de navegación como mapas digitales, se puede usar para encontrar la ruta más corta entre dos ubicaciones. En redes de computadoras, puede ayudar a decidir por dónde enviar paquetes de información para que lleguen más rápido a su destino.

También se puede usar en logística, transporte y almacenes automatizados. En estos casos, cada punto de entrega, estación o máquina puede representarse como un nodo, y cada camino entre ellos puede tener un peso que represente distancia, tiempo o costo.

## ¿Cómo lo implementaría en mi vida?

Lo implementaría para organizar rutas personales cuando tengo que ir a varios lugares en un mismo día. Por ejemplo, si debo ir a la escuela, al trabajo, a una tienda y después regresar a casa, cada lugar puede representarse como un nodo y cada trayecto como una conexión con cierto tiempo o distancia.

De esa manera, el algoritmo podría ayudarme a decidir cuál recorrido me conviene más para ahorrar tiempo y evitar vueltas innecesarias.

También podría usarse para organizar actividades pendientes, considerando el tiempo o esfuerzo que requiere cada una, buscando una forma más eficiente de completarlas.

## ¿Cómo lo implementaría en mi trabajo o trabajo de ensueño?

En mi trabajo relacionado con automatización lo implementaría para optimizar rutas dentro de una planta.

Por ejemplo, en un almacén automatizado, cada estación, banda transportadora, robot o zona de almacenamiento puede representarse como un nodo. Las conexiones entre ellos pueden tener pesos dependiendo de la distancia, tiempo de traslado, consumo de energía o carga de trabajo.

Con Dijkstra se podría calcular la mejor ruta para mover materiales, piezas o productos terminados. Esto ayudaría a reducir tiempos muertos, mejorar el flujo de producción y hacer más eficiente el sistema.

También podría aplicarse en mantenimiento industrial, para planear la ruta más eficiente al revisar varias máquinas dentro de una planta.

## Funcionamiento del programa

El programa desarrollado en Python utiliza un grafo precargado con seis nodos:

A, B, C, D, E y F.

Las conexiones tienen pesos que representan distancias entre los nodos.

El usuario debe ingresar:

- Nodo inicial.
- Nodo final.

Después, el programa ejecuta el algoritmo de Dijkstra y muestra en consola cada iteración. En cada paso se indica qué nodo fue seleccionado, qué vecinos se revisan, qué distancias se actualizan y cómo queda la tabla del algoritmo.

Al final se muestra la ruta más corta entre el nodo inicial y el nodo final, junto con la distancia total.

## Ejemplo de uso

Al ejecutar el programa, se puede usar el siguiente ejemplo:

```text
Nodo inicial: A
Nodo final: F