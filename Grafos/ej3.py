from graph import Graph
import math

puertos = Graph(is_directed=False)

puertitos = ["Madero", "Rodas", "C", "D", "E"]

for puersos in puertitos:
    puertos.insert_vertex(puersos)

conexiones = [ ("Madero", "C", 5), ("E", "D", 10), ("E", "C", 2), ("E", "Rodas", 7)]

for origen, destino, distancia in conexiones:
    puertos.insert_edge(origen, destino, distancia)


def barridos_primerpuerto(grafo, puerto):
    grafo.deep_sweep(puerto)



def MaderoaRodas(grafo):
    path = grafo.dijkstra('Madero') 
    destination = 'Rodas'
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
    
    resultados['Madero'] = {
        "camino": camino_completo,
        "distancia": peso_total if peso_total is not None and peso_total != math.inf else math.inf
    }
    
    return resultados


def Eliminarvertices_con_mas_aristasNodirigido(grafo):
    if not grafo:
        return False
    
    max_aristas = 0
    vertices_max = [] #lista de vertices con mas cantidad de aristas
    
    # Usar el diccionario de adyacencias que ya tienes
    conexiones_actuales = [("Madero", "C", 5), ("E", "D", 10), ("E", "C", 2), ("E", "Rodas", 7)]
    arreglo = {}
    
    # Crear el diccionario de adyacencias
    for origen, destino, _ in conexiones_actuales:
        if origen not in arreglo:
            arreglo[origen] = []
        arreglo[origen].append(destino)
        
        # Para grafo no dirigido, contar también las inversas
        if destino not in arreglo:
            arreglo[destino] = []
        arreglo[destino].append(origen)
    
    # Encontrar vértices con más aristas
    for vertice, aristas in arreglo.items():
        cantidad_aristas = len(aristas)
        
        if cantidad_aristas > max_aristas:
            max_aristas = cantidad_aristas
            vertices_max = [vertice]
        elif cantidad_aristas == max_aristas and vertice not in vertices_max:
            vertices_max.append(vertice)
    
    # Eliminar los vértices del grafo
    for vertice in vertices_max:
        grafo.delete_vertex(vertice)

    return f"El puerto: {vertices_max}, fue eliminado al tener la mayor cantidad de aristas ({max_aristas})"



barridos_primerpuerto(puertos, "Madero")
print(MaderoaRodas(puertos))
print(Eliminarvertices_con_mas_aristasNodirigido(puertos))