import stack
from random import randint

pila = stack.Stack()

pila2 = stack.Stack()

pila.push(randint(1, 100))
pila.push(randint(1, 100))
pila.push(randint(1, 100))
pila.push(randint(1, 100))

print("La pila original:")

pila.show()
print()

for i in range(pila.size()):
    pila2.push(pila.on_top())
    pila.pop()

print("La pila invertida:")

pila2.show()