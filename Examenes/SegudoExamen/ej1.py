from tree import BinaryTree
from collections import Counter

class Pokemon:
    def __init__(self, nombre, debilidad="", megaevolucion= bool, numero="", tipos=[], gigamax=bool):
        self.nombre = nombre               
        self.numero = numero
        self.tipos = tipos 
        self.megaevolucion = megaevolucion  
        self.gigamax = gigamax
        self.debilidad = debilidad       

    def __str__(self):
        return (f'Nombre: {self.nombre} | '
                f'numero: {self.numero} | '
                f'debilidad: {self.debilidad} | '
                f'Megaevolucion: {self.megaevolucion} | '
                f'gigamax: {self.gigamax}'
                f'tipos: {self.tipos}')
    

arbol_por_nombre = BinaryTree()
arbol_por_numero = BinaryTree()
arbol_por_tipo = BinaryTree()


pokemones = [
    Pokemon("Pikachu", "Tierra", False, "025", ["Electrico"], False),
    Pokemon("Charizard", "Agua", True, "006", ["Fuego", "Volador"], True),
    Pokemon("Bulbasaur", "Fuego", False, "001", ["Planta", "Veneno"], False),
    Pokemon("Squirtle", "Planta", False, "007", ["Agua"], False),
    Pokemon("Jigglypuff", "Acero", False, "039", ["Normal", "Hada"], False),
    Pokemon("Gengar", "Psíquico", True, "094", ["Fantasma", "Veneno"], False),
    Pokemon("Eevee", "Lucha", False, "133", ["Normal"], True),
    Pokemon("Snorlax", "Lucha", False, "143", ["Normal"], False),
    Pokemon("Mewtwo", "Fantasma", True, "150", ["Psíquico"], False),
    Pokemon("Lucario", "Fuego", True, "448", ["Lucha", "Acero"], False),
    Pokemon("Garchomp", "Hielo", True, "445", ["Dragon", "Tierra"], False),
    Pokemon("Greninja", "Electrico", False, "658", ["Agua", "Siniestro"], False),
    Pokemon("Mimikyu", "Acero", False, "778", ["Fantasma", "Hada"], False),
    Pokemon("Tyranitar", "Lucha", False, "248", ["Roca", "Siniestro"], False),
    Pokemon("Scizor", "Fuego", True, "212", ["Bicho", "Acero"], False),
    Pokemon("Blaziken", "Volador", True, "257", ["Fuego", "Lucha"], False),
    Pokemon("Gardevoir", "Acero", True, "282", ["Psíquico", "Hada"], False),
    Pokemon("Metagross", "Fuego", True, "376", ["Acero", "Psíquico"], False),
    Pokemon("Gyarados", "Electrico", True, "130", ["Agua", "Volador"], False),
    Pokemon("Dragonite", "Hielo", False, "149", ["Dragon", "Volador"], False),
    Pokemon("Jolteon", "Tierra", False, "135", ["Electrico"], False),
    Pokemon("Lycanroc", "Lucha", False, "745", ["Roca"], False),
    Pokemon("Tyrantrum", "Hielo", False, "697", ["Roca", "Dragon"], False),
    Pokemon("Chandelure", "Agua", False, "609", ["Fantasma", "Fuego"], False),
    Pokemon("Magnezone", "Tierra", False, "462", ["Electrico", "Acero"], False)
]
def cargar_pokemon(arbol, pokemones):
    for pokemon in pokemones:
        if arbol == arbol_por_nombre:
            arbol.insert(pokemon.nombre, pokemon)
        elif arbol == arbol_por_numero:
            arbol.insert(pokemon.numero, pokemon)
        elif arbol == arbol_por_tipo:
            for tipo in pokemon.tipos:
                arbol.insert(tipo, pokemon)


def buscarporNum(tree, num):
    resultado = []
    if tree == arbol_por_numero:
        nodo1 = tree.search(num)
        if nodo1:
            resultado.append((nodo1.value, str(nodo1.other_values)))
        else: print("No usaste el arbol por numero")
    return resultado

def busqueda_por_coincidencia(arbol, nombre):
    print(f"Búsqueda por coincidencia para '{nombre}':")
    if arbol == arbol_por_nombre:
        arbol.proximity_search(nombre)
    else:
        print("No usaste el arbol por nombre")


def buscar_por_tipo(arbol, tipo):
    resultado = []
    if arbol == arbol_por_tipo:
        nodo1 = arbol.search(tipo)
        if nodo1:
            resultado.append((nodo1.value, str(nodo1.other_values)))
        else: print("No usaste el arbol por tipo")
    return resultado

def listar_pokemones_asc(arbol):
    print("Listado ascendente:")
    arbol.in_order()

def listar_pokemones_by_level(arbol):
    print("Listado por nivel:")
    arbol.by_level()


def mostrardebilesJolteonLycanrocTyrantrum(arbol):
    pokemones = []

    debilidades = ["Electrico","Roca", "Dragón"]

    def inOrder(nodo):
        if nodo is not None:
            inOrder(nodo.left)
            if nodo.other_values.debilidad in debilidades:
                pokemones.append(nodo.other_values.nombre)
            inOrder(nodo.right)

    if arbol.root is not None:
        inOrder(arbol.root)

    return pokemones


def contadortipos(arbol):
    tipos_count = Counter()

    def inOrder(nodo):
        if nodo is not None and arbol == arbol_por_tipo:
            inOrder(nodo.left)
            if nodo.value is not None:
                tipos_count[nodo.value] += 1
            inOrder(nodo.right)

    if arbol.root is not None:
        inOrder(arbol.root)
    return tipos_count

def mostrarmegaevolucion(arbol):
    pokemones = []

    def inOrder(nodo):
        if nodo is not None:
            inOrder(nodo.left)
            if nodo.other_values.megaevolucion is True:
                pokemones.append(nodo.other_values.nombre)
            inOrder(nodo.right)

    if arbol.root is not None:
        inOrder(arbol.root)

    return pokemones

def mostrargigamax(arbol):
    pokemones = []

    def inOrder(nodo):
        if nodo is not None:
            inOrder(nodo.left)
            if nodo.other_values.gigamax is True:
                pokemones.append(nodo.other_values.nombre)
            inOrder(nodo.right)

    if arbol.root is not None:
        inOrder(arbol.root)

    return pokemones



cargar_pokemon(arbol_por_nombre, pokemones)
cargar_pokemon(arbol_por_numero, pokemones)
cargar_pokemon(arbol_por_tipo, pokemones)


print(buscarporNum(arbol_por_numero, "149"))
busqueda_por_coincidencia(arbol_por_nombre, "Pika")
print(buscar_por_tipo(arbol_por_tipo, "Electrico"))
print(buscar_por_tipo(arbol_por_tipo, "Fuego"))
print(buscar_por_tipo(arbol_por_tipo, "Acero"))
print(buscar_por_tipo(arbol_por_tipo, "Fantasma"))
(listar_pokemones_asc(arbol_por_nombre))
(listar_pokemones_asc(arbol_por_numero))
(listar_pokemones_by_level(arbol_por_nombre))
print(mostrardebilesJolteonLycanrocTyrantrum(arbol_por_nombre))
print(contadortipos(arbol_por_tipo))
print(mostrarmegaevolucion(arbol_por_nombre))
print(mostrargigamax(arbol_por_nombre))