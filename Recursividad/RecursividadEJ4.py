#Implementar una función para calcular la potencia dado dos números enteros, el primero re presenta la base y segundo el exponente.

def potencia(base: int, exponente: int) -> int:
    if exponente == 0:
        return 1
    elif exponente == 1:
        return base
    else:
        return base * potencia(base, exponente - 1)

print("Potencia de 2 elevado a 3:", potencia(2, 3))
