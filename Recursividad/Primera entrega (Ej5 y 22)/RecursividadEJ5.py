#Desarrollar una función que permita convertir un número romano en un número de forma recursiva.

romanos = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

def convertir(romano: str) -> int:
    if len(romano) == 0:
        return 0
    elif len(romano) == 1:
        return romanos[romano[0]]
    else:
        if romanos[romano[0]] < romanos[romano[1]]:
            return -romanos[romano[0]] + convertir(romano[1:])
        else:
            return romanos[romano[0]] + convertir(romano[1:])
        
print(convertir('V'))
print(convertir('IV'))
print(convertir('IX'))
print(convertir('XIV'))

#Nota para mi: Basicamente chequea primero la ubicacion de la letra en el string (ya que es una lista de letras)
#si su longitud es 0, no hay letra, retorna 0.
#Si es 1, significa que solo hay una letra, retorna el numero ese.
# Si hay mas, si la anterior es menor a la siguiente, se la resta, si es al reves, se suma.
#Y el diccionario esta, si no, la maquina no entiende nada.

