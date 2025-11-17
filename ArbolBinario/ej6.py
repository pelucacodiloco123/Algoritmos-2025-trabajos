# #Dado un archivo con todos los jedisnombre, de los que se cuenta con: nombre, especie, año de nacimiento,
# color de sable de luz, ranking (jedisnombre Master, jedisnombre Knight, Padawan) y maestro, los últimos
# tres campos pueden tener más de un valor. Escribir las funciones necesarias para resolver las
# siguientes consignas:

from tree import BinaryTree

class Jedi:
    def __init__(self, nombre, maestro="", colorsable="", especie="", anio="", ranking=""):
        self.nombre = nombre               
        self.especie = especie
        self.anio = anio 
        self.colorsable = colorsable  
        self.ranking = ranking
        self.maestro = maestro       

    def __str__(self):
        return (f'Nombre: {self.nombre} | '
                f'Especie: {self.especie} | '
                f'Maestro: {self.maestro} | '
                f'Color sable: {self.colorsable} | '
                f'Ranking: {self.ranking}')

# Crear los tres árboles
arbol_por_nombre = BinaryTree()
arbol_por_ranking = BinaryTree()
arbol_por_especie = BinaryTree()

jedis = [ 
    Jedi("Ahsoka Tano", maestro=["Anakin Skywalker"], colorsable=["Verde", "azul", "Amarillo", "blanco"], especie="Togruta", anio="36 ABY", ranking="Jedi Knight"),
    Jedi("Kit Fisto", maestro=["No se sabe"], colorsable=["Verde"], especie="Nautolano", anio="52 ABY", ranking="Jedi Master"),
    Jedi("Yoda", maestro=["N'Kata Del Gormo"], colorsable=["Verde"], especie="No se sabe", anio="896 ABY", ranking="Jedi Master"),
    Jedi("Luke Skywalker", maestro=["Obi-Wan Kenobi", "Yoda"], colorsable=["Azul", "Verde"], especie="Humano", anio="19 ABY", ranking="Jedi Master"),
    Jedi("Aayla Secura", maestro=["Quinlan Vos"], colorsable=["Azul"], especie="Twi'lek", anio="48 ABY", ranking="Jedi Knight"),
    Jedi("Mace Windu", maestro=["Cyslin Myr", "Yoda"], colorsable=["Violeta"], especie="Humano", anio="72 ABY", ranking="Jedi Master"),
    Jedi("Qui-Gon Jinn", maestro=["Dooku"], colorsable=["Verde"], especie="humano", anio="80 ABY", ranking="Jedi Master"),
    Jedi("Pong Krell", maestro=["No se sabe"], colorsable=["Verde", "Azul"], especie="Besalisko", anio="58 ABY", ranking="Jedi Master"),
    Jedi("Depa Billaba", maestro=["Mace Windu"], colorsable=["Verde", "Azul"], especie="Humano", anio="45 ABY", ranking="Jedi Master"),
    Jedi("Obi-Wan Kenobi", maestro=["Qui-Gon Jinn", "Yoda"], colorsable=["Azul"], especie="Humano", anio="57 ABY", ranking="Jedi Master"),
    Jedi("Anakin-Skywalker", maestro=["Obi-Wan Kenobi", "Darth Sidious"], colorsable=["Azul", "Rojo"], especie="Humano", anio="41 ABY", ranking="Jedi Knight"),
    Jedi("Finn Ertay", maestro=["No se sabe"], colorsable=["Azul"], especie="Twi'lek", anio="25 ABY", ranking="Padawan")
]

def cargar_jedis(arbol, jedis):
    for jedi in jedis:
        if arbol == arbol_por_nombre:
            arbol.insert(jedi.nombre, jedi)
        elif arbol == arbol_por_especie:
            # Clave única: especie + nombre
            clave_unica = f"{jedi.especie}-{jedi.nombre}"
            arbol.insert(clave_unica, jedi)
        elif arbol == arbol_por_ranking:
            arbol.insert(jedi.ranking, jedi)

def yodaYLuke(tree):
    resultado = []
    
    if tree == arbol_por_nombre:
        nodo1 = tree.search("Yoda")
        nodo2 = tree.search("Luke Skywalker")
        if nodo1:
            resultado.append((nodo1.value, str(nodo1.other_values)))
        if nodo2:
            resultado.append((nodo2.value, str(nodo2.other_values)))
            
    elif tree == arbol_por_especie:
        # Buscar por las claves únicas
        nodo1 = tree.search("No se sabe-Yoda")
        nodo2 = tree.search("Humano-Luke Skywalker")
        if nodo1:
            resultado.append((nodo1.value, str(nodo1.other_values)))
        if nodo2:
            resultado.append((nodo2.value, str(nodo2.other_values)))
        
    elif tree == arbol_por_ranking:
        def in_order_ranking(root):
            if root is not None:
                in_order_ranking(root.left)
                if root.other_values and root.other_values.nombre in ["Yoda", "Luke Skywalker"]:
                    resultado.append((root.value, str(root.other_values)))
                in_order_ranking(root.right)
        
        in_order_ranking(tree.root)
    
    return resultado

def listar_jedis_Master(arbol):
    jedis = []
    def inOrder(nodo):
        if nodo is not None and arbol != arbol_por_ranking:
            inOrder(nodo.left)
            if nodo.other_values.ranking== "Jedi Master":
                jedis.append(nodo.value)
            inOrder(nodo.right)
        elif nodo is not None:
            inOrder(nodo.left)
            if nodo.other_values.ranking== "Jedi Master":
                jedis.append(nodo.other_values.nombre)
            inOrder(nodo.right)

    if arbol.root is not None:
        inOrder(arbol.root)

    return jedis


def listar_jedis_colorsable(arbol):
    jedis = []
    def inOrder(nodo):
        if nodo is not None:
            inOrder(nodo.left)
            if "Verde" in nodo.other_values.colorsable:
                jedis.append(nodo.value)
            inOrder(nodo.right)

    if arbol.root is not None:
        inOrder(arbol.root)

    return jedis

def listar_jedis_con_maestro_en_lista(arbol):
    jedis_con_maestro = []
    nombres_jedis = [jedi.nombre for jedi in jedis]
    
    def in_order(nodo):
        if nodo is not None:
            in_order(nodo.left)
            jedi = nodo.other_values
            
            # Verificar si tiene maestros que estén en la lista
            if jedi.maestro:
                for maestro in jedi.maestro:
                    if maestro in nombres_jedis:
                        jedis_con_maestro.append(jedi.nombre)
                        break
            
            in_order(nodo.right)
    
    if arbol.root is not None:
        in_order(arbol.root)
    
    return jedis_con_maestro


def listar_jedis_TogruCerea(arbol):
    jedis = []
    def inOrder(nodo):
        if nodo is not None:
            inOrder(nodo.left)
            if nodo.other_values.especie in ["Togruta", "Cerean"]:
                jedis.append(nodo.value)
            inOrder(nodo.right)

    if arbol.root is not None:
        inOrder(arbol.root)
  
    return jedis

def listar_jedis_TogruCerea(arbol):
    jedis = []
    def inOrder(nodo):
        if nodo is not None:
            inOrder(nodo.left)
            if nodo.other_values.especie in ["Togruta", "Cerean"]:
                jedis.append(nodo.value)
            inOrder(nodo.right)

    if arbol.root is not None:
        inOrder(arbol.root)
  
    return jedis

def listar_jedis_Aguion(arbol):
    jedis = []
    def inOrder(nodo):
        if nodo is not None:
            inOrder(nodo.left)
            if nodo.other_values.nombre[0] == "A" and "-" in nodo.other_values.nombre:
                jedis.append(nodo.value)
            inOrder(nodo.right)

    if arbol.root is not None:
        inOrder(arbol.root)
  
    return jedis


cargar_jedis(arbol_por_nombre, jedis)
cargar_jedis(arbol_por_especie, jedis)
cargar_jedis(arbol_por_ranking, jedis)

print(listar_jedis_Aguion(arbol_por_nombre))