from graph import Graph
from random import sample, choice, randint

Grafo = Graph(is_directed=True)

# Generar 15 números únicos entre 1 y 100
valores_unicos = sample(range(1, 101), 15)

# Insertar vértices con valores únicos
for valor in valores_unicos:
    Grafo.insert_vertex(valor)

# Insertar aristas
for i in range(30):
    origen = choice(valores_unicos)
    destino = choice(valores_unicos)
    peso = randint(1, 100)
    
    Grafo.insert_edge(origen, destino, peso)

def eliminar_aislados(grafo):
    eliminados = [] #lista de eliminados
    
    for vertice in grafo: #recorre todos los vertices
        # Si no tiene aristas salientes
        if len(vertice.edges) == 0:
            # Verificar que nadie apunte a él
            nadie_lo_apunta = True
            for otro in grafo: #recorre todos los vertices menos el vertice inicial
                if otro != vertice:
                    for arista in otro.edges:  #Para cada vértice otro, recorremos todas sus aristas.
                        if arista.value == vertice.value:  #Verificar si esta arista apunta al vértice actual
                            nadie_lo_apunta = False
                            break
                if not nadie_lo_apunta: #si le apuntan, entonces no es aislado
                    break
            
            if nadie_lo_apunta: #si no le apuntan, lo elimina y añade a la lista
                eliminados.append(vertice.value)
    
    for valor in eliminados: #elimina los valores de la lista dentro del grafo
        grafo.delete_vertex(valor)
    
    return eliminados

def vertices_con_mas_aristas(grafo):

    if not grafo:
        return False
    
    max_aristas = 0
    vertices_max = [] #lista de vertices con mas cantidad de aristas
    
    for vertice in grafo:
        cantidad_aristas = len(vertice.edges) #chequea la cantidad de aristas de un vertice
        
        if cantidad_aristas > max_aristas: #intercambia si el numero es mayor
            max_aristas = cantidad_aristas
            vertices_max = [vertice.value] #Pone el vertice en la lista
        elif cantidad_aristas == max_aristas and vertice.value not in vertices_max:
            vertices_max.append(vertice.value) #añade un vertice si tiene el mismo numero de aristas que el que esta en la lista
    
    return vertices_max, max_aristas

def vertices_con_mas_aristas_entrantes(grafo):
    if not grafo:
        return False
    
    # Contar aristas entrantes para cada vértice
    aristas_entrantes = {} #diccionario de {valor_vertice: cantidad_aristas_entrantes}.
    
    # Inicializar contadores
    for vertice in grafo:
        aristas_entrantes[vertice.value] = 0 #Recorremos todos los vértices del grafo y inicializamos sus contadores en 0. Por ejemplo, si tenemos vértices 1, 2, 3, el diccionario queda: {1: 0, 2: 0, 3: 0}.
    
    # Contar aristas entrantes
    for vertice in grafo: #doble bucle, uno de vertices y otros de aristas
        for arista in vertice.edges:
            if arista.value in aristas_entrantes: #Para cada arista, verificamos si el vértice destino (arista.value) existe en nuestro diccionario. Si existe, incrementamos su contador porque significa que recibe una arista entrante.
                aristas_entrantes[arista.value] += 1
    
    # Encontrar el máximo
    max_entrantes = max(aristas_entrantes.values()) #el que tenga mas aristas entrantes
    vertices_max = []

    for vertice, count in aristas_entrantes.items():
        if count == max_entrantes:  #compara todos
            vertices_max.append(vertice)
    
    return vertices_max, max_entrantes


def vertices_sin_salida(grafo):
    sin_salida = []
    
    for vertice in grafo:
        if len(vertice.edges) == 0:
            sin_salida.append(vertice.value)
    
    return sin_salida


def contar_vertices(grafo):
    return len(grafo) 


def vertices_con_ciclos_directos(grafo):
    vertices_con_ciclo = []
    
    for vertice in grafo:
        # Verificar si este vértice tiene una arista que apunta a sí mismo
        for arista in vertice.edges:
            if arista.value == vertice.value:
                vertices_con_ciclo.append(vertice.value)
                break  # Solo necesitamos encontrar una vez
    
    return vertices_con_ciclo

def arista_mas_larga(grafo):
    if not grafo:
        return False
    
    aristas_maximas = []
    peso_maximo = 0
    
    # Buscar el peso máximo
    for vertice in grafo:
        for arista in vertice.edges:
            if arista.weight > peso_maximo:
                peso_maximo = arista.weight
    
    # Recopilar todas las aristas con ese peso máximo
    for vertice in grafo:
        for arista in vertice.edges:
            if arista.weight == peso_maximo:
                aristas_maximas.append({
                    'origen': vertice.value,
                    'destino': arista.value,
                    'peso': arista.weight
                })
    
    return aristas_maximas

print(eliminar_aislados(Grafo))
print(vertices_con_mas_aristas(Grafo))
print(vertices_con_mas_aristas_entrantes(Grafo))
print(vertices_sin_salida(Grafo))
print(contar_vertices(Grafo))
print(vertices_con_ciclos_directos(Grafo))
print(arista_mas_larga(Grafo))