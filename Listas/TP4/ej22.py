from list_ import List

class Jedi:
    def __init__(self, nombre, maestros, colorsable, especie):
        self.nombre = nombre
        self.maestros = maestros
        self.colorsable = colorsable
        self.especie = especie

    def __str__(self):
        return f"{self.nombre} ({self.maestros}) - {self.colorsable} - {self.especie}"
    
Jedis = List()
    
Jedis.append(Jedi("Ahsoka Tano",["Anakin Skywalker"], ["Verde", "azul", "Amarillo", "blanco"], "Togruta"))
Jedis.append(Jedi("Kit Fisto",["No se sabe"], ["Verde"], "Nautolano"))
Jedis.append(Jedi("Yoda",[" N'Kata Del Gormo"], ["verde"], "No se sabe"))
Jedis.append(Jedi("Luke Skywalker",["Obi-Wan Kenobi", "Yoda"], ["Azul", "verde"], "Humano"))
Jedis.append(Jedi("Aayla Secura",["Quinlan Vos"], ["Azul"], "Twi'lek"))
Jedis.append(Jedi("Mace Windu",["Cyslin Myr", "Yoda"], ["Violeta"], "Humano"))
Jedis.append(Jedi("Qui-Gon Jin",["Dooku"], ["Verde"],"humano"))
Jedis.append(Jedi("Pong Krell",["No se sabe"], ["Verde", "Azul"], "Besalisko"))
Jedis.append(Jedi("Depa Billaba", ["Mace Windu"],["Verde", "Azul"], "Humano"))
Jedis.append(Jedi("Obi-Wan Kenobi", ["Qui-Gon Jin", "Yoda"], ["Azul"], "Humano"))
Jedis.append(Jedi("Anakin Skywalker", ["Obi-Wan Kenobi", "Darth Sidious"], ["Azul", "Rojo"], "Humano"))
Jedis.append(Jedi("Finn Ertay", ["No se sabe"], ["Azul"],"Twi'lek"))


def order_by_nombre(value):
    return value.nombre

def order_by_especie(value):
    return value.especie

Jedis.add_criterion("nombre", order_by_nombre)
Jedis.add_criterion("especie", order_by_especie)

def mostrar_ahsoka_y_kit(value):
    resultado = []
    index1 = value.search("Ahsoka Tano", "nombre")
    if index1 is not None:
        resultado.append(str(value[index1]))
    else:
        resultado.append(None)

    index2 = value.search("Kit Fisto", "nombre")
    if index2 is not None:
        resultado.append(str(value[index2]))
    else:
        resultado.append(None)
    return resultado


def padawan_Yoda_Luke(value):
    resultado = []
    for jedi in value:
        if "Yoda" in jedi.maestros or "Luke Skywalker" in jedi.maestros:
            resultado.append(str(jedi.nombre))
    return resultado


def humano_twilek(value):
    resultado = []
    for jedi in value:
        if "Humano" in jedi.especie or "Twi'lek" in jedi.especie:
            resultado.append(str(jedi.nombre))
    return resultado

def letraA(value):
    resultados = []
    for jedi in value:
        if jedi.nombre[0] == "A":
            resultados.append(str(jedi))
    return resultados


def mascolores(value):
    resultado = []
    for jedi in value:
        if len(jedi.colorsable) > 2:
            resultado.append(str(jedi.nombre))
    return resultado

def amarillovioleta(value):
    resultado = []
    for jedi in value:
        if "Amarillo" in jedi.colorsable or "Violeta" in jedi.colorsable:
            resultado.append(str(jedi.nombre))
    return resultado

def padawan_Mace_Qin(value):
    resultado = []
    for jedi in value:
        if "Mace Windu" in jedi.maestros or "Qui-Gon Jin" in jedi.maestros:
            resultado.append(str(jedi.nombre))
    return resultado

Jedis.sort_by_criterion("nombre")
print("lista de jedis ordenadas por nombre")
Jedis.show()
Jedis.sort_by_criterion("especie")
Jedis.show()

print(mostrar_ahsoka_y_kit(Jedis))
print(padawan_Yoda_Luke(Jedis))
print(humano_twilek(Jedis))
print(letraA(Jedis))
print(mascolores(Jedis))
print(amarillovioleta(Jedis))
print(padawan_Mace_Qin(Jedis))