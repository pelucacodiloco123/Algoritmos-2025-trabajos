from tree import BinaryTree

MCU_Tree = BinaryTree()

MCU_Tree.insert("Capitana Marvel", {"is_villain": False})
MCU_Tree.insert("Iron Man", {"is_villain": False})
MCU_Tree.insert("Thanos", {"is_villain": True})
MCU_Tree.insert("Doctor Doom", {"is_villain": True})
MCU_Tree.insert("Doctor Strangeeeer", {"is_villain": False})
MCU_Tree.insert("Spider-Man", {"is_villain": False})
MCU_Tree.insert("Loki", {"is_villain": True})



def listar_villanos(node):
    villanos = []
    if node is not None:
        villanos.extend(listar_villanos(node.left))
        if node.other_values["is_villain"]:
            villanos.append(node.value)
        villanos.extend(listar_villanos(node.right))
    return villanos


def listar_superheroes_con_c(node):
    heroes = []
    if node is not None:
        heroes.extend(listar_superheroes_con_c(node.left))
        if not node.other_values["is_villain"] and node.value.startswith("C"):
            heroes.append(node.value)
        heroes.extend(listar_superheroes_con_c(node.right))
    return heroes


def contar_superheroes(node):
    if node is None:
        return 0
    cont = 0
    if not node.other_values["is_villain"]:
        cont = 1
    cont += contar_superheroes(node.left)
    cont += contar_superheroes(node.right)
    return cont



def Cambiar_Doctor_Strange(self, old_name, new_name):
    searched = self.proximity_search("Doctor")
    if searched:
        for search in searched:
            if search.value == old_name:
                old = search.value
                deleted_value, other_values = self.delete(old)
                if deleted_value is not None:
                    other_values["name"] = new_name
                    self.insert(new_name, other_values)
                    print(f"e) Se ha modificado {old} por {new_name}")
                return
        print(f"e) Se encontró 'Doctor', pero no {old_name}.")
    else:
        print("e) No se ha encontrado ningún elemento que empiece con 'Doctor'.")


def listar_superheroes_desc(node):
    heroes = []
    if node is not None:
        heroes.extend(listar_superheroes_desc(node.right))
        if not node.other_values["is_villain"]:
            heroes.append(node.value)
        heroes.extend(listar_superheroes_desc(node.left))
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



print(listar_villanos(MCU_Tree.root))
print(listar_superheroes_con_c(MCU_Tree.root))
print(contar_superheroes(MCU_Tree.root))
Cambiar_Doctor_Strange(MCU_Tree, "Doctor Strangeeeer", "Doctor Strange") #revisar
MCU_Tree.in_order() #revisar
print(listar_superheroes_desc(MCU_Tree.root))

print("Héroes (ordenados):")
arbol_heroes.in_order()

print("Villanos (ordenados):")
arbol_villanos.in_order()

print(f"Cantidad de héroes: {nodos_heroes}")
print(f"Cantidad de villanos: {nodos_villanos}")



