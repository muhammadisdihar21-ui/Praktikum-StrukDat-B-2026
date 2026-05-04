class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_manual(self):
        print("[INFO] Membangun Struktur Gudang...")

        self.root = Node("A")
        self.root.left = Node("B")
        self.root.right = Node("C")

        self.root.left.left = Node("D")
        self.root.left.right = Node("E")

        self.root.right.right = Node("F")
        print()
        print("[INFO] Struktur berhasil dibuat.")

    def traverse_preorder(self, node):
        if node is not None:
            if self.first_pre:
                print(node.data, end="")
                self.first_pre = False
            else:
                print(" - " + node.data, end="")
            self.traverse_preorder(node.left)
            self.traverse_preorder(node.right)

    def traverse_inorder(self, node):
        if node is not None:
            self.traverse_inorder(node.left)
            if self.first_in:
                print(node.data, end="")
                self.first_in = False
            else:
                print(" - " + node.data, end="")
            self.traverse_inorder(node.right)

    def traverse_postorder(self, node):
        if node is not None:
            self.traverse_postorder(node.left)
            self.traverse_postorder(node.right)
            if self.first_post:
                print(node.data, end="")
                self.first_post = False
            else:
                print(" - " + node.data, end="")

    def get_leaf_nodes(self, node):
        if node is not None:
            if node.left is None and node.right is None:
                if self.first_leaf:
                    print(node.data, end="")
                    self.first_leaf = False
                else:
                    print(", " + node.data, end="")
            self.get_leaf_nodes(node.left)
            self.get_leaf_nodes(node.right)

print()
print("SISTEM AUDIT DISTRIBUSI \"CEPAT SAMPAI\"")
print()
print("======================================")
print()

bt = BinaryTree()
bt.insert_manual()

print("\nHASIL AUDIT:")

print("1. Pre-Order : ", end="")
bt.first_pre = True
bt.traverse_preorder(bt.root)

print("\n2. In-Order : ", end="")
bt.first_in = True
bt.traverse_inorder(bt.root)

print("\n3. Post-Order : ", end="")
bt.first_post = True
bt.traverse_postorder(bt.root)

print()
print("\n[DATA] Gudang Ujung (Leaf Nodes): ", end="")
bt.first_leaf = True
bt.get_leaf_nodes(bt.root)
print()
print("\n======================================")
print()
print("Audit Selesai!")
print()