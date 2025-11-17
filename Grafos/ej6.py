from graph import Graph
import math

dioses = Graph(is_directed=True)

# Insertar vértices (dioses) con descripciones
dioses.insert_vertex("Urano", {"descripcion": "Dios primordial del cielo, padre de los Titanes"})
dioses.insert_vertex("Gea", {"descripcion": "Diosa primordial de la tierra, madre de los Titanes"})
dioses.insert_vertex("Cronos", {"descripcion": "Líder de los Titanes, dios del tiempo"})
dioses.insert_vertex("Rea", {"descripcion": "Titanide, hermana y esposa de Cronos"})
dioses.insert_vertex("Zeus", {"descripcion": "Rey de los dioses, dios del cielo y el trueno"})
dioses.insert_vertex("Hera", {"descripcion": "Reina de los dioses, diosa del matrimonio"})
dioses.insert_vertex("Poseidon", {"descripcion": "Dios de los mares, los terremotos y los caballos"})
dioses.insert_vertex("Hades", {"descripcion": "Dios del inframundo y los muertos"})
dioses.insert_vertex("Demeter", {"descripcion": "Diosa de la agricultura y las cosechas"})
dioses.insert_vertex("Hestia", {"descripcion": "Diosa del hogar y la familia"})
dioses.insert_vertex("Ares", {"descripcion": "Dios de la guerra y la violencia"})
dioses.insert_vertex("Atenea", {"descripcion": "Diosa de la sabiduría, la estrategia y la guerra justa"})
dioses.insert_vertex("Apolo", {"descripcion": "Dios de la luz, el sol, las artes y la medicina"})
dioses.insert_vertex("Artemisa", {"descripcion": "Diosa de la caza, la luna y la naturaleza"})
dioses.insert_vertex("Hefesto", {"descripcion": "Dios del fuego, la forja y los artesanos"})
dioses.insert_vertex("Afrodita", {"descripcion": "Diosa del amor, la belleza y el deseo"})
dioses.insert_vertex("Hermes", {"descripcion": "Dios mensajero, del comercio y los ladrones"})
dioses.insert_vertex("Dionisio", {"descripcion": "Dios del vino, la fiesta y el éxtasis"})
dioses.insert_vertex("Persefone", {"descripcion": "Reina del inframundo, diosa de la primavera"})
dioses.insert_vertex("Eros", {"descripcion": "Dios del amor romántico y la atracción"})

# Relaciones familiares (usando pesos numéricos para representar tipos de relación)
# 1 = padre/madre/hijo, 2 = hermano, 3 = pareja

relaciones = [
    # Relaciones de parentesco directo (peso 1)
    ("Urano", "Cronos", 1),           # Urano es padre de Cronos
    ("Gea", "Cronos", 1),             # Gea es madre de Cronos
    ("Cronos", "Zeus", 1),            # Cronos es padre de Zeus
    ("Rea", "Zeus", 1),               # Rea es madre de Zeus
    ("Cronos", "Hera", 1),            # Cronos es padre de Hera
    ("Rea", "Hera", 1),               # Rea es madre de Hera
    ("Cronos", "Poseidon", 1),        # Cronos es padre de Poseidon
    ("Rea", "Poseidon", 1),           # Rea es madre de Poseidon
    ("Cronos", "Hades", 1),           # Cronos es padre de Hades
    ("Rea", "Hades", 1),              # Rea es madre de Hades
    ("Cronos", "Demeter", 1),         # Cronos es padre de Demeter
    ("Rea", "Demeter", 1),            # Rea es madre de Demeter
    ("Cronos", "Hestia", 1),          # Cronos es padre de Hestia
    ("Rea", "Hestia", 1),             # Rea es madre de Hestia
    
    # Relaciones entre hermanos (peso 2)
    ("Zeus", "Hera", 2),              # Zeus y Hera son hermanos
    ("Zeus", "Poseidon", 2),          # Zeus y Poseidon son hermanos
    ("Zeus", "Hades", 2),             # Zeus y Hades son hermanos
    ("Zeus", "Demeter", 2),           # Zeus y Demeter son hermanos
    ("Zeus", "Hestia", 2),            # Zeus y Hestia son hermanos
    ("Hera", "Poseidon", 2),          # Hera y Poseidon son hermanos
    ("Hera", "Hades", 2),             # Hera y Hades son hermanos
    ("Poseidon", "Hades", 2),         # Poseidon y Hades son hermanos
    
    # Relaciones de pareja (peso 3)
    ("Urano", "Gea", 3),              # Urano y Gea son pareja
    ("Cronos", "Rea", 3),             # Cronos y Rea son pareja
    ("Zeus", "Hera", 3),              # Zeus y Hera son pareja (también hermanos)
    ("Zeus", "Demeter", 3),           # Zeus y Demeter fueron pareja
    ("Hades", "Persefone", 3),        # Hades y Persefone son pareja
    ("Ares", "Afrodita", 3),          # Ares y Afrodita son pareja
    ("Hefesto", "Afrodita", 3),       # Hefesto y Afrodita fueron pareja
    
    # Relaciones padre-hijo de Zeus (peso 1)
    ("Zeus", "Ares", 1),              # Zeus es padre de Ares
    ("Hera", "Ares", 1),              # Hera es madre de Ares
    ("Zeus", "Atenea", 1),            # Zeus es padre de Atenea
    ("Zeus", "Apolo", 1),             # Zeus es padre de Apolo
    ("Zeus", "Artemisa", 1),          # Zeus es padre de Artemisa
    ("Zeus", "Hefesto", 1),           # Zeus es padre de Hefesto
    ("Hera", "Hefesto", 1),           # Hera es madre de Hefesto
    ("Zeus", "Hermes", 1),            # Zeus es padre de Hermes
    ("Zeus", "Dionisio", 1),          # Zeus es padre de Dionisio
    ("Zeus", "Persefone", 1),         # Zeus es padre de Persefone
    ("Demeter", "Persefone", 1),      # Demeter es madre de Persefone
    ("Ares", "Eros", 1),              # Ares es padre de Eros
    ("Afrodita", "Eros", 1),          # Afrodita es madre de Eros
    
    # Relaciones entre hermanos hijos de Zeus (peso 2)
    ("Ares", "Atenea", 2),            # Ares y Atenea son hermanos
    ("Ares", "Apolo", 2),             # Ares y Apolo son hermanos
    ("Ares", "Artemisa", 2),          # Ares y Artemisa son hermanos
    ("Atenea", "Apolo", 2),           # Atenea y Apolo son hermanos
    ("Atenea", "Artemisa", 2),        # Atenea y Artemisa son hermanos
    ("Apolo", "Artemisa", 2),         # Apolo y Artemisa son hermanos gemelos
    ("Hermes", "Dionisio", 2),        # Hermes y Dionisio son hermanos
]

# Insertar todas las relaciones en el grafo
for origen, destino, peso in relaciones:
    dioses.insert_edge(origen, destino, peso)


def mostrarHijos(grafo, nombre_dios):
    for nodo in grafo:
        if nodo.value == nombre_dios:
            print(f"Hijos de {nombre_dios} ---")
            for edge in nodo.edges:
                if edge.weight == 1:
                    print(f"  - Hijo/a: {edge.value}")
            break 
    else:
        print(f"No se encontró al dios {nombre_dios}")


def mostrarinfo(grafo, nombre_dios):
    for nodo in grafo:
        if nodo.value == nombre_dios:  # ← ESTE ES EL CAMBIO CLAVE
            print(f"Nombre: {nodo.value}")
            print(f"Descripción: {nodo.other_values['descripcion']}")
            print("Relaciones:")
            for edge in nodo.edges:
                if edge.weight == 1:
                    print(f"  - Hijo/a: {edge.value}")
                elif edge.weight == 2:
                    print(f"  - Hermano/a: {edge.value}")
                elif edge.weight == 3:
                    print(f"  - Pareja: {edge.value}")
            break 
    else:
        print(f"No se encontró al dios {nombre_dios}")


def existe_relacion_directa(grafo, dios1, dios2):
    """Determina si existe relación directa entre dos dioses y muestra la relación"""
    pos1 = grafo.search(dios1, 'value')
    if pos1 is None:
        print(f"No se encontró al dios {dios1}")
        return False
    
    dios = grafo[pos1]
    relacion_encontrada = False
    
    # Buscar si dios2 está en las aristas de dios1
    for edge in dios.edges:
        if edge.value == dios2:
            relacion_encontrada = True
            if edge.weight == 1:
                print(f"Existe relación directa: {dios1} es padre/madre de {dios2}")
            elif edge.weight == 2:
                print(f"Existe relación directa: {dios1} y {dios2} son hermanos")
            elif edge.weight == 3:
                print(f"Existe relación directa: {dios1} y {dios2} son pareja")
            else:
                print(f"Existe relación directa: {dios1} -> {dios2} (tipo: {edge.weight})")
            break
    
    if not relacion_encontrada:
        # También verificar en el otro sentido (para grafos no dirigidos)
        pos2 = grafo.search(dios2, 'value')
        if pos2 is not None:
            dios_b = grafo[pos2]
            for edge in dios_b.edges:
                if edge.value == dios1:
                    relacion_encontrada = True
                    if edge.weight == 1:
                        print(f"Existe relación directa: {dios2} es padre/madre de {dios1}")
                    elif edge.weight == 2:
                        print(f"Existe relación directa: {dios1} y {dios2} son hermanos")
                    elif edge.weight == 3:
                        print(f" Existe relación directa: {dios1} y {dios2} son pareja")
                    else:
                        print(f"Existe relación directa: {dios2} -> {dios1} (tipo: {edge.weight})")
                    break
    
    if not relacion_encontrada:
        print(f"No existe relación directa entre {dios1} y {dios2}")
    
    return relacion_encontrada


def caminoDios(grafo, dios1, dios2):
    path = grafo.dijkstra(dios1) 
    destination = dios2
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
    
    resultados[dios1] = {
        "camino": camino_completo,
        "distancia": peso_total if peso_total is not None and peso_total != math.inf else math.inf
    }
    
    return resultados

def barridos(grafo):
    dios = ["Urano", "Gea", "Cronos", "Rea", "Zeus", "Hera", "Poseidon", "Hades", "Demeter", "Hestia", "Ares", "Atenea", "Apolo", "Artemisa", "Hefesto",  "Afrodita", "Hermes", "Dionisio", "Persefone", "Eros"]
    
    for diositos in dios:

        grafo.deep_sweep(diositos)
        grafo.amplitude_sweep(diositos)
        
    return print("Barridos completados")


def barridosMadre(grafo):
    dios = ["Urano", "Gea", "Cronos", "Rea", "Zeus", "Hera", "Poseidon", "Hades", "Demeter", "Hestia", "Ares", "Atenea", "Apolo", "Artemisa", "Hefesto",  "Afrodita", "Hermes", "Dionisio", "Persefone", "Eros"]
    
    for diositos in dios:
        # Encontrar madre
        madre = "No registrada"
        for otro_dios in grafo:
            if otro_dios.value != diositos:
                for edge in otro_dios.edges:
                    if edge.value == diositos and edge.weight == 1:
                        madre = otro_dios.value
                        break
        
        print(f"{diositos} (Madre: {madre})")
        grafo.deep_sweep(diositos)
        grafo.amplitude_sweep(diositos)
        
    return print("Barridos completados")


def mostrarAncestros(grafo, nombre_dios):
    """Muestra todos los ancestros de un dios específico"""
    ancestros = set()
    
    def buscar_ancestros(dios_actual, nivel=0):
        # Buscar padres del dios actual
        for otro_dios in grafo:
            if otro_dios.value != dios_actual:
                for edge in otro_dios.edges:
                    if edge.value == dios_actual and edge.weight == 1:
                        # Encontramos un padre/madre
                        ancestros.add(otro_dios.value)
                        # Buscar ancestros del padre/madre (recursivo)
                        buscar_ancestros(otro_dios.value, nivel + 1)
    
    # Iniciar búsqueda
    buscar_ancestros(nombre_dios)
    
    # Mostrar resultados
    if ancestros:
        print(f"Ancestros de {nombre_dios} ---")
        for ancestro in sorted(ancestros):
            print(f"{ancestro}")
        print(f"Total de ancestros: {len(ancestros)}")
    else:
        print(f"{nombre_dios} no tiene ancestros registrados")

# Ejemplos de uso
mostrarAncestros(dioses, "Zeus")
mostrarAncestros(dioses, "Ares")
mostrarAncestros(dioses, "Eros")



mostrarHijos(dioses, "Zeus")
mostrarinfo(dioses, "Zeus")
existe_relacion_directa(dioses, "Zeus", "Hera")
print(caminoDios(dioses, "Zeus", "Hera"))
barridos(dioses)
barridosMadre(dioses)
mostrarAncestros(dioses, "Zeus")