from tree import BinaryTree

class CreaturesTree(BinaryTree):
    class __nodeTree(BinaryTree._BinaryTree__nodeTree):
        def __init__(self, value: str, other_values: dict = None):
            if other_values is None:
                other_values = {
                    "Vencido por": [],
                    "descripcion": "",
                    "capturado por": None,
                }
            super().__init__(value, other_values)


            creatures = { }
