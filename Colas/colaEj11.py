from queue_ import Queue

class personaje:
 def __init__(self,nombre,planeta):
    self.nombre=nombre
    self.planeta=planeta
 def __str__(self):
        return f"{self.nombre} - {self.planeta}"

personajes = Queue()

personajes.arrive(personaje("Han Solo", "Corellia"))
personajes.arrive(personaje("Luke Skywalker", "Tatooine"))
personajes.arrive(personaje("Leia Organa", "Aldeeran"))
personajes.arrive(personaje("Maestro Yoda", "Dagobah"))
personajes.arrive(personaje("Ewok", "Endor"))
personajes.arrive(personaje("Jar Jar Binks","Naboo"))
personajes.arrive(personaje("Anakin Skywalker", "Tatooine"))

def planetas(personajes):
    planetas_validos = ["Tatooine", "Aldeeran", "Endor"]
    cantidad = personajes.size()

    for i in range(cantidad):
        if personajes.on_front().planeta in planetas_validos:
            print(personajes.on_front().nombre)
        personajes.move_to_end()


def LukeHan(personajes):
    cantidad = personajes.size()

    for i in range(cantidad):
        if personajes.on_front().nombre == "Han Solo" or personajes.on_front().nombre == "Luke Skywalker":
            print(personajes.on_front().planeta)
        personajes.move_to_end()


def insertar_antes_de_yoda(personajes, nuevo_personaje):
    cantidad = personajes.size()
    encontrado = False

    for i in range(cantidad):
        if personajes.on_front().nombre == "Maestro Yoda":
            personajes.arrive(nuevo_personaje)
            personajes.arrive(personajes.attention())
            encontrado = True
            break
        else:
            personajes.move_to_end()

    if not encontrado:
        print("Yoda no estaba en la cola.")

    restante = cantidad - (i + 1)
    for j in range(restante):
        personajes.move_to_end()

    print("Cola después de insertar personaje delante de Yoda:")
    personajes.show()



def eliminarpersonaje(personajes):
    cantidad = personajes.size()
    encontrado = False

    for i in range(cantidad):
        if personajes.on_front().nombre == "Jar Jar Binks":
            personajes.move_to_end()
            personajes.attention()
            encontrado = True
            break
        else:
            personajes.move_to_end()

    if not encontrado:
        print("Jar Jar Binks no estaba en la cola.")
   
    return personajes

planetas(personajes)
LukeHan(personajes)
insertar_antes_de_yoda(personajes, ("Juan,caca"))
eliminarpersonaje(personajes)


