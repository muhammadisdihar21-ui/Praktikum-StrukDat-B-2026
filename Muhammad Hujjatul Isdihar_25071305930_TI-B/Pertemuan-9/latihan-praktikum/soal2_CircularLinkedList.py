#Circular Linked List
class Node: #Membuat class Node
    def __init__(self, nama): #Membuat atribut nama dan next
        self.nama = nama
        self.next = None


class CircularLinkedList: #Membuat class CircularLinkedList
    def __init__(self):
        self.head = None

    def insert_tail(self, nama): #Membuat method insert_tail
        new_node = Node(nama)

        if self.head is None: #Pemilihan if
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head: #Perulangan while
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    def print_antrian(self): #Membuat Method print_antrian
        if self.head is None: #Pemilihan if
            return

        temp = self.head
        while True: #Perulangan while
            print(temp.nama, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(kembali ke awal)")

    def delete_head(self): #Membuat Method delete_head
        if self.head is None: #Pemilihan if
            return

        temp = self.head

        while temp.next != self.head: #Perulangan while
            temp = temp.next

        temp.next = self.head.next
        self.head = self.head.next


# Program utama
antrian = CircularLinkedList() #Membuat objek antrian dari class CircularLinkedList

print("\n=====ANTRIAN PELANGGAN TOKO LITERASI=====")
#Menambahkan nama nama yang mengantri
antrian.insert_tail("Andi")
antrian.insert_tail("Budi")
antrian.insert_tail("Citra")
antrian.insert_tail("Dina")

#Menampilkan nama antrian awal
print("\nAntrian awal:")
antrian.print_antrian()

#Menampilkan nama antrian yang sudah ditambah antriannya oleh Edo  
print("\nTambah Edo ke dalam Antrian:")
antrian.insert_tail("Edo")
antrian.print_antrian()

#Menampilkan nama antrian yang sudah selesai mengantri
print("\nAndi sudah dilayani:")
antrian.delete_head()
antrian.print_antrian()
print()