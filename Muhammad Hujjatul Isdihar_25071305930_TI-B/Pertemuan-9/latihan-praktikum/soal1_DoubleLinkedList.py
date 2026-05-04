#Double Linked List
class Node: #Membuat class Node
    def __init__(self, judul, pengarang): #Membuat atribut judul, pengarang, prev, dan next
        self.judul = judul
        self.pengarang = pengarang
        self.prev = None
        self.next = None


class DoublyLinkedList: #Membuat class DoublyLinkedList
    def __init__(self):
        self.head = None

    def insert_tail(self, judul, pengarang): #Membuat atribut judul dan pengarang ke method insert_tail()
        new_node = Node(judul, pengarang)

        if self.head is None: #Pemilihan if
            self.head = new_node
            return

        temp = self.head
        while temp.next: #perulangan while
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def print_forward(self): #Membuat method print_forward
        temp = self.head
        while temp: #Perulangan while
            print(temp.judul, "-", temp.pengarang)
            temp = temp.next

    def print_backward(self): #membuat method print_backward
        temp = self.head
        while temp.next: #Perulangan while
            temp = temp.next

        while temp: #Perulangan while
            print(temp.judul, "-", temp.pengarang)
            temp = temp.prev

    def delete_by_judul(self, judul): #membuat method delete_by_judul
        temp = self.head

        while temp: #Perulangan while
            if temp.judul == judul: #Pemilihan if
                if temp.prev:
                    temp.prev.next = temp.next
                else: #Pemilihan else
                    self.head = temp.next

                if temp.next: #Pemilihan if
                    temp.next.prev = temp.prev
                break

            temp = temp.next


# Program utama
buku = DoublyLinkedList() #Membuat objek buku dari class DoublyLinkedList()

#Menambahkan buku 
buku.insert_tail("Laskar Pelangi", "Andrea Hirata") 
buku.insert_tail("Bumi Manusia", "Pramoedya Ananta Toer")
buku.insert_tail("Sang Pemimpi", "Andrea Hirata")

print("\n=====DAFTAR LAGU DI TOKO BUKU LITERASI=====")

#Menampilkan buku dari depan ke belakang dengan pointer next
print("\nPrint Forward:")
buku.print_forward()

#Menampilkan buku dari belakang ke depan dengan pointer prev
print("\nPrint Backward:")
buku.print_backward()

#Menghapus buku Bumi Manusia
print("\nMenghapus Bumi Manusia\n")
buku.delete_by_judul("Bumi Manusia")

#Daftar buku setelah Bumi Manusia dihapus
print("\nDaftar buku setelah dihapus:")
buku.print_forward()