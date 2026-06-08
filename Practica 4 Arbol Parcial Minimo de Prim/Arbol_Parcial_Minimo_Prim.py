"""
El algoritmo de Prim sirve para encontrar un árbol parcial mínimo en un grafo
conectado, no dirigido y con pesos positivos.

Un árbol parcial mínimo conecta todos los nodos del grafo usando el menor costo
total posible, sin formar ciclos.

Grafo usado:
A conecta con B(4), C(2), D(7)
B conecta con A(4), C(1), E(5)
C conecta con A(2), B(1), D(3), E(8)
D conecta con A(7), C(3), F(6)
E conecta con B(5), C(8), F(2)
F conecta con D(6), E(2)

El programa muestra el proceso paso a paso en consola y genera un archivo
HTML llamado Arbol_Prim.html para visualizar el árbol parcial mínimo.
"""

import heapq
import os


# Grafo no dirigido.
# Cada nodo tiene una lista de vecinos con su respectivo peso.
GRAFO = {
    "A": [("B", 4), ("C", 2), ("D", 7)],
    "B": [("A", 4), ("C", 1), ("E", 5)],
    "C": [("A", 2), ("B", 1), ("D", 3), ("E", 8)],
    "D": [("A", 7), ("C", 3), ("F", 6)],
    "E": [("B", 5), ("C", 8), ("F", 2)],
    "F": [("D", 6), ("E", 2)]
}


# Coordenadas para dibujar cada nodo en el HTML.
POSICIONES = {
    "A": (120, 120),
    "B": (330, 90),
    "C": (230, 260),
    "D": (480, 250),
    "E": (430, 420),
    "F": (650, 330)
}


def mostrar_grafo():
    """Muestra en consola los nodos y sus conexiones."""

    print("\nGRAFO PRECARGADO")
    print("-" * 50)

    for nodo, vecinos in GRAFO.items():
        conexiones = [f"{vecino}({peso})" for vecino, peso in vecinos]
        print(f"{nodo} -> {', '.join(conexiones)}")


def pedir_nodo_inicial():
    """Pide al usuario el nodo desde donde iniciará Prim."""

    while True:
        nodo = input("\nNodo inicial para Prim: ").strip().upper()

        if nodo in GRAFO:
            return nodo

        print(f"Nodo inválido. Usa uno de estos: {', '.join(sorted(GRAFO.keys()))}")


def imprimir_arbol(arbol, costo_total):
    """Muestra las aristas que ya forman parte del árbol parcial mínimo."""

    print("\nÁrbol actual:")
    print(f"{'Origen':<10}{'Destino':<10}{'Peso'}")
    print("-" * 30)

    if not arbol:
        print("Todavía no se ha agregado ninguna arista.")
    else:
        for origen, destino, peso in arbol:
            print(f"{origen:<10}{destino:<10}{peso}")

    print(f"Costo acumulado: {costo_total}")


def prim(inicio):
    """
    Ejecuta el algoritmo de Prim.

    El algoritmo empieza desde un nodo inicial y va agregando la arista
    de menor peso que conecte un nodo visitado con uno no visitado.
    """

    visitados = set()
    cola = []
    arbol = []
    costo_total = 0

    visitados.add(inicio)

    # Se cargan las conexiones iniciales del nodo elegido.
    for vecino, peso in GRAFO[inicio]:
        heapq.heappush(cola, (peso, inicio, vecino))

    print("\nPROCESO PASO A PASO DEL ALGORITMO DE PRIM")
    print("-" * 55)
    print(f"Nodo inicial: {inicio}")
    print("Se agregan a la cola las conexiones que salen del nodo inicial.")

    paso = 1

    while cola and len(visitados) < len(GRAFO):

        # heapq permite tomar primero la arista con menor peso.
        peso, origen, destino = heapq.heappop(cola)

        print("\n" + "=" * 55)
        print(f"PASO {paso}")
        print("=" * 55)
        print(f"Arista candidata: {origen} -> {destino} con peso {peso}")

        # Si el destino ya fue visitado, usar esta arista formaría un ciclo.
        if destino in visitados:
            print(f"No se agrega porque {destino} ya fue visitado.")
            paso += 1
            continue

        print("Se agrega al árbol porque conecta con un nodo nuevo.")

        visitados.add(destino)
        arbol.append((origen, destino, peso))
        costo_total += peso

        # Se agregan las conexiones del nuevo nodo hacia nodos no visitados.
        for vecino, peso_vecino in GRAFO[destino]:
            if vecino not in visitados:
                heapq.heappush(cola, (peso_vecino, destino, vecino))
                print(f"Se añade candidata: {destino} -> {vecino} peso {peso_vecino}")

        print(f"Nodos visitados: {', '.join(sorted(visitados))}")
        imprimir_arbol(arbol, costo_total)

        paso += 1

    return arbol, costo_total


def obtener_aristas_unicas():
    """Obtiene las aristas del grafo sin repetirlas."""

    aristas = []
    vistas = set()

    for origen, vecinos in GRAFO.items():
        for destino, peso in vecinos:
            clave = tuple(sorted((origen, destino)))

            if clave not in vistas:
                aristas.append((origen, destino, peso))
                vistas.add(clave)

    return aristas


def generar_html(arbol, costo_total):
    """Genera el archivo HTML con el grafo y el árbol parcial mínimo."""

    archivo = "Arbol_Prim.html"
    arbol_claves = {tuple(sorted((origen, destino))) for origen, destino, peso in arbol}

    lineas_svg = ""
    nodos_svg = ""

    # Dibujo de aristas.
    for origen, destino, peso in obtener_aristas_unicas():
        x1, y1 = POSICIONES[origen]
        x2, y2 = POSICIONES[destino]

        clave = tuple(sorted((origen, destino)))
        pertenece = clave in arbol_claves

        color = "#16a34a" if pertenece else "#64748b"
        grosor = 5 if pertenece else 2

        medio_x = (x1 + x2) / 2
        medio_y = (y1 + y2) / 2

        lineas_svg += f"""
        <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"
              stroke="{color}" stroke-width="{grosor}" />

        <rect x="{medio_x - 14}" y="{medio_y - 13}"
              width="28" height="22" fill="#eef2ff" />

        <text x="{medio_x}" y="{medio_y + 4}" text-anchor="middle"
              font-size="14" font-weight="bold">{peso}</text>
        """

    # Dibujo de nodos.
    for nodo, (x, y) in POSICIONES.items():
        nodos_svg += f"""
        <circle cx="{x}" cy="{y}" r="27"
                fill="#dbeafe" stroke="#1e3a8a" stroke-width="2" />

        <text x="{x}" y="{y + 6}" text-anchor="middle"
              font-size="17" font-weight="bold">{nodo}</text>
        """

    filas = ""

    for origen, destino, peso in arbol:
        filas += f"""
        <tr>
          <td>{origen}</td>
          <td>{destino}</td>
          <td>{peso}</td>
        </tr>
        """

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Árbol Parcial Mínimo de Prim</title>

  <style>
    body {{
      font-family: Arial, sans-serif;
      background: #f4f7fb;
      color: #1f2937;
      margin: 0;
      padding: 20px;
    }}

    h1 {{
      text-align: center;
      color: #1e3a8a;
    }}

    .contenedor {{
      display: grid;
      grid-template-columns: 310px 1fr;
      gap: 18px;
    }}

    .panel {{
      background: white;
      border-radius: 12px;
      padding: 16px;
      box-shadow: 0 8px 20px rgba(15, 23, 42, 0.08);
    }}

    svg {{
      width: 100%;
      height: 540px;
      background: #eef2ff;
      border-radius: 12px;
      border: 1px solid #cbd5e1;
    }}

    table {{
      width: 100%;
      border-collapse: collapse;
      margin-top: 12px;
    }}

    th, td {{
      padding: 9px;
      border-bottom: 1px solid #e2e8f0;
      text-align: left;
    }}

    th {{
      background: #eff6ff;
    }}

    .costo {{
      font-size: 20px;
      font-weight: bold;
      color: #16a34a;
    }}

    .nota {{
      color: #475569;
      line-height: 1.5;
    }}
  </style>
</head>

<body>
  <h1>Simulador del Árbol Parcial Mínimo de Prim</h1>

  <div class="contenedor">
    <section class="panel">
      <h2>Resultado</h2>

      <p class="nota">
        Las aristas verdes forman el árbol parcial mínimo.
        Las aristas grises pertenecen al grafo original.
      </p>

      <p>Costo total:</p>
      <p class="costo">{costo_total}</p>

      <h2>Aristas seleccionadas</h2>

      <table>
        <thead>
          <tr>
            <th>Origen</th>
            <th>Destino</th>
            <th>Peso</th>
          </tr>
        </thead>

        <tbody>
          {filas}
        </tbody>
      </table>
    </section>

    <section class="panel">
      <svg viewBox="0 0 760 540">
        {lineas_svg}
        {nodos_svg}
      </svg>
    </section>
  </div>
</body>
</html>
"""

    salida = os.path.join(os.path.dirname(__file__), archivo)

    with open(salida, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"\nArchivo generado: {archivo}")
    print("Ábrelo con Live Server para ver la gráfica.")


def main():
    """Control principal del programa."""

    print("Simulador de Árbol Parcial Mínimo de Prim")
    print("-" * 55)

    mostrar_grafo()

    print("\nNodos disponibles:")
    print(", ".join(sorted(GRAFO.keys())))

    inicio = pedir_nodo_inicial()

    arbol, costo_total = prim(inicio)

    print("\nRESULTADO FINAL")
    print("-" * 55)

    for origen, destino, peso in arbol:
        print(f"{origen} - {destino}: {peso}")

    print(f"\nCosto total del árbol parcial mínimo: {costo_total}")

    generar_html(arbol, costo_total)


if __name__ == "__main__":
    main()