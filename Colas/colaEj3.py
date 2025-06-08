from queue_ import Queue
from stack import Stack

Cola = Queue()
Pila = Stack()

Cola.arrive("n")
Cola.arrive("e")
Cola.arrive("u")
Cola.arrive("q")
Cola.arrive("u")
Cola.arrive("e")
Cola.arrive("n")

def palindromo(Cola):
    Pila = Stack()
    aux_cola = Queue()

    while Cola.size() > 0:
        valor = Cola.attention()
        Pila.push(valor)
        aux_cola.arrive(valor)

    es_palindromo = True
    while aux_cola.size() > 0:
        if aux_cola.attention() != Pila.pop():
            es_palindromo = False
            break

    return es_palindromo

    

print(palindromo(Cola))
