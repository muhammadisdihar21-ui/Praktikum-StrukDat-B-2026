class Node:
    def __init__(self, nama, keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None

class QueueRumahSakit:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def enqueue(self, nama, keluhan):
        new_node = Node(nama, keluhan)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1
        print(f"[DAFTAR] {nama} terdaftar dengan keluhan: {keluhan}")
    
    def dequeue(self):
        if self.is_empty():
            print("[INFO] Antrian masih kosong, tidak ada pasien yang dipanggil.")
            return None
        
        temp = self.head
        self.head = self.head.next
        self._size -= 1

        if self.head is None:
            self.tail = None
        
        print(f"[PANGGIL] Dokter memanggil: {temp.nama} (keluhan: {temp.keluhan})")
        print()
        return temp
    
    def peek(self):
        if self.is_empty():
            return None
        return self.head
    
    def is_empty(self):
        return self.head is None
    
    def size(self):
        return self._size
    
    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0
        print("[CLEAR] Sesi pasienklinik selesai. Antrian dikosongkan.")
    
    def tampilkan(self):
        print()
        print("[ANTRIAN SAAT INI]")
        if self.is_empty():
            print("- Kosong -")
            return
        current = self.head
        no = 1
        while current:
            print(f"{no}. {current.nama} -> {current.keluhan}")
            current = current.next
            no += 1
        print()

    def jalankan(self):
        print("=" * 40)
        print("SISTEM ANTRIAN POLI UMUM\nRS Sehat Bersama")
        print("=" * 40 + "\n")

        pasien = QueueRumahSakit()
        if pasien.is_empty():
            status = "YA, antrian masih kosong."
        else:
            status = "TIDAK, ada pasien."
        print(f"[CEK] Apakah antrian kosong? → {status}")
        print()

        pasien.enqueue("BUDI", "demam tinggi")
        pasien.enqueue("ANI", "batuk pilek")
        pasien.enqueue("CITRA", "sakit kepala")
        print()

        print(f"[INFO] Jumlah pasien menunggu: {pasien.size()} orang")
        print()

        berikutnya = pasien.peek()
        if berikutnya:
            print(f"[PEEK] Pasien berikutnya: {berikutnya.nama} — {berikutnya.keluhan}")

        print()

        pasien.dequeue()

        pasien.enqueue("DODI", "nyeri perut")

        pasien.tampilkan()

        pasien.dequeue()

        print(f"[INFO] Jumlah pasien masih menunggu: {pasien.size()} orang")
        print()

        pasien.clear()

        if pasien.is_empty():
            status = "YA, antrian masih kosong."
        else:
            status = "TIDAK, ada pasien."
        print()
        print(f"[CEK] Apakah antrian kosong? → {status}")


        print("\n" + "=" * 40)
        print("Simulasi Selesai!")
        print("=" * 40)

if __name__ == "__main__":
    antrian = QueueRumahSakit()
    antrian.jalankan()
