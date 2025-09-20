from list_ import List

class Superheroe:
    def __init__(self, nombre, año, aparicion, casa, biografia):
        self.nombre = nombre
        self.año = año
        self.aparicion = aparicion
        self.casa = casa
        self.biografia = biografia
    def __str__(self):
        return f"{self.nombre} ({self.año}) - {self.aparicion} - {self.casa} - {self.biografia}"
    

Superheroes = List()
Superheroes.append(Superheroe("Superman", 1938, "Action Comics #1", "DC Comics", "Superman es un superhéroe ficticio creado por el escritor Jerry Siegel y el artista Joe Shuster.")),
Superheroes.append(Superheroe("Batman", 1939, "Detective Comics #27", "DC Comics", "Batman es un superhéroe ficticio creado por el artista Bob Kane y el escritor Bill Finger.")),
Superheroes.append(Superheroe("Spider-Man", 1962, "Amazing Fantasy #15", "Marvel Comics", "Spider-Man es un superhéroe ficticio creado por el escritor Stan Lee y el artista Steve Ditko.")),
Superheroes.append(Superheroe("Iron Man", 1963, "Tales to Astonish #1", "Marvel Comics", "Iron Man es un superhéroe ficticio creado por el escritor Stan Lee y el artista Jack Kirby.")),
Superheroes.append(Superheroe("Linterna Verde", 1940, "All-American Comics #16", "DC Comics", "Linterna Verde es un superhéroe ficticio creado por el escritor Bill Finger y el artista Martin Nodell.")),
Superheroes.append(Superheroe("Flash", 1940, "Flash Comics #1", "DC Comics", "Flash es un superhéroe ficticio creado por el escritor Gardner Fox y el artista Harry Lampert.")),
Superheroes.append(Superheroe("Wolverine", 1974, "The Incredible Hulk #180", "Marvel Comics", "Wolverine es un superhéroe ficticio creado por el escritor Roy Thomas y el artista Len Wein.")),
Superheroes.append(Superheroe("Dr.Strange", 1963, "Strange Tales #110", "DC comics", "Doctor Strange es un superhéroe ficticio creado por el escritor Stan Lee y el artista Steve Ditko.")),
Superheroes.append(Superheroe("Star-Lord", 1976, "Marvel Preview #4", "Marvel Comics", "Star-Lord es un superhéroe ficticio creado por el escritor Steve Englehart y el artista Steve Gan.")),
Superheroes.append(Superheroe("Capitana Marvel", 1968, "Marvel Super-Heroes #13", "Marvel Comics", "Capitana Marvel es un superhéroe ficticio creado por el escritor Roy Thomas y el artista Gene Colan.")),
Superheroes.append(Superheroe("Mujer Maravilla", 1941, "All-Star Comics #8", "DC Comics", "Mujer Maravilla es un superhéroe ficticio creado por el psicólogo William Moulton Marston y el artista Harry G. Peter.")),

def order_by_nombre(value):
    return value.nombre

def order_by_casa(value):
    return value.casa

def order_by_año(value):
    return value.año

Superheroes.add_criterion("nombre", order_by_nombre)
Superheroes.add_criterion("casa", order_by_casa)
Superheroes.add_criterion("año", order_by_año)

def remove_linternaverde(value):
    while True:
        index = value.search("Linterna Verde", "nombre")
        if index is not None:
            value.delete_value("Linterna Verde", "nombre")
        else:
            break


def wolverine_año(value):
    index = value.search("Wolverine", "nombre")
    if index is not None:
        return value[index].año

        
def DrStrange_cambiarCasa(value):
    index = value.search("Dr.Strange", "nombre")
    if index is not None:
        if value[index].casa == "DC comics":
            value[index].casa = "Marvel Comics"
        else:
            print("Dr.Strange no pertenece a DC Comics")


def mostrar_superheroesarmadura(value):
    resultado = []
    for item in value[:]:
        if "armadura" in item.biografia or "traje" in item.biografia:
            resultado.append(item.nombre)
    return resultado

def mostrar_superheroes1963(value):
    resultado = []
    for item in value[:]:
        if item.año < 1963:
            resultado.append(item.nombre)
    return resultado
        
def CapitanaMaravilla(value):
    resultado = []
    
    index1 = value.search("Capitana Marvel", "nombre")
    if index1 is not None:
        resultado.append(value[index1].casa)
    else:
        resultado.append(None)

    index2 = value.search("Mujer Maravilla", "nombre")
    if index2 is not None:
        resultado.append(value[index2].casa)
    else:
        resultado.append(None)

    return resultado

        
def flashStar(value):
    resultado = []
    index1 = value.search("Flash", "nombre")
    if index1 is not None:
        resultado.append(str(value[index1]))
    else:
        resultado.append(None)

    index2 = value.search("Star-Lord", "nombre")
    if index2 is not None:
        resultado.append(str(value[index2]))
    else:
        resultado.append(None)
    return resultado

        
def letraBMS(value):
    resultados = []
    for item in value:
        if item.nombre[0] in "BMS":
            resultados.append(item.nombre)
    return resultados

        
def contarcasa(value):
    DC = 0
    Marvel = 0
    
    for item in value[:]:
        if item.casa == "DC Comics":
            DC += 1
        elif item.casa == "Marvel Comics":
            Marvel += 1

    return f"DC Comics: {DC}, Marvel Comics: {Marvel}"

remove_linternaverde(Superheroes)
print(wolverine_año(Superheroes))
DrStrange_cambiarCasa(Superheroes)
print(mostrar_superheroesarmadura(Superheroes))
print(mostrar_superheroes1963(Superheroes))
print(CapitanaMaravilla(Superheroes))
print(flashStar(Superheroes))
print(letraBMS(Superheroes))
print(contarcasa(Superheroes))
        


        


    

