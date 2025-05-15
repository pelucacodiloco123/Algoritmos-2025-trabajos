import stack


pila = stack.Stack()
pila2 = stack.Stack()

pila.push("neuquen")

pila2.push(pila.on_top()[::-1])

if pila.on_top() == pila2.on_top():
    print("Es palindromo")
else:
    print("No es palindromo")