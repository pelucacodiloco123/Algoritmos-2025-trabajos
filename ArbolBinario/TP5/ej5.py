from tree import BinaryTree

MCU_Tree = BinaryTree()

MCU_Tree.insert("Capitana Marvel", {"is_villain": False})
MCU_Tree.insert("Iron Man", {"is_villain": False})
MCU_Tree.insert("Thanos", {"is_villain": True})
MCU_Tree.insert("Doctor Doom", {"is_villain": True})
MCU_Tree.insert("Doctor Strangeeeer", {"is_villain": False})
MCU_Tree.insert("Spider-Man", {"is_villain": False})
MCU_Tree.insert("Loki", {"is_villain": True})


def listar_villanos(arbol):
    villanos = []
    def inOrder(nodo):
        if nodo is not None:
            inOrder(nodo.left)
            if nodo.other_values["is_villain"] is True:
                villanos.append(nodo.value)
            inOrder(nodo.right)

    if arbol.root is not None:
        inOrder(arbol.root)
    
    return villanos


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


def contar_Superheroe(arbol):
    def __contarNodosArbol(nodo):
        cantidad = 0
        if nodo is not None:
            if nodo.other_values["is_villain"] is False: #si NO es villano se acumula
                cantidad += 1
            cantidad += __contarNodosArbol(nodo.left)
            cantidad += __contarNodosArbol(nodo.right)

        return cantidad

    total = 0
    if arbol.root is not None:
        total = __contarNodosArbol(arbol.root)
    
    return total


def modificar_doctor_strange(arbol, old_name, new_name):
    arbol.proximity_search("Doctor") #nos va a listar los nombres que comienzan con Doctor.
    value, other_value = arbol.delete(old_name) 
    
    if value is not None:
        arbol.insert(new_name, other_value)
        
    print("Verificamos como quedo (despues de acomodar a Doctor Strange): ")
    arbol.proximity_search("Doctor")


def listar_superheroes_desc(arbol):
   heroes = []
   def postOrder(nodo):
        if nodo is not None:
            postOrder(nodo.right)
            if nodo.other_values["is_villain"] is False:
                heroes.append(nodo.value)
            postOrder(nodo.left)

   
   if arbol.root is not None:
       postOrder(arbol.root)
 
   return heroes


def divide_tree(self, arbol_h, arbol_v):
    def __divide_tree(root, arbol_h, arbol_v):
        if root is not None:
            if root.other_values["is_villain"] is False:
                arbol_h.insert(root.value, root.other_values)
            else:
                arbol_v.insert(root.value, root.other_values)
            __divide_tree(root.left, arbol_h, arbol_v)
            __divide_tree(root.right, arbol_h, arbol_v)

    __divide_tree(self.root, arbol_h, arbol_v)



arbol_heroes = BinaryTree()
arbol_villanos = BinaryTree()


MCU_Tree.divide_tree(arbol_heroes, arbol_villanos)


def contar_nodos(arbol):
    def __contar(root):
        if root is None:
            return 0
        return 1 + __contar(root.left) + __contar(root.right)
    return __contar(arbol.root)

nodos_heroes = contar_nodos(arbol_heroes)
nodos_villanos = contar_nodos(arbol_villanos)



print(listar_villanos(MCU_Tree))
print(listar_superheroes_C(MCU_Tree))
print(contar_Superheroe(MCU_Tree))
modificar_doctor_strange(MCU_Tree, "Doctor Strangeeeer", "Doctor Strange")

print(listar_superheroes_desc(MCU_Tree))

print(f"Cantidad de héroes: {nodos_heroes}")
print(f"Cantidad de villanos: {nodos_villanos}")

print("Héroes (ordenados):")
arbol_heroes.in_order()

print("Villanos (ordenados):")
arbol_villanos.in_order()