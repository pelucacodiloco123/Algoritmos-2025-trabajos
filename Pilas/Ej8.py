
import stack
from random import randint, choice

# Palos posibles
palos = ["Espada", "Basto", "Copa", "Oro"]

# Crear pilas
mazo = stack.Stack()

espada = stack.Stack()
espada_ordenado = stack.Stack()

basto = stack.Stack()
basto_ordenado = stack.Stack()

copa = stack.Stack()
copa_ordenado = stack.Stack()

oro = stack.Stack()
oro_ordenado = stack.Stack()

# Crear cartas aleatorias
for _ in range(20):  # por ejemplo, 20 cartas
    carta = (choice(palos), randint(1, 12))  # ej: ("Copa", 4)
    mazo.push(carta)

    # Clasificar por palo
    if carta[0] == "Espada":
        espada.push(carta)
    elif carta[0] == "Basto":
        basto.push(carta)
    elif carta[0] == "Copa":
        copa.push(carta)
    else:
        oro.push(carta)

# Función para ordenar por número usando una pila auxiliar
def ordenar_pila(pila_original, pila_ordenada):
    while pila_original.size() > 0:
        temp = pila_original.on_top()
        pila_original.pop()

        while pila_ordenada.size() > 0 and pila_ordenada.on_top()[1] > temp[1]:
            pila_original.push(pila_ordenada.on_top())
            pila_ordenada.pop()

        pila_ordenada.push(temp)

# Ordenar cada pila
ordenar_pila(espada, espada_ordenado)
ordenar_pila(basto, basto_ordenado)
ordenar_pila(copa, copa_ordenado)
ordenar_pila(oro, oro_ordenado)

# Mostrar resultados
print("Cartas de ESPADA ordenadas:")
espada_ordenado.show()
print()

print("Cartas de BASTO ordenadas:")
basto_ordenado.show()
print()

print("Cartas de COPA ordenadas:")
copa_ordenado.show()
print()

print("Cartas de ORO ordenadas:")
oro_ordenado.show()
print()


