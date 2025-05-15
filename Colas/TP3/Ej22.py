import queue_

class Personajes:
    def __init__(self,heroe,identidad,genero):
        self.heroe=heroe
        self.identidad=identidad
        self.genero=genero
    
    def __str__(self):
        return f"{self.heroe} - {self.identidad} - {self.genero}"
    

Superheroes=queue_.Queue()

Superheroes.arrive(Personajes("Iron Man","Tony Stark","Masculino"))
Superheroes.arrive(Personajes("Spiderman","Peter Parker","Masculino"))
Superheroes.arrive(Personajes("Capitana Marvel","Carol Danvers","Femenino"))
Superheroes.arrive(Personajes("Ant-Man","Scott Lang","Masculino"))


def Nombre_CapitanaMarvel(cola: queue_.Queue):
    for i in range(cola.size()):
        if cola.on_front().heroe == "Capitana Marvel":
            print(cola.on_front().identidad)
        cola.move_to_end()
    return print("Se mostro el nombre de la Capitana Marvel")

def Mostrar_Femeninos(cola: queue_.Queue):
    for i in range(cola.size()):
        if cola.on_front().genero == "Femenino":
            print(cola.on_front())
        cola.move_to_end()
    return print("Se mostraron todos los personajes femeninos")


def Mostrar_Masculinos(cola: queue_.Queue):
    for i in range(cola.size()):
        if cola.on_front().genero == "Masculino":
            print(cola.on_front())
        cola.move_to_end()
    return print("Se mostraron todos los personajes masculinos")

def Superheroe_ScottLang(cola: queue_.Queue):
    for i in range(cola.size()):
        if cola.on_front().identidad == "Scott Lang":
            print(cola.on_front().heroe)
        cola.move_to_end()
    return print("Se mostro el nombre de heroe de Scott Lang")

def Nombre_S(cola: queue_.Queue):
    for i in range(cola.size()):
        if cola.on_front().heroe[0] == "S" or cola.on_front().identidad[0] == "S":
            print (cola.on_front())
            cola.move_to_end()
    return print("Se mostraron todos los personajes que empiezan con S")


def Buscar_Carol(cola: queue_.Queue):
    for i in range(cola.size()):
        if cola.on_front().identidad == "Carol Danvers":
            print(cola.on_front().heroe)
        cola.move_to_end()
    return print("Se mostro el nombre de superheroe de Carol Danvers")

Nombre_CapitanaMarvel(Superheroes)
Mostrar_Femeninos(Superheroes)
Mostrar_Masculinos(Superheroes)
Superheroe_ScottLang(Superheroes)
Nombre_S(Superheroes)
Buscar_Carol(Superheroes)
