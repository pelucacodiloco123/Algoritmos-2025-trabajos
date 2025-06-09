from list_ import List
from queue_ import Queue
from stack import Stack
from super_heroes_data import superheroes as data

def order_by_name(item):
    return item.name

class Superhero:
    def __init__(self, name, alias, real_name, short_bio, first_appearance, is_villain):
        self.name = name
        self.alias = alias
        self.real_name = real_name
        self.short_bio = short_bio
        self.first_appearance = first_appearance
        self.is_villain = is_villain

    def __str__(self):
        return f"{self.name}, {self.real_name} - {'Villano' if self.is_villain else 'Héroe'}"

list_superheroes = List()
list_superheroes.add_criterion('name', order_by_name)


for item in data:
    hero = Superhero(
        item['name'],
        item['alias'],
        item['real_name'],
        item['short_bio'],
        item['first_appearance'],
        item['is_villain']
    )
    list_superheroes.append(hero)

    list_superheroes.sort_by_criterion('name')  #consigna 1
    list_superheroes.show()

def Posicion_TheThing_Raccoon(list_superheroes): #consigna 2
 index = list_superheroes.search('The Thing', "name")
 index2 = list_superheroes.search('Rocket Raccoon', "name")

 return index, index2


def listar_villanos(value): #consigna 3
    resultado = []
    for item in value:
        if item.is_villain:
            resultado.append(item.name)
    return resultado


def listar_villanos1980(value): #consigna 4
    resultado = Queue()
    for item in value:
        if item.is_villain and item.first_appearance < 1980:
            resultado.arrive(item.name)
    return resultado



def letraBLMYW(value): #consigna 5
    resultados = []
    for item in value:
        if item.name.startswith(("Bl", "My", "W")) and not item.is_villain:
            resultados.append(item.name)
    return resultados


def order_by_real_name(item):
    return str(item.real_name) if item.real_name is not None else ""


list_superheroes.add_criterion('real name', order_by_real_name)

list_superheroes.sort_by_criterion('real name')  #consigna 6

def order_by_first_appearance(List_superheroes):
    return List_superheroes.first_appearance

list_superheroes.add_criterion('first appearance', order_by_first_appearance)

def order_by_first_appearance(item):
    return item.first_appearance

def lista_solo_heroes(list_superheroes): #consigna 7
    superheroe = List()
    superheroe.add_criterion("first_appearance", order_by_first_appearance)
    
    for item in list_superheroes:
        if not item.is_villain:
            superheroe.append(item)
             
    superheroe.sort_by_criterion("first_appearance")
    return superheroe


def Antman_cambiarnombrerealScottLang(list_superheroes): #consigna 8
    index = list_superheroes.search("Ant Man", "name")
    if index is not None:
        if list_superheroes[index].real_name != "Scott Lang":
            list_superheroes[index].real_name = "Scott Lang"
            print("Nombre real de Ant Man actualizado a Scott Lang.")
        else:
            print("El nombre real ya es Scott Lang.")
    else:
        print("Ant Man no está en la lista.")



def biografia_TimeTraveller_Suit(value): #consigna 9
    resultado = []
    for item in value:
        if "Time-Travelling" in item.short_bio or "Suit" in item.short_bio:
            resultado.append(item.name)
    return resultado

def eliminarymostrar_Electro_Baron(list_superheroes):  # consigna 10
    for nombre in ["Electro", "Baron Zemo"]:
        index = list_superheroes.search(nombre, "name")
        if index is not None:
            print(f"Datos de {nombre} antes de eliminar:")
            print(list_superheroes[index]) 
            list_superheroes.delete_value(nombre, "name")
            print(f"{nombre} eliminado.")
        else:
            print(f"{nombre} no estaba en la lista.")



list_superheroes.show()
print("Posición de 'The Thing' y 'Rocket Raccoon':", Posicion_TheThing_Raccoon(list_superheroes))
print("Villanos:", listar_villanos(list_superheroes))
print("Villanos de antes de 1980:", listar_villanos1980(list_superheroes))
print("Héroes que empiezan con Bl, My o W:", letraBLMYW(list_superheroes))
print("Listado de heroes ordenados por aparicion: ", (lista_solo_heroes(list_superheroes)).show())
Antman_cambiarnombrerealScottLang(list_superheroes)
eliminarymostrar_Electro_Baron(list_superheroes)
print(biografia_TimeTraveller_Suit(list_superheroes))


