from queue_ import Queue

cola = Queue()

cola.arrive(1)
cola.arrive(2)
cola.arrive(3)
cola.arrive(4)

def rango(cola):
    for i in range(cola.size()):
        menor = None
        mayor = None


        for j in range(cola.size()):
            if (menor is None) or (cola.on_front() < menor):
                menor = cola.on_front()

            cola.move_to_end()

        for j in range(cola.size()):
          if (mayor is None) or (cola.on_front() > mayor):
                mayor = cola.on_front()
                cola.move_to_end()
    return menor, mayor

def negativos(cola):
    negativo = 0
    for i in range(cola.size()):
        if 0 > cola.on_front():
            negativo += 1
            cola.move_to_end()
    return negativo

print(rango(cola))
print(negativos(cola))


        

