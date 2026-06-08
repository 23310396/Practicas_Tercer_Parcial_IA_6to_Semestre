"""
Kruskal permite encontrar un árbol de mínimo coste o máximo coste en un grafo
conectado, no dirigido y con pesos.

El árbol de mínimo coste conecta todos los nodos usando las aristas más baratas
sin formar ciclos. El árbol de máximo coste hace lo contrario: conecta todos los
nodos usando las aristas de mayor peso posible, también evitando ciclos.

Grafo usado:
A-B(4), A-C(2), A-D(7)
B-C(1), B-E(5)
C-D(3), C-E(8)
D-F(6)
E-F(2)

El programa muestra el proceso paso a paso en consola y genera un archivo HTML
llamado Kruskal_Max_Min.html para visualizar los árboles resultantes.
"""

import os


# Lista de aristas del grafo:
# cada tupla tiene: origen, destino y peso.
ARISTAS = [
    ("A", "B", 4),
    ("A", "C", 2),
    ("A", "D", 7),
    ("B", "C", 1),
    ("B", "E", 5),
    ("C", "D", 3),
    ("C", "E", 8),
    ("D", "F", 6),
    ("E", "F", 2)
]


# Coordenadas para dibujar los nodos en el HTML.
POSICIONES = {
    "A": (120, 130),
    "B": (330, 90),
    "C": (240, 270),
    "D": (500, 250),
    "E": (420, 420),
    "F": (650, 330)
}


def obtener_nodos():
    """Obtiene todos los nodos existentes a partir de la lista de aristas."""

    nodos = set()

    for origen, destino, peso in ARISTAS:
        nodos.add(origen)
        nodos.add(destino)

    return sorted(nodos)


def mostrar_grafo():
    """Muestra en consola todas las aristas del grafo original."""

    print("\nGRAFO PRECARGADO")
    print("-" * 45)
    print(f"{'Origen':<10}{'Destino':<10}{'Peso'}")
    print("-" * 45)

    for origen, destino, peso in ARISTAS:
        print(f"{origen:<10}{destino:<10}{peso}")


def crear_conjuntos(nodos):
    """
    Crea la estructura inicial de conjuntos.

    Al inicio, cada nodo es su propio representante.
    Esto sirve para detectar ciclos.
    """

    padre = {}

    for nodo in nodos:
        padre[nodo] = nodo

    return padre


def encontrar(padre, nodo):
    """
    Busca el representante principal de un nodo.

    Si dos nodos tienen el mismo representante, significa que ya pertenecen
    al mismo grupo y unirlos formaría un ciclo.
    """

    if padre[nodo] != nodo:
        padre[nodo] = encontrar(padre, padre[nodo])

    return padre[nodo]


def unir(padre, nodo_a, nodo_b):
    """Une dos conjuntos si pertenecen a grupos diferentes."""

    raiz_a = encontrar(padre, nodo_a)
    raiz_b = encontrar(padre, nodo_b)

    if raiz_a != raiz_b:
        padre[raiz_b] = raiz_a
        return True

    return False


def imprimir_arbol(nombre, arbol, costo):
    """Imprime las aristas seleccionadas hasta el momento."""

    print(f"\n{nombre}:")
    print(f"{'Origen':<10}{'Destino':<10}{'Peso'}")
    print("-" * 30)

    if not arbol:
        print("Todavía no hay aristas seleccionadas.")
    else:
        for origen, destino, peso in arbol:
            print(f"{origen:<10}{destino:<10}{peso}")

    print(f"Costo acumulado: {costo}")


def kruskal(tipo):
    """
    Ejecuta Kruskal.

    tipo = "minimo"  -> ordena las aristas de menor a mayor peso.
    tipo = "maximo"  -> ordena las aristas de mayor a menor peso.
    """

    nodos = obtener_nodos()
    padre = crear_conjuntos(nodos)

    if tipo == "minimo":
        aristas_ordenadas = sorted(ARISTAS, key=lambda arista: arista[2])
        titulo = "ÁRBOL DE MÍNIMO COSTE"
    else:
        aristas_ordenadas = sorted(ARISTAS, key=lambda arista: arista[2], reverse=True)
        titulo = "ÁRBOL DE MÁXIMO COSTE"

    arbol = []
    costo_total = 0
    paso = 1

    print("\n" + "=" * 55)
    print(f"PROCESO PASO A PASO - {titulo}")
    print("=" * 55)

    print("\nOrden de revisión de aristas:")
    for origen, destino, peso in aristas_ordenadas:
        print(f"{origen}-{destino}({peso})")

    for origen, destino, peso in aristas_ordenadas:
        print("\n" + "-" * 55)
        print(f"PASO {paso}")
        print("-" * 55)
        print(f"Arista revisada: {origen} - {destino} con peso {peso}")

        raiz_origen = encontrar(padre, origen)
        raiz_destino = encontrar(padre, destino)

        print(f"Representante de {origen}: {raiz_origen}")
        print(f"Representante de {destino}: {raiz_destino}")

        # Si tienen diferente representante, no se forma ciclo.
        if unir(padre, origen, destino):
            print("Se agrega porque no forma ciclo.")

            arbol.append((origen, destino, peso))
            costo_total += peso
        else:
            print("No se agrega porque formaría un ciclo.")

        imprimir_arbol(titulo, arbol, costo_total)

        # Un árbol con n nodos siempre tiene n-1 aristas.
        if len(arbol) == len(nodos) - 1:
            print("\nYa se conectaron todos los nodos necesarios.")
            break

        paso += 1

    return arbol, costo_total


def aristas_clave(arbol):
    """Convierte las aristas del árbol a claves fáciles de comparar."""

    claves = set()

    for origen, destino, peso in arbol:
        claves.add(tuple(sorted((origen, destino))))

    return claves


def generar_lineas_svg(arbol_min, arbol_max):
    """Genera las líneas SVG del grafo para el archivo HTML."""

    claves_min = aristas_clave(arbol_min)
    claves_max = aristas_clave(arbol_max)

    resultado = ""

    for origen, destino, peso in ARISTAS:
        x1, y1 = POSICIONES[origen]
        x2, y2 = POSICIONES[destino]
        clave = tuple(sorted((origen, destino)))

        if clave in claves_min and clave in claves_max:
            color = "#7c3aed"
            grosor = 6
        elif clave in claves_min:
            color = "#16a34a"
            grosor = 5
        elif clave in claves_max:
            color = "#dc2626"
            grosor = 5
        else:
            color = "#64748b"
            grosor = 2

        medio_x = (x1 + x2) / 2
        medio_y = (y1 + y2) / 2

        resultado += f"""
        <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"
              stroke="{color}" stroke-width="{grosor}" />

        <rect x="{medio_x - 14}" y="{medio_y - 13}"
              width="28" height="22" fill="#eef2ff" />

        <text x="{medio_x}" y="{medio_y + 4}" text-anchor="middle"
              font-size="14" font-weight="bold">{peso}</text>
        """

    return resultado


def generar_nodos_svg():
    """Genera los círculos y etiquetas de los nodos."""

    resultado = ""

    for nodo, (x, y) in POSICIONES.items():
        resultado += f"""
        <circle cx="{x}" cy="{y}" r="27"
                fill="#dbeafe" stroke="#1e3a8a" stroke-width="2" />

        <text x="{x}" y="{y + 6}" text-anchor="middle"
              font-size="17" font-weight="bold">{nodo}</text>
        """

    return resultado


def generar_filas(arbol):
    """Genera filas HTML para la tabla de resultados."""

    filas = ""

    for origen, destino, peso in arbol:
        filas += f"""
        <tr>
          <td>{origen}</td>
          <td>{destino}</td>
          <td>{peso}</td>
        </tr>
        """

    return filas


def generar_html(arbol_min, costo_min, arbol_max, costo_max):
    """Genera el archivo HTML para visualizar ambos árboles."""

    archivo = "Kruskal_Max_Min.html"

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Kruskal - Máximo y Mínimo Coste</title>

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
      grid-template-columns: 360px 1fr;
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
      margin-top: 10px;
      margin-bottom: 18px;
    }}

    th, td {{
      padding: 8px;
      border-bottom: 1px solid #e2e8f0;
      text-align: left;
    }}

    th {{
      background: #eff6ff;
    }}

    .min {{
      color: #16a34a;
      font-weight: bold;
    }}

    .max {{
      color: #dc2626;
      font-weight: bold;
    }}

    .nota {{
      color: #475569;
      line-height: 1.5;
    }}
  </style>
</head>

<body>
  <h1>Simulador de Kruskal</h1>

  <div class="contenedor">
    <section class="panel">
      <h2>Resultado</h2>

      <p class="nota">
        Verde: árbol de mínimo coste.<br>
        Rojo: árbol de máximo coste.<br>
        Morado: arista compartida por ambos árboles.
      </p>

      <h3 class="min">Árbol de mínimo coste</h3>
      <p><strong>Costo total:</strong> {costo_min}</p>

      <table>
        <thead>
          <tr>
            <th>Origen</th>
            <th>Destino</th>
            <th>Peso</th>
          </tr>
        </thead>
        <tbody>
          {generar_filas(arbol_min)}
        </tbody>
      </table>

      <h3 class="max">Árbol de máximo coste</h3>
      <p><strong>Costo total:</strong> {costo_max}</p>

      <table>
        <thead>
          <tr>
            <th>Origen</th>
            <th>Destino</th>
            <th>Peso</th>
          </tr>
        </thead>
        <tbody>
          {generar_filas(arbol_max)}
        </tbody>
      </table>
    </section>

    <section class="panel">
      <svg viewBox="0 0 760 540">
        {generar_lineas_svg(arbol_min, arbol_max)}
        {generar_nodos_svg()}
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

    print("Simulador de Kruskal - mínimo y máximo coste")
    print("-" * 55)

    mostrar_grafo()

    arbol_min, costo_min = kruskal("minimo")
    arbol_max, costo_max = kruskal("maximo")

    print("\n" + "=" * 55)
    print("RESULTADOS FINALES")
    print("=" * 55)

    imprimir_arbol("ÁRBOL DE MÍNIMO COSTE", arbol_min, costo_min)
    imprimir_arbol("ÁRBOL DE MÁXIMO COSTE", arbol_max, costo_max)

    generar_html(arbol_min, costo_min, arbol_max, costo_max)


if __name__ == "__main__":
    main()