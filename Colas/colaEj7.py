from queue_ import Queue

cola = Queue()

cola.arrive(1)
cola.arrive(2)
cola.arrive(3)
cola.arrive(4)

def eliminar_numero(cola,numero):
    for i in range(cola.size()):
        if cola.on_front() == numero:
            cola.attention()
        else:
            cola.move_to_end()
    return cola

eliminar_numero(cola,3)
cola.show()

