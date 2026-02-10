#Contoh penggunaan semua method list Python

#Membuat list awal
buah = ["apel", "pisang", "ceri", "apel"]  #list berisi string

#append() berfungsi menambah elemen di akhir list
buah.append("mangga")  #menambah "mangga" ke akhir list

#insert() berfungsi menambah elemen di posisi tertentu sesuai indeks
buah.insert(1, "jeruk")  #menyisipkan "jeruk" di index 1

#extend() berfungsi menambah elemen dari iterable lain
buah.extend(["nanas", "anggur"])  #menambah banyak item sekaligus

#count() berfungsi menghitung jumlah elemen tertentu
jumlah_apel = buah.count("apel")  #menghitung berapa kali "apel" muncul di dalam list

#index() berfungsi mengambil index kemunculan pertama elemen dalam list
index_pisang = buah.index("pisang")  #mencari posisi "pisang" berupa indeksnya

#remove() berfungsi menghapus elemen berdasarkan nilai
buah.remove("ceri")  #menghapus "ceri" dari list

#pop() berfungsi menghapus elemen berdasarkan index
buah.pop(0)  #menghapus elemen di index 0

#reverse() berfungsi membalikkan urutan list
buah.reverse()  #membalik urutan elemen

#sort() mengurutkan list sesuai aturan alfanumerik
buah.sort()  #mengurutkan list secara alfabet

#copy() berfungsi menyalin list
salinan_buah = buah.copy()  #membuat salinan list

#clear() berfungsi mengosongkan list
salinan_buah.clear()  #menghapus semua elemen di list salinan

#Menampilkan hasil akhir
print(buah)  #menampilkan isi list buah
print(jumlah_apel)  #menampilkan jumlah apel
print(index_pisang)  #menampilkan index pisang
