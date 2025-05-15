import stack


pila = stack.Stack()
pila2 = stack.Stack()

palabra = "saracatunga"

pila.push(palabra)

pila2.push(pila.on_top()[::-1])

print("La palabra original es ", pila.on_top())
print("La palabra invertida es ", pila2.on_top())
