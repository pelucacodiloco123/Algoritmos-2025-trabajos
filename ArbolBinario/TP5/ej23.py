from tree import BinaryTree
from collections import Counter

class Criatura:

    def __init__(self, nombre, derrotado_por=None, descripcion="", capturada=None):
        self.nombre = nombre               
        self.derrotado_por = derrotado_por
        self.descripcion = descripcion 
        self.capturada = capturada         

    def __str__(self):
        return (f'Criatura: {self.nombre} | '
                f'Derrotado por: {self.derrotado_por} | '
                f'Capturada: {self.capturada} | '
                f'Descripción: {self.descripcion}')

criaturas = [
    Criatura("Ceto", derrotado_por=None, descripcion="Diosa primordial del mar, madre de monstruos marinos.", capturada=None),
    Criatura("Tifón", derrotado_por="Zeus", descripcion="Gigante con forma de serpiente que intentó destronar a Zeus.", capturada=None),
    Criatura("Equidna", derrotado_por="Argos Panoptes", descripcion="Ser mitad mujer, mitad serpiente.", capturada=None),
    Criatura("Dino", derrotado_por=None, descripcion="Monstruo marino hija de Forcis y Ceto.", capturada=None),
    Criatura("Pefredo", derrotado_por=None, descripcion="Una de las Grayas, hermanas que compartían un ojo y un diente.", capturada=None),
    Criatura("Enio", derrotado_por=None, descripcion="Otra de las Grayas, asociada con la guerra.", capturada=None),
    Criatura("Escila", derrotado_por=None, descripcion="Monstruo marino que devoraba marineros.", capturada=None),
    Criatura("Caribdis", derrotado_por=None, descripcion="Monstruo marino que tragaba enormes cantidades de agua.", capturada=None),
    Criatura("Euríale", derrotado_por=None, descripcion="Una de las Gorgonas.", capturada=None),
    Criatura("Esteno", derrotado_por=None, descripcion="Otra de las Gorgonas.", capturada=None),
    Criatura("Medusa", derrotado_por="Perseo", descripcion="La única mortal de las Gorgonas.", capturada=None),
    Criatura("Ladón", derrotado_por="Heracles", descripcion="Dragón guardián de las manzanas de oro.", capturada=None),
    Criatura("Águila del Cáucaso", derrotado_por=None, descripcion="Ave que devoraba el hígado de Prometeo.", capturada=None),
    Criatura("Quimera", derrotado_por="Belerofonte", descripcion="Monstruo con cabeza de león, cuerpo de cabra y cola de serpiente.", capturada=None),
    Criatura("Hidra de Lerna", derrotado_por="Heracles", descripcion="Monstruo acuático de múltiples cabezas.", capturada="Heracles"),
    Criatura("León de Nemea", derrotado_por="Heracles", descripcion="León invulnerable derrotado por Heracles.", capturada="Heracles"),
    Criatura("Esfinge", derrotado_por="Edipo", descripcion="Criatura con cuerpo de león y rostro de mujer.", capturada=None),
    Criatura("Cerda de Cromión", derrotado_por="Teseo", descripcion="Una cerda salvaje, hija de Tifón y Equidna.", capturada=None),
    Criatura("Ortro", derrotado_por="Heracles", descripcion="Un perro de dos cabezas, hermano de Cerbero.", capturada=None),
    Criatura("Toro de Creta", derrotado_por="Teseo", descripcion="Un toro blanco que Poseidón envió al rey Minos.", capturada=None),
    Criatura("Jabalí de Calidón", derrotado_por="Atalanta", descripcion="Un jabalí monstruoso enviado por Artemisa para castigar al rey Eneo.", capturada=None),
    Criatura("Carcinos", derrotado_por=None, descripcion="Un enorme cangrejo que atacó a Heracles.", capturada=None),
    Criatura("Gerión", derrotado_por="Heracles", descripcion="Un gigante de tres cuerpos, tres cabezas y seis brazos.", capturada=None),
    Criatura("Cloto", derrotado_por=None, descripcion="Una de las Moiras, las diosas del destino. Hilaba el hilo de la vida.", capturada=None),
    Criatura("Láquesis", derrotado_por=None, descripcion="Otra de las Moiras. Medía el hilo de la vida.", capturada=None),
    Criatura("Átropos", derrotado_por=None, descripcion="La tercera de las Moiras. Cortaba el hilo de la vida.", capturada=None),
    Criatura("Minotauro de Creta", derrotado_por="Teseo", descripcion="Criatura con cabeza de toro y cuerpo de hombre.", capturada=None),
    Criatura("Harpías", derrotado_por=None, descripcion="Criaturas mitad mujer, mitad pájaro, que robaban comida y castigaban a los malvados.", capturada=None),
    Criatura("Argos Panoptes", derrotado_por="Hermes", descripcion="Dios mensajero, protector de los viajeros y los ladrones.", capturada=None),
    Criatura("Aves del Estínfalo", derrotado_por=None, descripcion="Aves con picos de bronce y plumas metálicas que lanzaban como flechas.", capturada=None),
    Criatura("Talos", derrotado_por="Medea", descripcion="Un gigante de bronce, guardián de la isla de Creta.", capturada=None),
    Criatura("Sirenas", derrotado_por=None, descripcion="Criaturas mitad mujer, mitad ave, que atraían a los marineros con su canto.", capturada=None),
    Criatura("Pitón", derrotado_por="Apolo", descripcion="Una gran serpiente o dragón que vivía cerca del oráculo de Delfos.", capturada=None),
    Criatura("Cierva Cerinea", derrotado_por=None, descripcion="Una cierva con pezuñas de bronce y astas de oro, sagrada para Artemisa.", capturada=None),
    Criatura("Basilisco", derrotado_por=None, descripcion="Una criatura mítica, a menudo un reptil, con un aliento o mirada letal.", capturada=None),
    Criatura("Jabalí de Erimanto", derrotado_por=None, descripcion="Un jabalí salvaje que aterrorizaba una región del Peloponeso.", capturada=None),
    Criatura("Dragón de la Cólquida", derrotado_por=None, descripcion="Un dragón que custodiaba el Vellocino de Oro en la Cólquide.", capturada=None),
    Criatura("Cerbero", derrotado_por=None, descripcion="El perro de tres cabezas que guardaba la entrada al inframundo.", capturada=None)
]

arbol_criaturas = BinaryTree()

def cargar_criaturas(arbol, criaturas):
    for criatu in criaturas:
        arbol.insert(criatu.nombre, criatu)


def listar_creaturas(arbol):
    criaturas = []
    def inOrder(nodo):
        if nodo is not None:
            inOrder(nodo.left)
            criaturas.append((nodo.value, nodo.other_values.derrotado_por))

            inOrder(nodo.right)

    if arbol.root is not None:
        inOrder(arbol.root)

    return criaturas

def cargar_descripcion(arbol, nombre, descripcion):
    nodo = arbol.search(nombre)
    if nodo is not None:
        nodo.other_values.descripcion = descripcion
        print(f"Descripción de {nombre} actualizada.")
    else:
        print(f"No se encontró la criatura {nombre}.")  

def mostrar_info_talos(arbol):
    nodo = arbol.search("Talos")
    if nodo is not None:
        personaje = nodo.other_values
        print(personaje)
    else:
        print("Talos no se encontró en el árbol.") 


def top3_derrotadores(arbol):
    derrotadores_count = Counter()

    def inOrder(nodo):
        if nodo is not None:
            inOrder(nodo.left)
            criatura = nodo.other_values
            if criatura.derrotado_por is not None:
                derrotadores_count[criatura.derrotado_por] += 1
            inOrder(nodo.right)

    if arbol.root is not None:
        inOrder(arbol.root)


    return derrotadores_count.most_common(3)

# def ranking(arbol, ranking_result): (Otra forma de realizarlo (la dada en clase))
#     def __ranking(node, ranking_result):
#         if node is not None:
#             __ranking(node.left, ranking_result)
#             criatura = node.other_values
#             if criatura.derrotado_por is not None:
#                 heroe = criatura.derrotado_por
#                 if heroe not in ranking_result:
#                     ranking_result[heroe] = 1
#                 else:
#                     ranking_result[heroe] += 1
#             __ranking(node.right, ranking_result)

#     if arbol.root is not None:
#         __ranking(arbol.root, ranking_result)

        
def ordenar_ranking(item):
    return item[1]


        
def ordenar_ranking(item):
    return item[1]



def listar_criaturas_Heracles(arbol):
    criaturas = []
    def inOrder(nodo):
        if nodo is not None:
            inOrder(nodo.left)
            if nodo.other_values.derrotado_por == "Heracles":
                criaturas.append(nodo.value)
            inOrder(nodo.right)

    if arbol.root is not None:
        inOrder(arbol.root)

    return criaturas

def listar_criaturas_noderrotadas(arbol):
    criaturas = []
    def inOrder(nodo):
        if nodo is not None:
            inOrder(nodo.left)
            if nodo.other_values.derrotado_por == None:
                criaturas.append(nodo.value)
            inOrder(nodo.right)

    if arbol.root is not None:
        inOrder(arbol.root)

    return criaturas


def modificar_captura_Heracles(arbol):
    def inOrder(nodo):
        if nodo is not None:
            inOrder(nodo.left)
            if nodo.value in ["Cerbero", "Toro de Creta", "Cierva Cerinea", "Jabalí de Erimanto"]:
                nodo.other_values.capturada = "Heracles"
            inOrder(nodo.right)

    if arbol.root is not None:
        inOrder(arbol.root)

def busqueda_por_coincidencia(arbol, valor):
    print(f"Búsqueda por coincidencia para '{valor}':")
    arbol.proximity_search(valor)


def delete_basilisco_Sirenas(arbol):
    def inOrder(nodo):
        if nodo is not None:
            inOrder(nodo.left)
            if nodo.value in ["Basilisco", "Sirenas"]:
                arbol.delete(nodo.value)
            inOrder(nodo.right)

    if arbol.root is not None:
        inOrder(arbol.root)


def aves_heracles(arbol):
     def inOrder(nodo):
        if nodo is not None:
            inOrder(nodo.left)
            if nodo.value == "Aves del Estínfalo":
                nodo.other_values.derrotado_por = "Heracles"
                print(f"{nodo.other_values.descripcion} Ademas, Heracles derroto a varias de ellas.")
            inOrder(nodo.right)
   
     if arbol.root is not None:
         inOrder(arbol.root)

def dragon_ladon(arbol):
     def inOrder(nodo):
        if nodo is not None:
            inOrder(nodo.left)
            if nodo.value == "Ladón":
                nodo.value = "Dragón Ladón"
            inOrder(nodo.right)
   
     if arbol.root is not None:
         inOrder(arbol.root)

def captura_heracles(arbol):
     criaturas = []
     def inOrder(nodo):
        if nodo is not None:
            inOrder(nodo.left)
            if nodo.other_values.capturada == "Heracles":
                criaturas.append(nodo.value)
            inOrder(nodo.right)
   
     if arbol.root is not None:
         inOrder(arbol.root)
         
     return criaturas


cargar_criaturas(arbol_criaturas, criaturas)
listar_creaturas(arbol_criaturas)
cargar_descripcion(arbol_criaturas,"Jabalí de Calidón", "Sale asadito?")
mostrar_info_talos(arbol_criaturas)
top3_derrotadores(arbol_criaturas)
listar_criaturas_Heracles(arbol_criaturas)
listar_criaturas_noderrotadas(arbol_criaturas)
modificar_captura_Heracles(arbol_criaturas)
busqueda_por_coincidencia(arbol_criaturas, "Jabalí")
delete_basilisco_Sirenas(arbol_criaturas)
aves_heracles(arbol_criaturas)
dragon_ladon(arbol_criaturas)
arbol_criaturas.by_level()
captura_heracles(arbol_criaturas)

# Otra forma de hacer el ranking con la funcion dada en clase:
# ranking_result = {}
# ranking(arbol_criaturas, ranking_result)
# list_ranking = list(ranking_result.items())
# list_ranking.sort(key=ordenar_ranking, reverse=True)
# print(list_ranking[:3])