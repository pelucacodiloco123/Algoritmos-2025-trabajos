from graph import Graph
import math

red = Graph(is_directed=False)

# Insertar equipos con nombre que incluye tipo
red.insert_vertex("Red Hat", {"tipo": "notebook"})
red.insert_vertex("Debian", {"tipo": "notebook"})
red.insert_vertex("Arch", {"tipo": "notebook"})
red.insert_vertex("Manjaro", {"tipo": "pc"})
red.insert_vertex("Fedora", {"tipo": "pc"})
red.insert_vertex("Impresora", {"tipo": "impresora"})
red.insert_vertex("Guarani", {"tipo": "servidor"})
red.insert_vertex("Switch1", {"tipo": "switch"})
red.insert_vertex("Switch2", {"tipo": "switch"})
red.insert_vertex("MongoDB", {"tipo": "servidor"})
red.insert_vertex("Ubuntu", {"tipo": "pc"})
red.insert_vertex("Mint", {"tipo": "pc"})
red.insert_vertex("Router1", {"tipo": "router"})
red.insert_vertex("Router2", {"tipo": "router"})
red.insert_vertex("Router3", {"tipo": "router"})
red.insert_vertex("Parrot", {"tipo": "pc"})

conexiones = [
    ("Ubuntu", "Switch1", 18),
    ("Impresora", "Switch1", 22),
    ("Mint", "Switch1", 80),
    ("Debian", "Switch1", 17),
    ("Switch1", "Router1", 29),
    ("Router1", "Router2", 37),
    ("Router1", "Router3", 43),
    ("Router2", "Router3", 50),
    ("Router2", "Guarani", 9),
    ("Router2", "Red Hat", 25),
    ("Router3", "Switch2", 61),
    ("Switch2", "Fedora", 3),
    ("Switch2", "Arch", 56),
    ("Switch2", "Manjaro", 40),
    ("Switch2", "Parrot", 12),
    ("Switch2", "MongoDB", 5)
    ]


for origen, destino, peso in conexiones:
    red.insert_edge(origen, destino, peso)


def barridos_originales(grafo):
    notebooks = ["Red Hat", "Debian", "Arch"]
    
    for notebook in notebooks:
        grafo.deep_sweep(notebook)
        grafo.amplitude_sweep(notebook)
        
    return print("Barridos completados")



def obtener_caminos_impresora(grafo):

    pcs = ["Manjaro", "Red Hat", "Fedora"]    
    resultados = {}   
    
    for pc in pcs:
        path = grafo.dijkstra(pc) #todos los caminos mas cortos a pc
        destination = 'Impresora'
        peso_total = None
        camino_completo = []
        
        while path.size() > 0: #mientras que el path tenga algo, hace un pop al value
            value = path.pop()
            if value[0] == destination: #chequea hasta que sea la impresora
                if peso_total is None:
                    peso_total = value[1] #añade el peso
                camino_completo.append(value[0]) #añade la impresora al camino
                destination = value[2] #añade el predecesor de la impresora y vuelve a hacer esto
        
        camino_completo.reverse() #Lo inverte para que sea de pc a impresora

        resultados[pc] = { #Aca construye el camino
            "camino": camino_completo,
            "distancia": peso_total if peso_total is not None and peso_total != math.inf else math.inf
        }
    
    return resultados


def arbolExpansion(arbol, vertice):
    tree = arbol.kruskal(vertice)
    peso_total = 0
    arbolito = [] 

    for edge in tree.split(';'):
        origin, destination, weight = edge.split('-')
        print(f"Arista: {origin} - {destination}, Peso: {weight}")
        peso_total += int(weight)

    return peso_total


def obtener_caminos_Guarani(grafo):
    pcs = ["Manjaro", "Parrot", "Fedora", "Ubuntu", "Mint"]    
    pc_mas_cercana = None
    mejor_resultado = {}
    distancia_minima = math.inf
    
    for pc in pcs:
        path = grafo.dijkstra(pc)
        destination = 'Guarani'
        peso_total = None
        camino_completo = []
        
        while path.size() > 0:
            value = path.pop()
            if value[0] == destination: 
                if peso_total is None:
                    peso_total = value[1] 
                camino_completo.append(value[0])
                destination = value[2] 
        
        camino_completo.reverse()

        # Solo guardar si es la más cercana
        if peso_total is not None and peso_total < distancia_minima:
            distancia_minima = peso_total
            pc_mas_cercana = pc
            mejor_resultado = {
                pc: {
                    "camino": camino_completo,
                    "distancia": peso_total
                }
            }
    
    return mejor_resultado if pc_mas_cercana else False


def obtener_caminos_MongoDB(grafo):
    pcs = ["Ubuntu", "Mint"]    
    pc_mas_cercana = None
    mejor_resultado = {}
    distancia_minima = math.inf
    
    for pc in pcs:
        path = grafo.dijkstra(pc)
        destination = 'MongoDB'
        peso_total = None
        camino_completo = []
        
        while path.size() > 0:
            value = path.pop()
            if value[0] == destination: 
                if peso_total is None:
                    peso_total = value[1] 
                camino_completo.append(value[0])
                destination = value[2] 
        
        camino_completo.reverse()

        # Solo guardar si es la más cercana
        if peso_total is not None and peso_total < distancia_minima:
            distancia_minima = peso_total
            pc_mas_cercana = pc
            mejor_resultado = {
                pc: {
                    "camino": camino_completo,
                    "distancia": peso_total
                }
            }
    
    return mejor_resultado if pc_mas_cercana else False


def cambiar_ImpresoraYResolverB(red):
    red.delete_edge("Impresora", "Switch1")
    red.insert_edge("Impresora", "Router2", 22)

    notebooks = ["Red Hat", "Debian", "Arch"]
    
    for notebook in notebooks:
        red.deep_sweep(notebook)
        red.amplitude_sweep(notebook)


print(barridos_originales(red))
print(obtener_caminos_impresora(red))
print(arbolExpansion(red, "Impresora"))
print(obtener_caminos_Guarani(red))
print(obtener_caminos_MongoDB(red))
print(cambiar_ImpresoraYResolverB(red))
