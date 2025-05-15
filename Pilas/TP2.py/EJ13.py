import stack

class Armadura:
    def __init__(self, modelo: str, pelicula: str, estado: str):
        self.modelo = modelo
        self.pelicula = pelicula
        self.estado = estado

    def __str__(self):
        return f"{self.modelo} - {self.pelicula} - {self.estado}"


IronMan = stack.Stack()
IronMan.push(Armadura("Mark I", "Iron Man 1", "Destruida"))
IronMan.push(Armadura("Mark I", "Iron Man 2", "Impecable"))
IronMan.push(Armadura("Mark I", "Iron Man 3", "Destruida"))
IronMan.push(Armadura("Mark II", "Iron Man 1", "Destruida"))
IronMan.push(Armadura("Mark II", "Iron Man 2", "Impecable"))
IronMan.push(Armadura("Mark II", "Iron Man 3", "Destruida"))
IronMan.push(Armadura("Mark II (Casco)", "Avengers: Endgame", "Impecable"))
IronMan.push(Armadura("Mark II (Casco)", "Deadpool And Wolverine", "Impecable"))
IronMan.push(Armadura("Mark III", "Iron Man 1", "Impecable"))
IronMan.push(Armadura("Mark III", "Iron Man 2", "Impecable"))
IronMan.push(Armadura("Mark III", "Iron Man 3", "Impecable"))
IronMan.push(Armadura("Mark IV", "Iron Man 2", "Destruida"))
IronMan.push(Armadura("Mark IV", "Iron Man 3", "Destruida"))
IronMan.push(Armadura("Mark V", "Iron Man 2", "Destruida"))
IronMan.push(Armadura("Mark V", "Iron Man 3", "Impecable"))
IronMan.push(Armadura("Mark V", "Deadpool And Wolverine", "Impecable"))
IronMan.push(Armadura("Mark LXXXV", "Avengers: Endgame", "Dañada"))
IronMan.push(Armadura("Mark XLVII", "Spiderman: Homecoming", "Impecable"))
IronMan.push(Armadura("Mark XLVI", "Capitan America: Civil War", "Dañada"))

IronMan.push(Armadura("Mark XLIV (Hulkbuster)", "Avengers: Age of Ultron", "Impecable"))

def buscar_hulkbuster(pila: stack.Stack):
    aux = stack.Stack() 
    encontrada = False

    while pila.size() > 0:
        armadura = pila.pop()
        if armadura is None:
            continue
        aux.push(armadura)

        if armadura.modelo == "Mark XLIV (Hulkbuster)":
            print(f"Hulkbuster encontrada en la pila y pertenece a la película: {armadura.pelicula}")
            encontrada = True

    while aux.size() > 0:
        pila.push(aux.pop())

    if not encontrada:
        print("Hulkbuster no encontrada en la pila.")


def buscar_dañado(pila: stack.Stack):
    aux = stack.Stack() 
    dañadas = []

    while pila.size() > 0:
        armadura = pila.pop()
        if armadura is None:
            continue
        aux.push(armadura)

        if armadura.estado == "Dañada":
            dañadas.append(armadura.modelo)

    while aux.size() > 0:
        pila.push(aux.pop())

    if dañadas:
        print("Armaduras dañadas encontradas en la pila:")
        for armadura in dañadas:
            print(armadura)
    else:
        print("No se encontraron armaduras dañadas en la pila.")


def eliminar_destruidas(pila: stack.Stack):
    aux = stack.Stack()

    while pila.size() > 0:
        armadura = pila.pop()
        if armadura is None:
            continue
        if armadura.estado != "Destruida":
            aux.push(armadura)

    while aux.size() > 0:
        pila.push(aux.pop())

    print("Armaduras destruidas eliminadas de la pila.")

def buscar_capitan_spiderman(pila: stack.Stack):
    aux = stack.Stack()
    encontrada = False

    while pila.size() > 0:
        armadura = pila.pop()
        aux.push(armadura)

        if armadura.pelicula == "Capitan America: Civil War" or armadura.pelicula == "Spiderman: Homecoming":
            print(armadura)
            encontrada = True

    while aux.size() > 0:
        pila.push(aux.pop())

    if not encontrada:
        print("No se encontraron armaduras de Capitan America: Civil War o Spiderman: Homecoming en la pila.")


    
buscar_hulkbuster(IronMan)
buscar_dañado(IronMan)
eliminar_destruidas(IronMan)
buscar_capitan_spiderman(IronMan)



