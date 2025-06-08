from list_ import List

lista = List()
lista2 = List()
lista3 = List()
lista4 = List()

lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)

lista2.append(3)
lista2.append(4)
lista2.append(5)
lista2.append(6)
lista2.append(7)
lista2.append(8)

def union(value, value2, value3):
    for item in value:
        value3.append(item)
    for item in value2:
        value3.append(item)
    return value3


def unionsinrepetidos(value, value2, value3):
    for item in value:
        if item not in value2:
            value3.append(item)
    for item in value2:
        if item not in value:
            value3.append(item)
            return value3

def contareptidos(value,value2):
    repetidos = 0
    for item in value:
        if item in value2:
            repetidos += 1
    return repetidos

def eliminarlista(lista):
    while lista:
        eliminado = lista.pop(0)
        print("Elemento eliminado:", eliminado)


print(union(lista, lista2, lista3))
print(unionsinrepetidos(lista, lista2, lista4))
print(contareptidos(lista, lista2))
print(eliminarlista(lista))

