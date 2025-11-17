from tree import BinaryTree

Tree = BinaryTree()

def Expressioninsert(Tree, expresion): #RPN (Notación Polaca Inversa)
    pila = []
    tokens = expresion.split()  # Convertir string en lista de tokens

    for token in tokens:
        if token in "+-*/":  # Es operador
            derecho = pila.pop()
            izquierdo = pila.pop()
            # Usar la clase __nodeTree de BinaryTree en lugar de Nodo
            nodo = Tree._BinaryTree__nodeTree(token)
            nodo.left = izquierdo
            nodo.right = derecho
            pila.append(nodo)
        else:  # Es operando
            # Crear nodo operando sin hijos
            nodo_operando = Tree._BinaryTree__nodeTree(token)
            pila.append(nodo_operando)
    
    # Asignar la raíz del árbol al último nodo de la pila
    if pila:
        Tree.root = pila[0]


#Los operandos primero, luego los operadores

#Sin paréntesis - el orden define la precedencia

#Se lee de izquierda a derecha

#Cuando encuentras un operador, lo aplicas a los dos operandos anteriores

#se supone que se veria algo asi
  #   +
#    / \
#   3   *
#      / \
#     5   2

#In_order lo muestra como una cuenta normal, post_order en RPN


def resolver_expresion(arbol):
    def _calcular(nodo):
        if nodo.left is None and nodo.right is None:
            return float(nodo.value)  # Es número
        
        izquierdo = _calcular(nodo.left)
        derecho = _calcular(nodo.right)
        
        if nodo.value == '+': return izquierdo + derecho
        if nodo.value == '-': return izquierdo - derecho
        if nodo.value == '*': return izquierdo * derecho
        if nodo.value == '/': return izquierdo / derecho
    
    return _calcular(arbol.root) if arbol.root else 0



Expressioninsert(Tree, "3 5 2 * +")
Tree.in_order()
print(resolver_expresion(Tree))