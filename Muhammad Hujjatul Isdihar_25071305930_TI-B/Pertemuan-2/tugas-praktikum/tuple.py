#Contoh penggunaan tuple Python

#Membuat tuple
angka = (1, 2, 3, 2, 4)

#count() berfungsi menghitung jumlah nilai tertentu
jumlah_dua = angka.count(2)  #menghitung berapa kali angka 2 muncul

#index() berfungsi mengambil index kemunculan pertama nilai dalam tuple
index_tiga = angka.index(3)  #mencari posisi angka 3 dalam tuple

#Tuple bersifat immutable (tidak bisa diubah langsung)
#Jika ingin mengubah, harus dikonversi ke list
angka_list = list(angka)  #mengubah tuple ke list
angka_list.append(5)  #menambah elemen ke list

#Mengubah kembali ke tuple
angka_baru = tuple(angka_list)  #list dikonversi kembali ke tuple

#Menampilkan hasil
print(angka)  #tuple awal
print(jumlah_dua)  #jumlah angka 2
print(index_tiga)  #index angka 3
print(angka_baru)  #tuple baru
