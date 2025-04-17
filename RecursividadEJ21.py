#Dada una lista de valores ordenadas, desarrollar un algoritmo que modifique el método de  búsqueda binaria para que funcione de forma recursiva, y permita determinar si un valor dado  está o no en dicha lista.

def busquedabinaria(lista, valor):
    if len(lista) == 0:
        return False
    else:
        medio = len(lista) // 2
        if lista[medio] == valor:
            return True
        elif valor < lista[medio]:
            return busquedabinaria(lista[:medio], valor) 
        else:
            return busquedabinaria(lista[medio+1:], valor)
        
print(busquedabinaria([1,2,3,4,5], 5))
print(busquedabinaria([1,2,3,4,5], 6))
