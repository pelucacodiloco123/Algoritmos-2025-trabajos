import stack

class Personaje:
    def __init__(self, nombre: str, peliculas: int):
        self.nombre = nombre
        self.peliculas = peliculas

    def __str__(self):
        return f"{self.nombre} - {self.peliculas}"


Marvel = stack.Stack()

Marvel.push(Personaje("Iron Man", 9))
Marvel.push(Personaje("Thor", 9))
Marvel.push(Personaje("Capitan America", 9))
Marvel.push(Personaje("Groot", 6))
Marvel.push(Personaje("Rocket Raccoon", 6))
Marvel.push(Personaje("Viuda Negra",9))

def buscar_GrootandRocket(pila: stack.Stack):
    aux = stack.Stack()
    posicionRocket = None
    posicionGroot = None
    posicion = 0  # posición desde la cima

    while pila.size() > 0:
        personaje = pila.pop()
        aux.push(personaje)

        if personaje.nombre == "Rocket Raccoon":
            posicionRocket = posicion
        elif personaje.nombre == "Groot":
            posicionGroot = posicion
        
        posicion += 1

    # Restaurar la pila original
    while aux.size() > 0:
        pila.push(aux.pop())

    print("Posición de Rocket Raccoon desde la cima:", posicionRocket)
    print("Posición de Groot desde la cima:", posicionGroot)

def buscas_5peliculas(pila: stack.Stack):
    aux = stack.Stack()

    aux = stack.Stack()
    encontrada = False

    while pila.size() > 0:
        Personaje = pila.pop()
        aux.push(Personaje)

        if Personaje.peliculas >= 5:
            print(f"{Personaje.nombre} tiene {Personaje.peliculas} películas")
            encontrada = True

    while aux.size() > 0:
        pila.push(aux.pop())

    if not encontrada:
        print("No se encontraron personajes con 5 o más películas.")


def buscas_Blackwidow(pila: stack.Stack):
    aux = stack.Stack()

    aux = stack.Stack()
    encontrada = False

    while pila.size() > 0:
        Personaje = pila.pop()
        aux.push(Personaje)

        if Personaje.nombre == "Viuda Negra":
            print(f"{Personaje.nombre} tiene {Personaje.peliculas} películas")
            encontrada = True

    while aux.size() > 0:
        pila.push(aux.pop())

    if not encontrada:
        print("No se enconro a la Viuda Negra en la pila.")


def buscar_Blackwidow(pila: stack.Stack):
    aux = stack.Stack()

    aux = stack.Stack()
    encontrada = False

    while pila.size() > 0:
        Personaje = pila.pop()
        aux.push(Personaje)

        if Personaje.nombre == "Viuda Negra":
            print(f"{Personaje.nombre} tiene {Personaje.peliculas} películas")
            encontrada = True

    while aux.size() > 0:
        pila.push(aux.pop())

    if not encontrada:
        print("No se encontro a la Viuda Negra en la pila.")


def buscar_CDG(pila: stack.Stack):

    aux = stack.Stack()
    encontrada = False

    while pila.size() > 0:
        Personaje = pila.pop()
        aux.push(Personaje)

        if Personaje.nombre[0] == "C" or Personaje.nombre[0] == "D" or Personaje.nombre[0] == "G":
            print(f"El nombre del Personaje es {Personaje.nombre} y empieza con las letras C, D o G")
            encontrada = True

    while aux.size() > 0:
        pila.push(aux.pop())

    if not encontrada:
        print("No se encontraron personajes que empiecen con C, D o G en la pila.")


buscar_GrootandRocket(Marvel)
buscas_5peliculas(Marvel)
buscar_Blackwidow(Marvel)
buscar_CDG(Marvel)