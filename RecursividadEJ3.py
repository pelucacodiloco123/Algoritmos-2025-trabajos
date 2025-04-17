# Implementar una función para calcular el producto de dos números enteros dados en forma recursiva

def producto(num1, num2):
    # Caso base: si num2 es 0, el producto es 0
    if num2 == 0:
        return 0
    # Si num2 es negativo, convertir el problema a un caso positivo
    elif num2 < 0:
        return -producto(num1, -num2)
    # Caso recursivo: sumar num1, num2 veces
    else:
        return num1 + producto(num1, num2 - 1)

# Obtener los números del usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Calcular y mostrar el producto
print("El producto de", num1, "y", num2, "es:", producto(num1, num2))
