#Desarrollar un algoritmo que permita implementar la búsqueda secuencial con centinela de  manera recursiva, y permita determinar si un valor dado está o no en dicha lista.

def busquedasecuencial(lista, valor):
    if len(lista) == 0:
        return False
    elif lista[0] == valor:
        return True
    else:
        return busquedasecuencial(lista[1:], valor)
    
print(busquedasecuencial([1,2,3,4,5], 5))