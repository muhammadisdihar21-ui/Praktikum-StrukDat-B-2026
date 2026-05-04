class Node:
    def __init__(self, id_buku, judul):
        self.id_buku = id_buku
        self.judul = judul
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, id_buku, judul):
        new_node = Node(id_buku, judul)

        if self.root is None:
            self.root = new_node
            print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
        else:
            self._insert_recursive(self.root, new_node)

    def _insert_recursive(self, current, new_node):
        if new_node.id_buku < current.id_buku:
            if current.left is None:
                current.left = new_node
                print(f"[INSERT] Berhasil memasukkan: ID {new_node.id_buku} - {new_node.judul}")
            else:
                self._insert_recursive(current.left, new_node)
        elif new_node.id_buku > current.id_buku:
            if current.right is None:
                current.right = new_node
                print(f"[INSERT] Berhasil memasukkan: ID {new_node.id_buku} - {new_node.judul}")
            else:
                self._insert_recursive(current.right, new_node)

    def search(self, id_buku):
        return self._search_recursive(self.root, id_buku)

    def _search_recursive(self, current, id_buku):
        if current is None:
            return None

        if id_buku == current.id_buku:
            return current
        elif id_buku < current.id_buku:
            return self._search_recursive(current.left, id_buku)
        else:
            return self._search_recursive(current.right, id_buku)

    def inorder(self):
        print()
        print("[INFO] Koleksi Buku (In-Order Traversal):")
        self._inorder_recursive(self.root, 1)

    def _inorder_recursive(self, current, counter):
        if current is None:
            return counter
        counter = self._inorder_recursive(current.left, counter)
        print(f"{counter}. {current.id_buku} - {current.judul}")
        counter += 1
        counter = self._inorder_recursive(current.right, counter)
        
            

    def get_min(self):
        current = self.root
        while current.left is not None:
            current = current.left
        return current

    def get_max(self):
        current = self.root
        while current.right is not None:
            current = current.right
        return current

    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, current):
        if current is None:
            return -1

        left_height = self._height_recursive(current.left)
        right_height = self._height_recursive(current.right)

        return max(left_height, right_height) + 1

print()
print("SISTEM KATALOG PERPUSTAKAAN \"ILMU TERANG\"")
print()
print("=========================================")
print()
bst = BST()

bst.insert(50, "Dasar Pemrograman")
bst.insert(30, "Struktur Data")
bst.insert(70, "Kecerdasan Buatan")
bst.insert(20, "Matematika Diskrit")
bst.insert(40, "Basis Data")
bst.insert(60, "Jaringan Komputer")
bst.insert(80, "Sistem Operasi")

bst.inorder()

print("\n[SEARCH] Mencari ID 60...", end=" ")
hasil = bst.search(60)
if hasil:
    print(f"Ditemukan! Judul: {hasil.judul}")
else:
    print("Data tidak ditemukan.")

print("[SEARCH] Mencari ID 100...", end=" ")
hasil = bst.search(100)
if hasil:
    print(f"Ditemukan! Judul: {hasil.judul}")
else:
    print("Data tidak ditemukan.")

min_node = bst.get_min()
max_node = bst.get_max()

print(f"\n[STATISTIK] ID Terkecil: {min_node.id_buku}")
print(f"[STATISTIK] ID Terbesar: {max_node.id_buku}")
print(f"[INFO] Tinggi (Height) Tree: {bst.height()}")
print()
print("=========================================")
print()
print("Simulasi Selesai!")
print()