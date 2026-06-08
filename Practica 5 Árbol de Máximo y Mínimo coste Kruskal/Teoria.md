# Árbol de Máximo y Mínimo Coste con Kruskal

## ¿Qué es?

El algoritmo de Kruskal es un método utilizado para encontrar un árbol de expansión dentro de un grafo conectado, no dirigido y con pesos.

Un árbol de expansión conecta todos los nodos del grafo usando solamente las aristas necesarias y sin formar ciclos.

Cuando se buscan las aristas de menor peso, se obtiene un árbol de mínimo coste. Cuando se buscan las aristas de mayor peso, se obtiene un árbol de máximo coste.

En esta práctica se simulan ambos casos: el árbol de mínimo coste y el árbol de máximo coste.

## ¿Para qué sirve?

Sirve para encontrar una forma eficiente de conectar todos los nodos de un sistema.

En el caso del árbol de mínimo coste, se busca reducir el costo total de conexión. Esto puede representar menos cable, menos distancia, menor gasto o menor tiempo.

En el caso del árbol de máximo coste, se puede usar cuando interesa seleccionar las conexiones de mayor valor, capacidad, prioridad o beneficio.

Kruskal es útil porque permite construir una red sin conexiones innecesarias y evitando ciclos.

## ¿Cómo funciona?

El algoritmo de Kruskal trabaja ordenando las aristas del grafo.

Para el árbol de mínimo coste, las aristas se ordenan de menor a mayor peso.

Para el árbol de máximo coste, las aristas se ordenan de mayor a menor peso.

Después se revisa cada arista en ese orden. Si la arista conecta dos nodos que todavía no están en el mismo grupo, se agrega al árbol. Si al agregarla se formaría un ciclo, se descarta.

El proceso termina cuando todos los nodos quedan conectados. Si el grafo tiene n nodos, el árbol final debe tener n - 1 aristas.

## ¿Cómo se implementa en el mundo?

En el mundo real, Kruskal puede aplicarse en problemas de redes y optimización.

Por ejemplo, puede ayudar a diseñar redes eléctricas, redes de fibra óptica, tuberías, caminos o conexiones entre equipos, buscando reducir el costo total de instalación.

También puede usarse para analizar sistemas donde se necesita seleccionar conexiones importantes sin repetir caminos ni crear ciclos innecesarios.

En ingeniería, este tipo de algoritmo ayuda a tomar decisiones cuando hay muchas opciones de conexión y se necesita elegir las mejores de acuerdo con un criterio de peso.

## ¿Cómo lo implementaría en mi vida?

Lo implementaría en situaciones donde necesite conectar varios puntos de la forma más conveniente.

Por ejemplo, si tuviera que organizar la conexión de varios dispositivos en una casa, taller o laboratorio, podría representar cada dispositivo como un nodo y cada cable como una arista con cierto costo.

Con el árbol de mínimo coste podría saber cómo conectar todo usando menos cable o gastando menos dinero.

También podría usar la idea del árbol de máximo coste para priorizar opciones que tengan mayor beneficio o importancia.

## ¿Cómo lo implementaría en mi trabajo o trabajo de ensueño?

En un trabajo relacionado con automatización, mecatrónica o ingeniería industrial, lo implementaría para diseñar conexiones dentro de una planta.

Por ejemplo, podría usarse para conectar sensores, PLCs, robots, estaciones de trabajo o módulos de control.

Cada equipo sería un nodo y cada posible conexión tendría un peso dependiendo de la distancia, costo, dificultad de instalación o capacidad.

El árbol de mínimo coste ayudaría a reducir cableado, material y tiempo de instalación. El árbol de máximo coste podría servir para seleccionar conexiones de mayor capacidad, prioridad o confiabilidad.

## Conclusión

El algoritmo de Kruskal es una herramienta útil para construir redes eficientes.

En esta práctica se implementó un simulador en Python que muestra paso a paso cómo se seleccionan o descartan las aristas. Además, se genera una visualización en HTML donde se muestran el árbol de mínimo coste y el árbol de máximo coste sobre el mismo grafo.