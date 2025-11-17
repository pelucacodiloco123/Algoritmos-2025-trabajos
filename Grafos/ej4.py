from graph import Graph
import math

antenas = Graph(is_directed=False)

antenas.insert_vertex("TGK783", {"ubicacion": "Misiones", "velocidad": "23"})
antenas.insert_vertex("T800", {"ubicacion": "Mendoza", "velocidad": "23"})
antenas.insert_vertex("ANT456", {"ubicacion": "Córdoba", "velocidad": "50"})
antenas.insert_vertex("SAT901", {"ubicacion": "Salta", "velocidad": "35"})
antenas.insert_vertex("COM234", {"ubicacion": "Buenos Aires", "velocidad": "42"})

# Nuevas antenas
antenas.insert_vertex("PTR111", {"ubicacion": "La Rioja", "velocidad": "40"})
antenas.insert_vertex("LNK202", {"ubicacion": "Chaco", "velocidad": "28"})
antenas.insert_vertex("NOD333", {"ubicacion": "Entre Ríos", "velocidad": "33"})


conexiones = [
    ("TGK783", "ANT456", 15),
    ("TGK783", "LNK202", 18),

    ("ANT456", "COM234", 10),
    ("ANT456", "PTR111", 12),

    ("COM234", "SAT901", 25),
    ("COM234", "NOD333", 14),

    ("SAT901", "T800", 20),
    ("SAT-901", "PTR-111", 16),

    ("T800", "PTR111", 30),
    ("T800", "NOD333", 28),

    ("LNK202", "NOD333", 22),
]


for origen, destino, peso in conexiones:
    antenas.insert_edge(origen, destino, peso)


def MendoaMisio(grafo):
    path = grafo.dijkstra('T800')
    destination = 'TGK783'       
    peso_total = None
    camino_completo = []
    resultados = {}
    
    while path.size() > 0:
        value = path.pop()
        if value[0] == destination:
            if peso_total is None:
                peso_total = value[1]
            camino_completo.append(value[0])
            destination = value[2]
    
    camino_completo.reverse()
    
    resultados['Mendoza'] = {
        "camino": camino_completo,
        "distancia": peso_total if peso_total is not None and peso_total != math.inf else math.inf
    }
    
    return resultados

def arbolExpansion(grafo, vertice):
    tree = grafo.kruskal(vertice)

    peso_total = 0
    for edge in tree.split(';'):
        origin, destination, weight = edge.split('-')
        peso_total += int(weight)
    return peso_total


def mostrarTGK783(grafo):
    for nodo in grafo:
        if nodo.value == "TGK783":  # Acceder directamente al value del nodo
            print(f"Antena: {nodo.value}")
            print(f"Ubicación: {nodo.other_values['ubicacion']}")
            print(f"Velocidad: {nodo.other_values['velocidad']}")
            print("Conexiones:")
            for edge in nodo.edges:
                print(f"  - Destino: {edge.value}, Peso: {edge.weight}")
            break  # Solo necesitamos mostrar TGK783 una vez
    else:
        print("No se encontró la antena TGK783")


print(len(antenas))
print(MendoaMisio(antenas))
arbolExpansion(antenas, "COM234")
mostrarTGK783(antenas)

