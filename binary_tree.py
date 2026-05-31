class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def print_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.value))
        print_tree(node.left, level + 1, "L--- ")
        print_tree(node.right, level + 1, "R--- ")


print("VALID TREE")
print("-" * 30)

root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.right.left = Node("D")

print_tree(root)

print("\nNOT A TREE")
print("-" * 30)

A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")

A.left = B
A.right = C

B.right = D
C.left = D  # D now has TWO parents

print("A -> B -> D")
print("A -> C -> D")

print("\nD object id from B:", id(B.right))
print("D object id from C:", id(C.left))

print("\nAre they the same object?")
print(B.right is C.left)