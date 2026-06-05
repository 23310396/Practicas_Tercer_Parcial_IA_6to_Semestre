"""
============================================================
SIMULADOR DEL ALGORITMO DE DIJKSTRA
============================================================

Descripción:
Este programa simula el algoritmo de Dijkstra con un grafo precargado.
Muestra el procedimiento paso a paso en consola, calcula la ruta más
corta entre dos nodos y genera un archivo HTML con la gráfica del resultado.

Autor: Despreciable

Nota:
Para ver la gráfica, abre el archivo "dijkstra_grafica.html" con Live Server
en Visual Studio Code.
============================================================
"""

import math


GRAFO = {
    "A": {"B": 4, "C": 2},
    "B": {"A": 4, "C": 1, "D": 5},
    "C": {"A": 2, "B": 1, "D": 8, "E": 10},
    "D": {"B": 5, "C": 8, "E": 2, "F": 6},
    "E": {"C": 10, "D": 2, "F": 3},
    "F": {"D": 6, "E": 3},
}

POSICIONES = {
    "A": (100, 250),
    "B": (250, 120),
    "C": (250, 380),
    "D": (430, 120),
    "E": (430, 380),
    "F": (620, 250),
}


def mostrar_grafo():
    """Muestra el grafo precargado en consola."""

    print("\n==================== GRAFO PRECARGADO ====================")

    for nodo, vecinos in GRAFO.items():
        conexiones = [f"{vecino}({peso})" for vecino, peso in vecinos.items()]
        print(f"{nodo} -> {', '.join(conexiones)}")


def imprimir_tabla(distancias, anteriores, visitados):
    """Imprime la tabla actual del algoritmo."""

    print("\nTABLA ACTUAL:")
    print(f"{'Nodo':<10}{'Distancia':<15}{'Anterior':<15}{'Visitado'}")
    print("-" * 55)

    for nodo in GRAFO:
        distancia = "∞" if distancias[nodo] == math.inf else str(distancias[nodo])
        anterior = "-" if anteriores[nodo] is None else anteriores[nodo]
        visitado = "Sí" if nodo in visitados else "No"

        print(f"{nodo:<10}{distancia:<15}{anterior:<15}{visitado}")


def dijkstra(inicio):
    """
    Ejecuta el algoritmo de Dijkstra desde el nodo inicial.

    Retorna:
    - distancias: distancia mínima desde el nodo inicial hasta cada nodo.
    - anteriores: nodo anterior usado para reconstruir la ruta más corta.
    """

    distancias = {nodo: math.inf for nodo in GRAFO}
    anteriores = {nodo: None for nodo in GRAFO}
    visitados = set()

    distancias[inicio] = 0
    iteracion = 1

    print("\n================ INICIO DEL ALGORITMO =================")
    print(f"Nodo inicial: {inicio}")
    print("La distancia del nodo inicial es 0 y las demás empiezan en infinito.")

    while len(visitados) < len(GRAFO):
        nodo_actual = None
        menor_distancia = math.inf

        for nodo in GRAFO:
            if nodo not in visitados and distancias[nodo] < menor_distancia:
                menor_distancia = distancias[nodo]
                nodo_actual = nodo

        if nodo_actual is None:
            break

        print("\n--------------------------------------------------------")
        print(f"ITERACIÓN {iteracion}")
        print("--------------------------------------------------------")
        print(f"Nodo seleccionado: {nodo_actual}")
        print(f"Distancia acumulada actual: {distancias[nodo_actual]}")

        visitados.add(nodo_actual)

        for vecino, peso in GRAFO[nodo_actual].items():
            if vecino in visitados:
                continue

            nueva_distancia = distancias[nodo_actual] + peso

            print(f"\nRevisando conexión {nodo_actual} -> {vecino}")
            print(
                f"Distancia posible = {distancias[nodo_actual]} + "
                f"{peso} = {nueva_distancia}"
            )

            if nueva_distancia < distancias[vecino]:
                print(
                    f"Se actualiza {vecino}: "
                    f"{distancias[vecino]} -> {nueva_distancia}"
                )

                distancias[vecino] = nueva_distancia
                anteriores[vecino] = nodo_actual
            else:
                print(f"No se actualiza {vecino}")

        imprimir_tabla(distancias, anteriores, visitados)
        iteracion += 1

    return distancias, anteriores


def reconstruir_ruta(anteriores, inicio, fin):
    """Reconstruye la ruta más corta usando el diccionario de nodos anteriores."""

    ruta = []
    actual = fin

    while actual is not None:
        ruta.insert(0, actual)
        actual = anteriores[actual]

    if ruta and ruta[0] == inicio:
        return ruta

    return []


def obtener_aristas_ruta(ruta):
    """Convierte una ruta en pares de nodos para poder colorearla en la gráfica."""

    return [(ruta[i], ruta[i + 1]) for i in range(len(ruta) - 1)]


def generar_grafica_html(ruta, distancia_total):
    """
    Genera un archivo HTML con SVG.

    Este archivo se abre con Live Server para ver la gráfica en el navegador.
    """

    archivo = "dijkstra_grafica.html"
    aristas_ruta = obtener_aristas_ruta(ruta)
    aristas_dibujadas = set()

    svg_aristas = ""
    svg_nodos = ""

    for nodo, vecinos in GRAFO.items():
        x1, y1 = POSICIONES[nodo]

        for vecino, peso in vecinos.items():
            llave = tuple(sorted((nodo, vecino)))

            if llave in aristas_dibujadas:
                continue

            x2, y2 = POSICIONES[vecino]

            esta_en_ruta = (
                (nodo, vecino) in aristas_ruta
                or (vecino, nodo) in aristas_ruta
            )

            color = "#e53935" if esta_en_ruta else "#777777"
            grosor = 5 if esta_en_ruta else 2

            medio_x = (x1 + x2) / 2
            medio_y = (y1 + y2) / 2

            svg_aristas += f"""
            <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"
                  stroke="{color}" stroke-width="{grosor}" />

            <rect x="{medio_x - 14}" y="{medio_y - 12}"
                  width="28" height="24" fill="white" />

            <text x="{medio_x}" y="{medio_y + 5}" text-anchor="middle"
                  font-size="14" font-weight="bold">{peso}</text>
            """

            aristas_dibujadas.add(llave)

    for nodo, (x, y) in POSICIONES.items():
        if nodo == ruta[0]:
            color_nodo = "#7CFC98"
        elif nodo == ruta[-1]:
            color_nodo = "#87CEFA"
        elif nodo in ruta:
            color_nodo = "#FFD966"
        else:
            color_nodo = "#FFF2CC"

        svg_nodos += f"""
        <circle cx="{x}" cy="{y}" r="24"
                fill="{color_nodo}" stroke="black" stroke-width="2" />

        <text x="{x}" y="{y + 5}" text-anchor="middle"
              font-size="16" font-weight="bold">{nodo}</text>
        """

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Simulador de Dijkstra</title>

    <style>
        body {{
            font-family: Arial, sans-serif;
            background: #f4f4f4;
            text-align: center;
        }}

        .contenedor {{
            background: white;
            width: 850px;
            margin: 30px auto;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 0 12px rgba(0,0,0,0.2);
        }}

        svg {{
            border: 1px solid #cccccc;
            background: white;
            border-radius: 8px;
        }}

        .ruta {{
            font-size: 18px;
            font-weight: bold;
            color: #333333;
        }}

        .nota {{
            color: #555555;
        }}
    </style>
</head>

<body>
    <div class="contenedor">
        <h1>Simulador del Algoritmo de Dijkstra</h1>

        <p class="ruta">Ruta más corta: {' → '.join(ruta)}</p>
        <p class="ruta">Distancia total: {distancia_total}</p>

        <svg width="750" height="500">
            {svg_aristas}
            {svg_nodos}
        </svg>

        <p class="nota">
            La ruta más corta aparece en rojo.
            El nodo inicial está en verde y el nodo final en azul.
        </p>
    </div>
</body>
</html>
"""

    with open(archivo, "w", encoding="utf-8") as salida:
        salida.write(html)

    print("\n==================== GRÁFICA GENERADA ====================")
    print(f"Archivo creado: {archivo}")
    print("Para verla, abre ese archivo con Live Server en Visual Studio Code.")


def main():
    """Función principal del programa."""

    print("============================================================")
    print("SIMULADOR DEL ALGORITMO DE DIJKSTRA")
    print("============================================================")

    mostrar_grafo()

    print("\nNodos disponibles:")
    print(", ".join(GRAFO.keys()))

    inicio = input("\nIngresa el nodo inicial: ").strip().upper()
    fin = input("Ingresa el nodo final: ").strip().upper()

    if inicio not in GRAFO:
        print("\nError: el nodo inicial no existe.")
        return

    if fin not in GRAFO:
        print("\nError: el nodo final no existe.")
        return

    distancias, anteriores = dijkstra(inicio)
    ruta = reconstruir_ruta(anteriores, inicio, fin)

    if not ruta:
        print("\nNo existe una ruta entre esos nodos.")
        return

    distancia_total = distancias[fin]

    print("\n================= RUTA MÁS CORTA SOLICITADA =================")
    print(f"Nodo inicial: {inicio}")
    print(f"Nodo final: {fin}")
    print(f"Ruta: {' -> '.join(ruta)}")
    print(f"Distancia total: {distancia_total}")

    generar_grafica_html(ruta, distancia_total)

    print("\nPrograma finalizado.")


if __name__ == "__main__":
    main()