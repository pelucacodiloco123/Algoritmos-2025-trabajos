import stack
from random import randint

pila = stack.Stack()
pila2 = stack.Stack()

pila.push(randint(1, 100))
pila.push(randint(1, 100))
pila.push(randint(1, 100))
pila.push(randint(1, 100))

cont = 0

print(f"Se corroborara si el numero {pila.on_top()} se repite")

numero = pila.on_top()

for i in range(pila.size()):
    top_element = pila.on_top()
    pila2.push(top_element)
    pila.pop()
    if  pila2.on_top() == numero:
        cont += 1

print("El numero se repite", cont, "veces")





