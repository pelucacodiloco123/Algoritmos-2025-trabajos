from queue_ import Queue
from random import randint

cola = Queue()

for i in range(10):
    cola.arrive(randint(1,100))


def ordenar_colacreciente(cola):

    for i in range(cola.size()):
        menor = None


        for j in range(cola.size()):
            if (menor is None) or (cola.on_front() < menor):
                menor = cola.on_front()

            cola.move_to_end()


        for j in range(cola.size()):
            if cola.on_front() == menor:
                cola.attention()
            else:
                cola.move_to_end()

        cola.arrive(menor)


cola.show()
print("espacio")
ordenar_colacreciente(cola)
cola.show()

    

