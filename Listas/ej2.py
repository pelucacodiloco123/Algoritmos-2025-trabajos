from list_ import List

lista = List()

lista.append("a")
lista.append("b")
lista.append("c")
lista.append("d")

def remove_vocal(value):
    for item in value[:]: 
        if item in "aeiou":
            value.remove(item)

remove_vocal(lista)

print(lista.show())


