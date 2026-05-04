class Pasien:
    __total_pasien = 0

    def __init__(self, id_pasien, nama, penyakit):
        self.__id = id_pasien
        self.__nama = nama
        self.__penyakit = penyakit
        Pasien.__total_pasien += 1

    @property
    def id(self):
        return self.__id

    @property
    def nama(self):
        return self.__nama

    @property
    def penyakit(self):
        return self.__penyakit

    def tampilkan_info(self):
        print(f"ID       : {self.__id}")
        print(f"Nama     : {self.__nama}")
        print(f"Penyakit : {self.__penyakit}")

    @staticmethod
    def hitung_pasien():
        return Pasien.__total_pasien


class PasienPrioritas(Pasien):
    def __init__(self, id_pasien, nama, penyakit, prioritas):
        super().__init__(id_pasien, nama, penyakit)
        self.prioritas = prioritas

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Prioritas: {self.prioritas}")
        
        if self.prioritas.lower() == "darurat":
            print("** Segera tangani! **")


p1 = Pasien("P001", "Andi", "Flu")
p1.tampilkan_info()
print("-" * 20)

p2 = PasienPrioritas("P007", "Ghani", "Sesak Napas", "Darurat")
p2.tampilkan_info()
print("-" * 20)

print(f"Total pasien terdaftar: {Pasien.hitung_pasien()}")