class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinartySearchTree:
    def __init__(self):
        self.root = None

    def insertroot(self, data):
        new = Node(data)

        if self.root == None:
            self.root = new
            return
        
        P = self.root
        Q = self.root

        while Q != None and new.data != P.data:
            P = Q

            if new.data < P.data:
                Q = P.left
            else:
                Q = P.right
        
        if new.data == P.data:
            print("Woi datanya duplikat!!")
            return
        
        if new.data < P.data:
            P.left = new
        else:
            P.right = new

    
bst = BinartySearchTree()

bst.insertroot(12)
bst.insertroot(9)
bst.insertroot(5)
bst.insertroot(10)
bst.insertroot(15)

def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

inorder(bst.root)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_root(self, data):
        self.root = Node(data)

    def insert_left(self, parent_node, data):
        new_node = Node(data)
        if parent_node.left is None:
            parent_node.left = new_node
        else:
            new_node.left = parent_node.left
            parent_node.left = new_node
            
    def insert_right(self, parent_node, data):
        new_node = Node(data)
        if parent_node.right is None:
            parent_node.right = new_node
        else:
            new_node.right = parent_node.right
            parent_node.right = new_node

tree = BinaryTree()
tree.insert_root("F") 

tree.insert_left(tree.root, "B")
tree.insert_left(tree.root.left, "A")
tree.insert_right(tree.root.left, "D") 
tree.insert_left(tree.root.left.right, "C")
tree.insert_right(tree.root.left.right, "E") 

tree.insert_right(tree.root, "G")
tree.insert_right(tree.root.right, "I") 
tree.insert_left(tree.root.right.right, "H") 

print()
print("Hasil Inorder:")
inorder(tree.root)