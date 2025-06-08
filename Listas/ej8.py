#prueba que encontre
class Nodo:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class ListaDobleEnlazada:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def append(self, data):
        nuevo_nodo = Nodo(data)
        if self.first is None:
            self.first = self.last = nuevo_nodo
        else:
            self.last.next = nuevo_nodo
            nuevo_nodo.prev = self.last
            self.last = nuevo_nodo
        self.size += 1

    def __len__(self):
        return self.size

    def show(self):
        actual = self.first
        while actual:
            print(actual.data, end=" ")
            actual = actual.next
        print()

def es_palindromo(palabra):
    caracteres = ListaDobleEnlazada()

    # cargar carácter a carácter
    for letra in palabra:
        caracteres.append(letra)

    if len(caracteres) == 0:
        return False  # vacío no se considera palíndromo

    inicio = caracteres.first
    fin = caracteres.last

    while inicio != fin and inicio.prev != fin:
        if inicio.data != fin.data:
            return False
        inicio = inicio.next
        fin = fin.prev

    return True

# 📌 Pruebas
print(es_palindromo("neuquen"))    # True
print(es_palindromo("radar"))      # True
print(es_palindromo("python"))     # False
