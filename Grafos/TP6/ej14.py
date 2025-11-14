from graph import Graph
import math

Casa = Graph(is_directed=False)

Casa.insert_vertex("Cocina")
Casa.insert_vertex("Comedor")
Casa.insert_vertex("Cochera")
Casa.insert_vertex("Quincho")
Casa.insert_vertex("Baño1")
Casa.insert_vertex("Baño2")
Casa.insert_vertex("habitacion1")
Casa.insert_vertex("habitacion2")
Casa.insert_vertex("SaladeEstar")
Casa.insert_vertex("Terraza")
Casa.insert_vertex("Patio")

#distancia en metros
conexiones = [
    # Cocina - 5 aristas (uno de los vértices con 5 conexiones)
    ("Cocina", "Comedor", 5),
    ("Cocina", "Baño1", 3),
    ("Cocina", "SaladeEstar", 4),
    ("Cocina", "Patio", 8),
    ("Cocina", "habitacion1", 7),
    
    # Comedor - 5 aristas (segundo vértice con 5 conexiones)
    ("Comedor", "SaladeEstar", 2),
    ("Comedor", "Terraza", 6),
    ("Comedor", "Patio", 4),
    ("Comedor", "Quincho", 10),
    ("Comedor", "Baño2", 5),
    
    # Cochera - 3 aristas
    ("Cochera", "Quincho", 3),
    ("Cochera", "Patio", 12),
    ("Cochera", "habitacion2", 8),
    
    # Quincho - 3 aristas
    ("Quincho", "Terraza", 4),
    ("Quincho", "Patio", 6),
    ("Quincho", "Baño2", 7),
    
    # Baño1 - 3 aristas
    ("Baño1", "habitacion1", 2),
    ("Baño1", "SaladeEstar", 3),
    ("Baño1", "Patio", 9),
    
    # Baño2 - 3 aristas
    ("Baño2", "habitacion2", 3),
    ("Baño2", "Terraza", 5),
    ("Baño2", "Quincho", 7),
    
    # habitacion1 - 3 aristas
    ("habitacion1", "SaladeEstar", 4),
    ("habitacion1", "Patio", 6),
    ("habitacion1", "Baño1", 2),
    
    # habitacion2 - 3 aristas
    ("habitacion2", "Terraza", 4),
    ("habitacion2", "Cochera", 8),
    ("habitacion2", "Baño2", 3),
    
    # SaladeEstar - 3 aristas
    ("SaladeEstar", "Patio", 5),
    ("SaladeEstar", "Terraza", 3),
    ("SaladeEstar", "Comedor", 2),
    
    # Terraza - 3 aristas
    ("Terraza", "Patio", 4),
    ("Terraza", "Quincho", 4),
    ("Terraza", "Comedor", 6),
    
    # Patio - 3 aristas
    ("Patio", "Quincho", 6),
    ("Patio", "Cochera", 12),
    ("Patio", "Terraza", 4)
]

for origen, destino, distancia in conexiones:
    Casa.insert_edge(origen, destino, distancia)

def arbolExpansion(grafo, vertice):
    tree = grafo.kruskal(vertice)
    
    peso_total = 0
    for edge in tree.split(';'):
        origin, destination, weight = edge.split('-')
        peso_total += int(weight)
        print(f'Metros de cable que se necesitan: {peso_total}')


def Habitacion1_sala(grafo):

    habits = ["habitacion1"]
    resultados = {}   
    
    for habit in habits:
        path = grafo.dijkstra(habit) #todos los caminos mas cortos a pc
        destination = 'SaladeEstar'
        peso_total = None
        camino_completo = []
        
        while path.size() > 0: #mientras que el path tenga algo, hace un pop al value
            value = path.pop()
            if value[0] == destination:
                if peso_total is None:
                    peso_total = value[1]
                camino_completo.append(value[0])
                destination = value[2]
        
        camino_completo.reverse()

        resultados[habit] = {
            "camino": camino_completo,
            "distancia": f"{peso_total} metros para conectar el router al Smart TV" if peso_total is not None and peso_total != math.inf else math.inf
        }
    
    return resultados


print(arbolExpansion(Casa, "Cocina"))
print(Habitacion1_sala(Casa))