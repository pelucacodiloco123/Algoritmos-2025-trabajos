import stack
from random import randint

pila = stack.Stack()
pila2 = stack.Stack()

i = randint(1, 4)  # entre 1 y 4

# Agregar 4 elementos aleatorios
for j in range(4):
    pila.push(randint(1, 100))

print("Pila original:")
pila.show()
print()

# Sacar los i elementos y meterlos en pila2
for j in range(i):
    pila2.push(pila.on_top())
    pila.pop()

# Eliminar el i-ésimo (el último que se sacó, o sea el tope de pila2)
pila2.pop()

# Volver a meter los otros elementos en pila
if pila2:
    pila.push(pila2.on_top())
    pila2.pop()

print(f"Pila sin el elemento {i} desde la cima:")
pila.show()

