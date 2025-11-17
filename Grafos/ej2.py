from graph import Graph
import math

grafo = Graph(is_directed=True)
grafeishon = Graph(is_directed=False)

grafitis = ["A", "B", "C", "D", "E"]


def cargar(grafo, grafitis):
    for grafi in grafitis:
        grafo.insert_vertex(grafi)

conexiones = [("A","B", 0),
("A", "C", 0),
("A", "E", 0),
("B", "C", 0),
("C", "B", 0),
("C", "D", 0),
("E", "B", 0),
("E", "D", 0),
("D", "D", 0)]

conexiones_con_pesos = [
    ("A","B", 5),
    ("A", "C", 3), 
    ("A", "E", 7),
    ("B", "C", 2),
    ("C", "B", 4),
    ("C", "D", 6),
    ("E", "B", 1),
    ("E", "D", 8),
    ("D", "D", 9)
]

cargar(grafo, grafitis)
cargar(grafeishon, grafitis)

for origen, destino, distancia in conexiones:
    grafo.insert_edge(origen, destino, distancia)

for origen, destino, distancia in conexiones_con_pesos:
    grafeishon.insert_edge(origen, destino, distancia)


def arreglo_listas_adyacencias(conexiones):
    arreglo = {} #{vértice: [lista_de_vecinos]}
    for origen, destino, _ in conexiones: #Recorre cada conexión en la lista conexiones, Desempaqueta la tupla en tres variables: origen, destino, _
        if origen not in arreglo: #Verifica si el vértice origen ya existe como clave en el diccionario
            arreglo[origen] = [] #Crea una lista vacía para el vértice origen
        arreglo[origen].append(destino) #agrega el vértice destino a la lista de vecinos del vértice origen
    return arreglo

def lista_listas_adyacencia(conexiones):
    lista = []
    
    # Paso 1: Encontrar todos los vértices únicos manualmente
    vertices = []
    
    # Recorrer todas las conexiones para encontrar vértices origen
    for conexion in conexiones:
        origen = conexion[0]  # primer elemento de la tupla
        if origen not in vertices:
            vertices.append(origen)
    
    # Recorrer todas las conexiones para encontrar vértices destino
    for conexion in conexiones:
        destino = conexion[1]  # segundo elemento de la tupla
        if destino not in vertices:
            vertices.append(destino)
    
    # Paso 2: Ordenar los vértices
    vertices.sort()
    
    # Paso 3: Para cada vértice, encontrar sus vecinos
    for vertice in vertices:
        adyacentes = []
        
        # Buscar en todas las conexiones
        for conexion in conexiones:
            origen = conexion[0]
            destino = conexion[1]
            
            # Si el origen es igual al vértice actual, agregar el destino a adyacentes
            if origen == vertice:
                adyacentes.append(destino)
        
        # Paso 4: Agregar a la lista final
        lista.append([vertice, adyacentes])
    
    return lista

def arbolExpansion(grafo, vertice):
    tree = grafo.kruskal(vertice)
    
    peso_total = 0
    for edge in tree.split(';'): #Divide el string tree por el caracter ; y itera sobre cada elemento.
        origin, destination, weight = edge.split('-') #Divide cada edge por el caracter - y asigna origen, destination, weight
        peso_total += int(weight) #Convierte weight de string a entero y lo suma al acumulador peso_total.
    return {peso_total}

def agregararcoEC(grafo):
    grafo.insert_edge("E", "C", 0)


def CaminoAC(grafo):
    path = grafo.dijkstra('A') 
    destination = 'C'
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
    
    resultados['A'] = {
        "camino": camino_completo,
        "distancia": peso_total if peso_total is not None and peso_total != math.inf else math.inf
    }
    
    return resultados

print(arreglo_listas_adyacencias(conexiones))
print(lista_listas_adyacencia(conexiones))
print(arbolExpansion(grafeishon, "A"))
agregararcoEC(grafo)
print(CaminoAC(grafo))

