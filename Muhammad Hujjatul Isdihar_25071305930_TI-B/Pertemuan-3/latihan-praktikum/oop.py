class MyKereta:
    def __init__(self, merek, warna, jumlahKursi):
        self.merek = merek
        self.warna = warna
        self.jumlahKursi = jumlahKursi
    def jalan(self):
        print(self.merek + (" akan segera berangkat"))
    def berhenti(self):
        print(self.merek + (" akan segera sampai"))
    def tidakBeroperasi(self):
        print(self.merek + (" tidak beroperasi"))
              
    
kereta1 = MyKereta("Purwojaya", "Putih", 100)
kereta2 = MyKereta("Agro", "Merah", 80)
kereta3 = MyKereta("Taksaka", "Kuning", 70)
kereta1.merek = "Manahan"
print(kereta1.merek)
print(kereta1.warna)
print(kereta1.jumlahKursi)
print(kereta2.merek)
print(kereta2.warna)
print(kereta2.jumlahKursi)
print(kereta3.merek)
print(kereta3.warna)
print(kereta3.jumlahKursi)

kereta1.jalan()
kereta2.berhenti()
kereta3.tidakBeroperasi()
