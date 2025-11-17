from graph import Graph
import math

grafo = Graph(is_directed=True)

grafo.insert_vertex("A")
grafo.insert_vertex("B")
grafo.insert_vertex("C")
grafo.insert_vertex("D")
grafo.insert_vertex("E")
grafo.insert_vertex("F")
grafo.insert_vertex("G")

conexiones = [
 ("A", "B", 15),
 ("A", "D", 13),
 ("C", "A", 19),
 ("C", "F", 9),
 ("F", "G", 3),
 ("C", "G", 27),
 ("C", "E", 5),
 ("B", "C", 2),
 ("B", "F", 12),
 ("B", "E", 20),
 ("E", "F", 1)]

for origen, destino, peso in conexiones:
    grafo.insert_edge(origen, destino, peso)

def barridos_ACF(grafo):
    letras = ["A", "C", "F"]
    
    for letra in letras:
        grafo.deep_sweep(letra)
        grafo.amplitude_sweep(letra)
        
    return print("Barridos completados")

def AhastaF(grafo):
    path = grafo.dijkstra('A') 
    destination = 'F'
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

def ChastaD(grafo):
    path = grafo.dijkstra('C') 
    destination = 'D'
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
    
    resultados['C'] = {
        "camino": camino_completo,
        "distancia": peso_total if peso_total is not None and peso_total != math.inf else math.inf
    }
    
    return resultados


def BhastaG(grafo):
    path = grafo.dijkstra('B') 
    destination = 'G'
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
    
    resultados['B'] = {
        "camino": camino_completo,
        "distancia": peso_total if peso_total is not None and peso_total != math.inf else math.inf
    }
    
    return resultados


def mostrar_matriz_adyacencia(grafo):
    # 1. Definir la lista de vértices en el orden que aparecerán en la matriz
    vertices = ["A", "B", "C", "D", "E", "F", "G"]
    
    # 2. Obtener el número total de vértices
    n = len(vertices)
    
    # 3. Crear matriz n x n inicializada con infinito (representa "sin conexión")
    matriz = [[math.inf] * n for _ in range(n)]
    
    # 4. Crear diccionario para mapear nombre de vértice -> índice numérico
    indice_vertice = {vertice: i for i, vertice in enumerate(vertices)}
    
    # 5. Recorrer cada vértice para llenar la matriz
    for i, vertice in enumerate(vertices):
        # 6. Buscar el objeto vértice en el grafo usando el valor "A", "B", etc.
        vertice_obj = grafo.search(vertice, 'value')
        
        # 7. Si el vértice existe en el grafo
        if vertice_obj is not None:
            # 8. Recorrer todas las aristas que salen de este vértice
            for edge in grafo[vertice_obj].edges:
                # 9. Obtener el índice del vértice destino en la matriz
                j = indice_vertice[edge.value]
                
                # 10. Asignar el peso de la arista en la posición [i][j] de la matriz
                matriz[i][j] = edge.weight
    
    # 11. Mostrar encabezado de la matriz con nombres de vértices
    print("Matriz de Adyacencia:")
    print("   " + "  ".join(vertices))
    
    # 12. Recorrer cada fila para mostrar la matriz formateada
    for i, vertice in enumerate(vertices):
        # 13. Convertir cada valor de la fila a string (∞ para infinito)
        fila = [f"{matriz[i][j]:2}" if matriz[i][j] != math.inf else " ∞" for j in range(len(vertices))]
        
        # 14. Mostrar la fila con el nombre del vértice al inicio
        print(f"{vertice}  " + "  ".join(fila))
    
    # 15. Retornar la matriz por si se quiere usar posteriormente
    return matriz


def aniadir(grafo):
    grafo.insert_edge("C", "A", 5)
    grafo.insert_edge("C", "B", 15)
    grafo.insert_edge("G", "D", 12)

barridos_ACF(grafo)
print(AhastaF(grafo))
print(ChastaD(grafo))
print(BhastaG(grafo))

aniadir(grafo)

barridos_ACF(grafo)
print(AhastaF(grafo))
print(ChastaD(grafo))
print(BhastaG(grafo))
mostrar_matriz_adyacencia(grafo)
