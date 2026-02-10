#list angka awal
angka = [10, 20, 30, 40, 50]

#1.menambahkan angka 60 ke dalam list
angka.append(60)
print(angka)

#2.menghapus angka 20 dari list
angka.remove(20)
print(angka)

#3.menampilkan angka tertinggi dan terendah dari list
tertinggi = max(angka)
terendah = min(angka)
print("Angka tertinggi adalah: ", tertinggi)
print("Angka terendah adalah: ", terendah)

#4.menghitung rata-rata angka setelah perubahan list
jumlah = 0
rata = 0
for x in angka:
    jumlah = jumlah + x

rata = jumlah / len(angka)
print(rata)

#5.menampilkan seluruh isi list setelah perubahan
print(angka)
    

