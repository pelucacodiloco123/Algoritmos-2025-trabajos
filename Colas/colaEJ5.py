from queue_ import Queue
from stack import Stack

cola = Queue()
pila = Stack()

pila.push("A")
pila.push("B")
pila.push("C")
pila.push("D")

def invertir_pila(pila):
  for i in range(pila.size()):
        cola.arrive(pila.pop())
        while cola.size() > 0:
            pila.push(cola.attention())
        return pila

pila.show()
invertir_pila(pila)
