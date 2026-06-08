# Árbol Parcial Mínimo de Prim

## ¿Qué es?

El algoritmo de Prim es un método utilizado para encontrar el árbol parcial mínimo de un grafo conectado, no dirigido y con pesos.

Un árbol parcial mínimo es una estructura que conecta todos los nodos del grafo usando solamente las conexiones necesarias y con el menor costo total posible. Además, no debe formar ciclos.

En otras palabras, Prim busca una forma de unir todos los puntos de un grafo gastando lo menos posible.

## ¿Para qué sirve?

Sirve para resolver problemas donde se necesita conectar varios puntos con el menor costo.

Puede aplicarse cuando los pesos representan distancia, dinero, tiempo, cableado, energía o cualquier recurso que se quiera minimizar.

Algunos ejemplos son:

- Diseñar redes eléctricas.
- Instalar cableado de internet.
- Conectar ciudades con carreteras.
- Diseñar tuberías.
- Optimizar conexiones entre equipos.
- Planear redes de comunicación.

## ¿Cómo funciona?

El algoritmo empieza desde un nodo inicial y va construyendo poco a poco el árbol.

Primero se selecciona un nodo de inicio. Después se revisan las conexiones disponibles desde ese nodo y se elige la arista con menor peso que conecte con un nodo que todavía no esté dentro del árbol.

Luego se repite el proceso: desde los nodos que ya están dentro del árbol, se busca la conexión más barata hacia un nodo nuevo.

El algoritmo termina cuando todos los nodos ya fueron conectados.

## ¿Cómo se implementa en el mundo?

En el mundo real se puede usar para diseñar redes de bajo costo.

Por ejemplo, una empresa de telecomunicaciones podría usar Prim para decidir cómo conectar varias zonas con fibra óptica gastando la menor cantidad de cable posible.

También puede aplicarse en instalaciones eléctricas, donde se quiere conectar varias áreas usando la menor cantidad de material.

En logística e infraestructura, puede ayudar a planear conexiones entre almacenes, estaciones, máquinas o puntos de distribución.

## ¿Cómo lo implementaría en mi vida?

Lo implementaría para organizar conexiones o recorridos donde quiera gastar menos recursos.

Por ejemplo, si tuviera que conectar varios dispositivos en una casa o taller usando cable, podría representar cada equipo como un nodo y cada posible conexión como una arista con su distancia.

Después usaría Prim para encontrar la forma de conectar todo con la menor cantidad de cable.

También podría aplicarlo para organizar tareas relacionadas entre sí, buscando una forma eficiente de unir actividades o lugares sin repetir caminos innecesarios.

## ¿Cómo lo implementaría en mi trabajo o trabajo de ensueño?

En un trabajo relacionado con mecatrónica, automatización o ingeniería industrial, lo implementaría para diseñar conexiones eficientes dentro de una planta.

Por ejemplo, si se necesitan conectar sensores, PLCs, estaciones de trabajo, robots o módulos de una línea de producción, cada elemento podría representarse como un nodo.

Las conexiones podrían tener pesos según la distancia, el costo del cableado, la dificultad de instalación o el tiempo de mantenimiento.

Con Prim se podría obtener una red funcional con el menor costo total posible, evitando conexiones innecesarias y reduciendo material, tiempo y dinero.

## Conclusión

El algoritmo de Prim es útil porque permite conectar todos los nodos de un grafo con el menor costo posible y sin formar ciclos.

En esta práctica se desarrolló un simulador en Python que muestra el proceso paso a paso en consola. Además, se genera una visualización en HTML donde se puede observar el grafo original y el árbol parcial mínimo resaltado.