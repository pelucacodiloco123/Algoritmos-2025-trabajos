from tree import BinaryTree

Tree = BinaryTree()

Tree.insert("a")
Tree.insert("b")
Tree.insert("c")
Tree.insert("d")

def mostrarnododerecho(Arbol, valor_nodo):
    nodo = Arbol.search(valor_nodo)
    return nodo.right.value if nodo and nodo.right else None

def mostrarnodoIZQ(Arbol, valor_nodo):
    nodo = Arbol.search(valor_nodo)
    return nodo.left.value if nodo and nodo.left else None

print(mostrarnododerecho(Tree, "c"))
print(mostrarnodoIZQ(Tree, "c"))
