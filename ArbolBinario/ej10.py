from tree import BinaryTree

def contar_nodos_nivel(tree, nivel_objetivo):
    """Cuenta el número de nodos en un nivel específico del árbol"""
    # PASO 1: Verificar si el árbol está vacío
    if tree.root is None:
        return 0  # Si no hay raíz, el árbol está vacío
    
    # PASO 2: Inicializar variables
    count = 0  # Contador para llevar la cuenta de nodos en el nivel objetivo
    current_level = 0  # (Esta variable no se usa realmente, podría eliminarse)
    
    # PASO 3: Definir función recursiva interna
    def contar_recursivo(nodo, nivel_actual):
        nonlocal count  # Permite modificar la variable count de la función exterior
        
        # PASO 3.1: Caso base - si el nodo es None, termina esta rama
        if nodo is None:
            return
        
        # PASO 3.2: Verificar si estamos en el nivel objetivo
        if nivel_actual == nivel_objetivo:
            count += 1  #Encontramos un nodo en el nivel que buscamos
        
        # PASO 3.3: Llamar recursivamente a los hijos
        contar_recursivo(nodo.left, nivel_actual + 1)   # Hijo izquierdo, nivel +1
        contar_recursivo(nodo.right, nivel_actual + 1)  # Hijo derecho, nivel +1
    
    # PASO 4: Iniciar la recursión desde la raíz (nivel 0)
    contar_recursivo(tree.root, 0)
    
    # PASO 5: Retornar el resultado final
    return count


def listar_nodos_nivel(tree, nivel_objetivo):
    """Lista los nodos que hay en un nivel específico del árbol"""
    # PASO 1: Verificar si el árbol está vacío
    if tree.root is None:
        return []  # Si no hay raíz, retorna lista vacía
    
    # PASO 2: Crear lista para almacenar los nodos del nivel objetivo
    nodos_nivel = []
    
    # PASO 3: Definir función recursiva interna
    def listar_recursivo(nodo, nivel_actual):
        # PASO 3.1: Caso base - si el nodo es None, termina esta rama
        if nodo is None:
            return
        
        # PASO 3.2: Verificar si estamos en el nivel objetivo
        if nivel_actual == nivel_objetivo:
            nodos_nivel.append(nodo.value)  # Agregar el valor del nodo a la lista
            return  # Retornamos aca para no seguir bajando niveles
        
        # PASO 3.3: Llamar recursivamente a los hijos (solo si no estamos en el nivel objetivo)
        listar_recursivo(nodo.left, nivel_actual + 1)   # Hijo izquierdo, nivel +1
        listar_recursivo(nodo.right, nivel_actual + 1)  # Hijo derecho, nivel +1
    
    # PASO 4: Iniciar la recursión desde la raíz (nivel 0)
    listar_recursivo(tree.root, 0)
    
    # PASO 5: Retornar la lista con todos los nodos del nivel objetivo
    return nodos_nivel


def nivel_esta_completo(tree, nivel_objetivo):
    """Determina si un nivel del árbol está completo (tiene todos los nodos posibles)"""
    if tree.root is None:
        return False
    
    # Un nivel está completo si tiene 2^nivel_objetivo nodos
    nodos_esperados = 2 ** nivel_objetivo
    nodos_reales = contar_nodos_nivel(tree, nivel_objetivo)
    
    return nodos_reales == nodos_esperados


def nodos_faltantes_para_completar(tree, nivel_objetivo):
    """Calcula cuántos nodos faltan para que un nivel esté completo"""
    if tree.root is None:
        return 2 ** nivel_objetivo  # Si no hay árbol, faltan todos los nodos del nivel
    
    nodos_esperados = 2 ** nivel_objetivo
    nodos_reales = contar_nodos_nivel(tree, nivel_objetivo)
    nodos_faltantes = nodos_esperados - nodos_reales
    
    return max(0, nodos_faltantes)


tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)
tree.insert(12)
tree.insert(18)

nivel = 2

print(contar_nodos_nivel(tree, nivel))
print(listar_nodos_nivel(tree, nivel))
print(nivel_esta_completo(tree, nivel))
print(nodos_faltantes_para_completar(tree, nivel))
