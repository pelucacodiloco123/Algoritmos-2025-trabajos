from queue_ import Queue
from random import randint

cola = Queue()

for i in range(10):
    cola.arrive(randint(1, 100))

def eliminar_notprimos(cola):
    for i  in range(cola.size()):
        if cola.on_front() % 2 == 0:
            cola.attention()
        else:
            cola.move_to_end()
    return cola

cola.show()
print("Espacio")
(eliminar_notprimos(cola)).show()
