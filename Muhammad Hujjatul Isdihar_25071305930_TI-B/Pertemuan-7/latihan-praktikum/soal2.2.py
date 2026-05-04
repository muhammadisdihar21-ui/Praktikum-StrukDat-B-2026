class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class AntreanLinkedList:
    
    def __init__(self):
        self.head = None


    def tampilkan(self):
        temp = self.head
        
        if temp is None:
            print("Antrean kosong")
            return
        
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        
        print("None")


    def hitung(self):
        temp = self.head
        count = 0
        
        while temp:
            count += 1
            temp = temp.next
        
        return count


    def insert_at_position(self, nama_pasien, posisi):

        new_node = Node(nama_pasien)

        if self.head is None:
            self.head = new_node
            return

        jumlah = self.hitung()

        if posisi > jumlah:
            temp = self.head
            
            while temp.next:
                temp = temp.next
            
            temp.next = new_node
            return

        if posisi == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        
        for i in range(posisi - 2):
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node


antrian = AntreanLinkedList()

antrian.insert_at_position("Pasien A (Stabil)",1)
antrian.insert_at_position("Pasien B (Stabil)",2)
antrian.insert_at_position("Pasien C (Stabil)",3)

print("Antrean awal:")
antrian.tampilkan()

antrian.insert_at_position("Pasien D (Darurat)",2)

print("Antrean setelah pasien darurat:")
antrian.tampilkan()

antrian.insert_at_position("Pasien E (Darurat)",10)

print("Antrean setelah penambahan lagi:")
antrian.tampilkan()