from queue_ import Queue

cola = Queue()

cola.arrive(1)
cola.arrive(1)
cola.arrive(2)
cola.arrive(3)
cola.arrive(4)

def repetido(cola, numero):
    repetido = 0
    for i in range(cola.size()):
        if numero == cola.on_front():
            repetido += 1
            cola.move_to_end()
    return repetido

print(repetido(cola,1))

    