from tree import BinaryTree

Tree = BinaryTree()

Tree.insert("a")
Tree.insert("b")
Tree.insert("c")
Tree.insert("d")

def nodoMinimo(tree):
    if tree.root is None:
        return None
    
    current = tree.root
    while current.left is not None:
        current = current.left
    return current.value

def nodoMaximo(tree):
    if tree.root is None:
        return None
    
    current = tree.root
    while current.right is not None:
        current = current.right
    return current.value


minimo = nodoMinimo(Tree)
maximo = nodoMaximo(Tree)

print(f"Nodo mínimo: {minimo}")
print(f"Nodo máximo: {maximo}")