from list_ import List

list = List()
listpar = List()
listimpar = List()

list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)
list.append(6)
list.append(7)
list.append(8)
list.append(9)
list.append(10)

def parimpar(value):
    for item in value[:]:
        if item % 2 == 0:
            listpar.append(item)
        else:
            listimpar.append(item)

print(f"Lista original: {list}")
parimpar(list)
print(f"Lista par: {listpar}")
print(f"Lista impar: {listimpar}")
