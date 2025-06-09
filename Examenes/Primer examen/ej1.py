
superheroes = [
    "Iron Man", "Thor", "Hulk", "Black Widow", "Hawkeye",
    "Spider-Man", "Doctor Strange", "Black Panther", "Scarlet Witch",
    "Vision", "Ant-Man", "Wasp", "Falcon", "Winter Soldier", "Capitan America"
]


def buscar_capitan(lista, index=0):
    if index >= len(lista):
        return False
    if lista[index] == "Capitan America":
        return True
    return buscar_capitan(lista, index + 1)


def listar_superheroes(lista, index=0):
    if index >= len(lista):
        return
    print(lista[index])
    listar_superheroes(lista, index + 1)


if buscar_capitan(superheroes):
    print("Capitan America está en la lista.")
else:
    print("Capitan America NO está en la lista.")

print("Listado de superhéroes:")
listar_superheroes(superheroes)
