from queue_ import Queue

Cola = Queue()

Cola.arrive("A")
Cola.arrive("B")
Cola.arrive("C")
Cola.arrive("D")
Cola.arrive("E")

def eliminar_vocales(Cola):
    for i in range(Cola.size()):
        if Cola.on_front() in "AEIOUaeiou":
          Cola.attention()
        else:
           Cola.move_to_end()
    return Cola

(eliminar_vocales(Cola)).show()
