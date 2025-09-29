def listar_superheroes_C(arbol):
    heroes = []
    def inOrder(nodo):
        if nodo is not None:
            inOrder(nodo.left)
            if nodo.other_values["is_villain"] is False and nodo.value.startswith("C"):
                heroes.append(nodo.value)
            inOrder(nodo.right)

    if arbol.root is not None:
        inOrder(arbol.root)

    return heroes