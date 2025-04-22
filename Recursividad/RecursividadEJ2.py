#Implementar una función que calcule la suma de todos los números enteros comprendidos  entre cero y un número entero positivo dado de forma recursiva.

def suma(num: int) -> int:
    if num == 0:
        return 0
    else:
        return num + suma(num - 1)

print(suma(5))