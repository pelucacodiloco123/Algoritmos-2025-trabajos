#El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u  otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos  objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con  ayuda de la fuerza” realizar las siguientes actividades: 
#a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no  queden más objetos en la mochila; 
#b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sa car para encontrarlo; 
#c. Utilizar un vector para representar la mochila.
#Todo tiene que ser de forma recursiva.


def usar_fuerza(mochila, sable_de_luz, objetos_sacados=0):
    if len(mochila) == 0:
        print("No hay objetos que sacar de la mochila.")
        return False
    
    if len(mochila) == objetos_sacados:
        print("No hay un sable de luz en la mochila.")
        return False
    
    elif mochila[0] == sable_de_luz:
        print(f"Se encontró el sable de luz después de sacar {objetos_sacados} objetos.")
        return True
    else:
        return usar_fuerza(mochila[1:], sable_de_luz, objetos_sacados + 1)


mochila = ["Pistola", "Sable de Luz", "Granada", "Creditos", "Libro"]
sable_de_luz = "Sable de Luz"


usar_fuerza(mochila, sable_de_luz)

#Recordatorio para mi:
#lista[1:] es slicing (rebanado de listas) en Python, y significa:
# Crear una nueva lista desde el segundo elemento (índice 1) hasta el final. Osea en vez de arrancar por el primer elemento
#Arranca por el segundo, chequea de vuelta hasta que encuentro el numerito buscado.