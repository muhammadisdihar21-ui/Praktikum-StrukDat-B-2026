history_array = ["google.com", "python.org"]

def tambah_pencarian_array(keyword):
    history_array.insert(0, keyword)
    print(f"Menambahkan: {keyword}")

history = True
while history:
    print()
    keyword = input("Masukkan history: ")
    tambah_pencarian_array(keyword)
    print()
    lagi = int(input("Lagi? ketik 1 jika ya, ketik 0 jika tidak: "))
    if lagi == 0:
        break

print()
print("Isi history_array (Terbaru -> Terlama):")
print(history_array)
print()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class HistoryLinkedList:
    def __init__(self):
        self.head = None

    def tambah_pencarian_linked(self, keyword):
        new_node = Node(keyword)
        new_node.next = self.head
        self.head = new_node
        print(f"Menambahkan ke LinkedList: {keyword}")

    def tampilkan_history(self):
        current = self.head
        history_list = []
        while current:
            history_list.append(current.data)
            current = current.next
        print("Riwayat (Head -> Tail):", " -> ".join(history_list))

history_ll = HistoryLinkedList()

history_ll.tambah_pencarian_linked("python.org")
history_ll.tambah_pencarian_linked("google.com")

history_ll.tambah_pencarian_linked("github.com")
history_ll.tampilkan_history()