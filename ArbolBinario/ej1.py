from tree import BinaryTree
from random import randint

numeros = BinaryTree()

for i in range(10):
    num = randint(1, 10000)
    numeros.insert(num)

numeros.pre_order()
numeros.in_order()
numeros.post_order()
numeros.by_level()


def buscar_numero(value, num):
    buscao = value.search(num)
    if buscao is not None:
        return True
    else:
        return False

def eliminar_3valores(arbol):
    for i in range(3):
        num = randint(1, 1000)
        buscao = arbol.search(num)
        if buscao is not None:
            arbol.delete(buscao.value)
        else:
            return None

def alturita(arbol, nodo):
    if nodo is not None:
        altura_izq = arbol.hight(nodo.left)
        altura_derecha = arbol.hight(nodo.right)
        return altura_izq, altura_derecha
    else:
        return None
    
def contarocurrencias(arbol, nodo): #El arbol binario solo deja tener una sola ocurrencia
   ocurrencia = arbol.search(nodo)

   if ocurrencia is not None:
       print("Hay una ocurrencia")
   else:
       print("No hay ocurrencias de este numero")





buscar_numero(numeros, 52)
eliminar_3valores(numeros)
alturita(numeros, 300)

