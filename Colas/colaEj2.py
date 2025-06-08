from queue_ import Queue
from stack import Stack

Cola = Queue()
Pila = Stack()

Cola.arrive("A")
Cola.arrive("B")
Cola.arrive("C")
Cola.arrive("D")

def invertir_Cola(Cola):
    for i in range(Cola.size()):
        Pila.push(Cola.attention())
    
    while Pila.size() > 0:
        Cola.arrive(Pila.pop())
    
    return Cola

Cola.show()
invertir_Cola(Cola).show()