from graph import Graph
import math


grafo_star_wars = Graph(is_directed=False)

personajes = [
    "C3PO", "Yoda", "Leia", "Luke Skywalker", "Darth Vader", 
    "Boba Fett", "Rey", "Kylo Ren", "Chewbacca", "Han Solo", 
    "R2D2", "BB8"
]

for personaje in personajes:
    grafo_star_wars.insert_vertex(personaje)


grafo_star_wars.insert_edge("C3PO", "R2D2", 9)
grafo_star_wars.insert_edge("C3PO", "Luke Skywalker", 5)
grafo_star_wars.insert_edge("C3PO", "Leia", 6)
grafo_star_wars.insert_edge("C3PO", "Han Solo", 4)

grafo_star_wars.insert_edge("R2D2", "Luke Skywalker", 8)
grafo_star_wars.insert_edge("R2D2", "Leia", 7)
grafo_star_wars.insert_edge("R2D2", "Yoda", 2)

grafo_star_wars.insert_edge("Yoda", "Luke Skywalker", 4)
grafo_star_wars.insert_edge("Yoda", "Darth Vader", 5)

grafo_star_wars.insert_edge("Luke Skywalker", "Leia", 9)
grafo_star_wars.insert_edge("Luke Skywalker", "Han Solo", 7)
grafo_star_wars.insert_edge("Luke Skywalker", "Darth Vader", 5)
grafo_star_wars.insert_edge("Luke Skywalker", "Chewbacca", 5)

grafo_star_wars.insert_edge("Han Solo", "Chewbacca", 9)
grafo_star_wars.insert_edge("Han Solo", "Leia", 8)

grafo_star_wars.insert_edge("Darth Vader", "Boba Fett", 3)

grafo_star_wars.insert_edge("Rey", "BB8", 6)
grafo_star_wars.insert_edge("Rey", "Chewbacca", 3)
grafo_star_wars.insert_edge("Rey", "Leia", 2)
grafo_star_wars.insert_edge("Rey", "Kylo Ren", 4)

grafo_star_wars.insert_edge("Kylo Ren", "Leia", 1)
grafo_star_wars.insert_edge("Kylo Ren", "Han Solo", 1)

grafo_star_wars.insert_edge("Chewbacca", "BB8", 2)


def arbolExpansion(arbol, vertice):
    tree = arbol.kruskal(vertice)
    peso_total = 0

    for edge in tree.split(';'):
        origin, destination, weight = edge.split('-')
        print(f"{origin}, {destination} (weight: {weight})")
        peso_total += int(weight)

    return peso_total

def max_episodios_compartidos(grafo):
    max_peso = 0
    pares_maximos = []

    for vertex in grafo:
        for edge in vertex.edges:
            peso = edge.weight

            if peso > max_peso:
                max_peso = peso
                pares_maximos = [(vertex.value, edge.value)]
            elif peso == max_peso:
                pares_maximos.append((vertex.value, edge.value))
    
    return max_peso, pares_maximos


def caminocorto(grafo, inicio, fin):
    path = grafo.dijkstra(inicio) 
    destination = fin
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
    
    resultados[inicio] = {
        "camino": camino_completo,
        "distancia": peso_total if peso_total is not None and peso_total != math.inf else math.inf
    }
    
    return resultados

def episodios9(grafo):
    personajes = []
    for vertex in grafo:
       for edge in vertex.edges:
           if edge.weight >= 9:
               personajes.append((vertex.value, edge.value))
    return personajes




print(arbolExpansion(grafo_star_wars, "C3PO"))
print(arbolExpansion(grafo_star_wars, "Yoda"))
print(arbolExpansion(grafo_star_wars, "Leia"))

print(max_episodios_compartidos(grafo_star_wars))

print(caminocorto(grafo_star_wars, "C3PO", "R2D2"))
print(caminocorto(grafo_star_wars, "Yoda", "Darth Vader"))
print(episodios9(grafo_star_wars))






