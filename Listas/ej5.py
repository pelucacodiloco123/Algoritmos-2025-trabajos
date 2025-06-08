from list_ import List

lista = List()

lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)
lista.append(5)

def remove_primo(value):
    for item in value[:]:
        if item % 2 != 0 and item > 1:
            value.remove(item)

remove_primo(lista)

print(lista.show())